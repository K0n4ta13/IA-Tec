import os
import cv2

INPUT_DIR = "faces"
OUTPUT_DIR = "processed_faces"
IMG_SIZE = (224, 224)
GRAYSCALE = False


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for filename in os.listdir(INPUT_DIR):
        input_path = os.path.join(INPUT_DIR, filename)

        img = cv2.imread(input_path)
        if img is None:
            print(f"Error leyendo {filename}, se omite.")
            continue

        if GRAYSCALE:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        img = cv2.resize(img, IMG_SIZE)

        output_path = os.path.join(OUTPUT_DIR, filename)
        cv2.imwrite(output_path, img)

    print(f"Todas las imágenes han sido procesadas y guardadas en: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
