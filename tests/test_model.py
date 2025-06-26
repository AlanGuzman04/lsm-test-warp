import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from model import load_model

def test_load_model():
    model = load_model("../data/keypoints/hola.h5")
    assert model is not None
    print("✅ test_load_model aprobado")


