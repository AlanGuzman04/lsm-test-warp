def normalize_keypoints(keypoints):
    min_val = min(keypoints)
    return [k - min_val for k in keypoints]

def convert_to_text(prediction, label_map):
    return label_map.get(prediction, "")
