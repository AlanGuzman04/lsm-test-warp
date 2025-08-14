import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from utils import convert_to_text



def test_convert_to_text():
    prediction = 2
    label_map = {0: "a", 1: "b", 2: "c"}
    assert convert_to_text(prediction, label_map) == "b"
    print("✅ test_convert_to_text aprobado")
