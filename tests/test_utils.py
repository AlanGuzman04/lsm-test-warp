import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from utils import normalize_keypoints




def test_normalize_keypoints():
    input_data = [0.5, 0.6, 0.7]
    expected = [0.0, 0.1, 0.2]
    result = normalize_keypoints(input_data)
    assert result == pytest.approx(expected, abs=0.01)
    print("✅ test_normalize_keypoints aprobado")
    print("Los tensores estan normalizados correctamente.")
