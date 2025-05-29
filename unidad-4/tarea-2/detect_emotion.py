from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.models import load_model
import argparse
import os
import sys


def detect_emotion(image_path):
    labels = ["angry", "disgust", "fear", "happy", "neutral", "sad", "surprise"]
    model = load_model("emotions_model.keras")
    img = image.load_img(image_path, color_mode="grayscale", target_size=(48, 48))
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    pred = model.predict(img_array)
    label = np.argmax(pred)

    print(labels[label])
    print(label)
    return labels[label]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Detecta la emoción en una imagen facial en escala de grises 48x48."
    )
    parser.add_argument("image_path", help="Ruta de la imagen a analizar")

    args = parser.parse_args()

    if not os.path.exists(args.image_path):
        print(f"La ruta {0} a la imagen no existe:", args.image_path)
        sys.exit(1)

    emotion = detect_emotion(args.image_path)
    print("Emoción detectada:", emotion)
