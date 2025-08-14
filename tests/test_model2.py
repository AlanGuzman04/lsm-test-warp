import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from model import load_model, predict_sign

def test_load_model():
    model_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'models', 'actions_15.keras'))
    model = load_model(model_path)
    assert model is not None
    print("✅ test_load_model aprobado")

def test_predict_sign():
    model_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'models', 'actions_15.keras'))
    model = load_model(model_path)
    dummy_input = np.random.rand(1, 15, 1662)  # Simula datos de entrada
    result = predict_sign(model, dummy_input)
    assert isinstance(result, int)
    print("✅ test_predict_sign aprobado")