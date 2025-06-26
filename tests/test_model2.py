import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from model import load_model, predict_sign


def test_predict_sign():
    model = load_model("models/actionns_15.keras")
    dummy_input = np.random.rand(1, 15, 1662)  # Simula datos de entrada
    result = predict_sign(model, dummy_input)
    assert isinstance(result, int)
    print("✅ test_predict_sign aprobado")