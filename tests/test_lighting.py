import cv2
import numpy as np
import pytest

def calculate_brightness(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return np.mean(gray)

def test_lighting_condition():
    cap = cv2.VideoCapture(0)
    assert cap.isOpened(), "No se pudo acceder a la cámara"

    ret, frame = cap.read()
    cap.release()

    assert ret, "No se pudo capturar imagen de la cámara"

    brightness = calculate_brightness(frame)
    print(f"\n🔆 Brillo promedio: {brightness:.2f}")

    # Evaluación de la iluminación
    if brightness < 100:
        pytest.fail("❌ Iluminación insuficiente: la imagen está demasiado oscura.")
    elif brightness > 200:
        pytest.fail("❌ Iluminación excesiva: la imagen está demasiado brillante.")
    else:
        print("✅ Iluminación adecuada para el reconocimiento.")
