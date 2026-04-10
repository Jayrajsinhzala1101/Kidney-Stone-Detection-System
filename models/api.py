from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import io
import os

app = FastAPI(title="Kidney Stone Detection API")

# ✅ Put your model path here (dynamic for deployment)
BASE_API_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_API_DIR, "kidney_stone_detection_model.h5")

LABELS = {0: "Normal", 1: "Stone"}
IMG_SIZE = (150, 150)

# ✅ Load model ONCE (fast + correct)
try:
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

    model = load_model(MODEL_PATH, compile=False)


except Exception as e:
    # If model fails to load, API should still start and show a clear error
    model = None
    load_error = str(e)


def preprocess_image(file_bytes: bytes) -> np.ndarray:
    img = Image.open(io.BytesIO(file_bytes)).convert("RGB")
    img = img.resize(IMG_SIZE)
    arr = np.array(img, dtype=np.float32) / 255.0
    arr = np.expand_dims(arr, axis=0)  # (1,150,150,3)
    return arr


@app.get("/")
def home():
    if model is None:
        return {"status": "error", "message": "Model not loaded", "details": load_error}
    return {"status": "ok", "message": "Model loaded. Use POST /predict"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if model is None:
        return JSONResponse(
            status_code=500,
            content={"error": "Model not loaded", "details": load_error}
        )

    try:
        file_bytes = await file.read()
        x = preprocess_image(file_bytes)

        pred = model.predict(x, verbose=0)[0]  # e.g. [0.2, 0.8]
        idx = int(np.argmax(pred))
        confidence = float(np.max(pred)) * 100

        return {
            "filename": file.filename,
            "prediction": LABELS.get(idx, str(idx)),
            "confidence": round(confidence, 2),
            "raw_scores": [float(p) for p in pred]
        }

    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})
