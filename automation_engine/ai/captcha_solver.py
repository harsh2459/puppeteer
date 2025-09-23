import tensorflow as tf
import numpy as np
import cv2
from config import settings

class NeuralCaptchaSolver:
    def __init__(self):
        try:
            self.model = tf.keras.models.load_model(settings.CAPTCHA_MODEL_PATH)
        except:
            self.model = None
            
    def preprocess_image(self, image_path):
        img = cv2.imread(image_path)
        img = cv2.resize(img, (128, 64))
        img = img / 255.0
        return np.expand_dims(img, axis=0)
        
    def solve_captcha(self, image_path):
        if not self.model:
            return "FAILED"
        processed = self.preprocess_image(image_path)
        prediction = self.model.predict(processed)
        return "SOLVED" if prediction[0][0] > 0.5 else "FAILED"