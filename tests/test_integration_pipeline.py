import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from model import load_model, predict_sign
from utils import convert_to_text
from db import save_translation, get_last_translation

def test_full_prediction_pipeline():
    input_data = np.random.rand(1, 15, 1662)

    model = load_model("data/keypoints/a.h5")

    prediction = predict_sign(model, input_data)

    label_map = {0: "a", 1: "b", 2: "c"}
    text = convert_to_text(prediction, label_map)

    save_translation(text)

    assert get_last_translation() == text
