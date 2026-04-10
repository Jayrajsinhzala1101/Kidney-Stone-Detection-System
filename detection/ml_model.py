import numpy as np
from PIL import Image
import os
from django.conf import settings
import logging
from tensorflow import keras

logger = logging.getLogger(__name__)

class KidneyStonePredictor:
    """
    Machine Learning Model Handler for Kidney Stone Detection.

    Loads a Keras/TensorFlow model if available; otherwise falls back to a dummy
    predictor so the app keeps running in demo mode.
    """
    
    def __init__(self, model_path=None):
        """
        Initialize the ML model predictor.
        
        Args:
            model_path (str): Path to the .h5 Keras model file
        """
        self.model = None
        # The provided model is expected at the project root by default.
        self.model_path = model_path or os.path.join(settings.BASE_DIR, 'kidney_stone_cnn.h5')

        # Default labels for a binary kidney stone classifier.
        self.class_names = ['No Kidney Stone', 'Kidney Stone']
        self.load_model()
    
    def load_model(self):
        """
        Load the ML model from a .h5 file.
        """
        try:
            if os.path.exists(self.model_path):
                # Load the Keras model (HDF5/legacy format)
                self.model = keras.models.load_model(self.model_path)
                logger.info(f"Kidney stone model loaded successfully from {self.model_path}")
            else:
                logger.warning(f"Model file not found at {self.model_path}")
                self.model = self._create_dummy_model()
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            self.model = self._create_dummy_model()
    
    def _create_dummy_model(self):
        """
        Create a dummy model for testing until a real model is provided.
        """
        class DummyModel:
            def predict(self, X, verbose=0):
                # Return random probabilities for a binary classifier
                probas = np.random.rand(X.shape[0], 2).astype("float32")
                probas = probas / probas.sum(axis=1, keepdims=True)
                return probas
        
        return DummyModel()

    def _get_expected_input_size(self):
        """
        Try to infer model input size (H, W, C). Falls back to 224x224x3.
        """
        try:
            if getattr(self.model, "input_shape", None):
                # Typical: (None, H, W, C)
                _, h, w, c = self.model.input_shape
                if h and w and c:
                    return int(h), int(w), int(c)
        except Exception:
            pass

        return 224, 224, 3
    
    def preprocess_image(self, image):
        """
        Preprocess image for model prediction
        
        Args:
            image: PIL Image or numpy array
            
        Returns:
            numpy array: Preprocessed image
        """
        try:
            # Convert to PIL Image if it's not already
            if isinstance(image, np.ndarray):
                image = Image.fromarray(image)

            h, w, c = self._get_expected_input_size()

            # Convert to correct color mode
            if c == 1:
                if image.mode != 'L':
                    image = image.convert('L')
            else:
                if image.mode != 'RGB':
                    image = image.convert('RGB')

            # Resize image to model expected size
            image = image.resize((w, h))
            
            # Convert to numpy array
            image_array = np.array(image)
            
            # Normalize pixel values (0-255 to 0-1)
            image_array = image_array.astype('float32') / 255.0

            # Ensure channel dimension exists for grayscale models
            if c == 1 and len(image_array.shape) == 2:
                image_array = np.expand_dims(image_array, axis=-1)
            
            # Add batch dimension if needed
            if len(image_array.shape) == 3:
                image_array = np.expand_dims(image_array, axis=0)
            
            return image_array
            
        except Exception as e:
            logger.error(f"Error preprocessing image: {str(e)}")
            raise
    
    def predict(self, image):
        """
        Predict kidney stone presence from image.
        
        Args:
            image: PIL Image or numpy array
            
        Returns:
            dict: Prediction results with label and confidence
        """
        try:
            # Preprocess image
            processed_image = self.preprocess_image(image)
            
            # Make prediction with Keras model
            predictions = self.model.predict(processed_image, verbose=0)

            # Normalize output shape handling:
            # - (1, 1) sigmoid: value is probability of "Kidney Stone"
            # - (1, 2) softmax: index maps to class_names
            pred = np.array(predictions)
            if pred.ndim == 2 and pred.shape[1] == 1:
                p_stone = float(pred[0][0])
                predicted_class = 1 if p_stone >= 0.5 else 0
                confidence = p_stone if predicted_class == 1 else (1.0 - p_stone)
            else:
                predicted_class = int(np.argmax(pred[0]))
                confidence = float(pred[0][predicted_class])

            label = self.class_names[predicted_class] if predicted_class < len(self.class_names) else "Unknown"
            has_stone = (label.lower().find("kidney stone") != -1) or (predicted_class == 1)

            return {
                'label': label,
                'confidence': confidence,
                'has_stone': has_stone,
                'class_id': predicted_class
            }
            
        except Exception as e:
            logger.error(f"Error making prediction: {str(e)}")
            return {
                'label': 'Detection Failed',
                'confidence': 0.0,
                'has_stone': False,
                'class_id': -1
            }

# Global instance for easy access
predictor = KidneyStonePredictor()