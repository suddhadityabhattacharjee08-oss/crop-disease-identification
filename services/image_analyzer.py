import numpy as np
from PIL import Image


def load_image(path):
    try:
        return np.array(Image.open(path).convert("RGB"))
    except FileNotFoundError:
        print("Image file not found.")
    except Exception as exc:
        print(f"Could not load image: {exc}")
    return None


class LeafImageAnalyzer:
    def __init__(self, image):
        self.image = image

    def analyze(self):
        if self.image is None:
            raise ValueError("Image could not be loaded.")
        if self.image.ndim != 3 or self.image.shape[2] != 3:
            raise ValueError("Expected an RGB color image.")

        red = self.image[:, :, 0].astype(float)
        green = self.image[:, :, 1].astype(float)
        blue = self.image[:, :, 2].astype(float)

        total_pixels = self.image.shape[0] * self.image.shape[1]

        brown_mask = (
            (red > 70) & (red > green * 1.15) & (green > blue * 1.15)
        )
        yellow_mask = (red > 120) & (green > 100) & (blue < 120)
        dark_mask = (red < 80) & (green < 80) & (blue < 80)

        return {
            "brown_percentage": float(np.mean(brown_mask) * 100),
            "yellow_percentage": float(np.mean(yellow_mask) * 100),
            "dark_percentage": float(np.mean(dark_mask) * 100),
            "total_pixels": int(total_pixels),
        }

    def generate_symptoms(self):
        analysis = self.analyze()
        symptoms = []

        if analysis["brown_percentage"] >= 5:
            symptoms.append("brown spots")
        if analysis["yellow_percentage"] >= 5:
            symptoms.append("yellow leaves")
        if analysis["dark_percentage"] >= 5:
            symptoms.append("dark leaf spots")

        return symptoms
