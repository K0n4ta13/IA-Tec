import cv2
import numpy as np
from tensorflow.keras.models import load_model


def detect_emotion_from_frame(frame, model, labels):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (48, 48))
    img_array = resized.astype("float32") / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    img_array = np.expand_dims(img_array, axis=-1)

    pred = model.predict(img_array)
    label_idx = np.argmax(pred)
    return labels[label_idx], label_idx


if __name__ == "__main__":
    labels = ["angry", "disgust", "fear", "happy", "neutral", "sad", "surprise"]
    model = load_model("emotions_model.keras")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("No se pudo abrir la cámara.")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("No se pudo leer el frame.")
            break

        emotion, label_idx = detect_emotion_from_frame(frame, model, labels)

        cv2.putText(
            frame,
            f"Emocion: {emotion}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )

        cv2.imshow("Detección de emociones - Presiona Q para salir", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
