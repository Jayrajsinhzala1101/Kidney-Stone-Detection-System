import sys
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Change this if your model file name/path is different
MODEL_PATH = r"C:\Users\Admin\Downloads\New folder (4)\kidney_stone_detection_model.h5"

# Label mapping based on your notebook
LABELS = {0: "Normal", 1: "Stone"}

def predict_image(img_path: str):
    # Load model
    model = load_model(MODEL_PATH)

    # Load + preprocess image (same as training)
    img = image.load_img(img_path, target_size=(150, 150))
    arr = image.img_to_array(img)              # (150,150,3)
    arr = arr / 255.0                          # rescale
    arr = np.expand_dims(arr, axis=0)          # (1,150,150,3)

    # Predict
    pred = model.predict(arr, verbose=0)[0]    # e.g. [0.2, 0.8]
    idx = int(np.argmax(pred))
    confidence = float(np.max(pred)) * 100

    return LABELS.get(idx, str(idx)), confidence, pred.tolist()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python predict.py path_to_image.jpg")
        sys.exit(1)

    img_path = sys.argv[1]
    label, conf, raw = predict_image(img_path)

    print(f"Prediction: {label}")
    print(f"Confidence: {conf:.2f}%")
    print(f"Raw scores: {raw}")
