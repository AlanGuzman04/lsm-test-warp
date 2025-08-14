import os
import cv2

# SETTINGS
MIN_LENGTH_FRAMES = 5
LENGTH_KEYPOINTS = 1662
MODEL_FRAMES = 15

# PATHS
ROOT_PATH = os.getcwd()
FRAME_ACTIONS_PATH = os.path.join(ROOT_PATH, "frame_actions")
DATA_PATH = os.path.join(ROOT_PATH, "data")
DATA_JSON_PATH = os.path.join(DATA_PATH, "data.json")
MODEL_FOLDER_PATH = os.path.join(ROOT_PATH, "models")
MODEL_PATH = os.path.join(MODEL_FOLDER_PATH, f"actions_{MODEL_FRAMES}.keras")
KEYPOINTS_PATH = os.path.join(DATA_PATH, "keypoints")
WORDS_JSON_PATH = os.path.join(MODEL_FOLDER_PATH, "words.json")

# SHOW IMAGE PARAMETERS
FONT = cv2.FONT_HERSHEY_PLAIN
FONT_SIZE = 1.5
FONT_POS = (5, 30)

words_text = {
    "a": "A",
    "b": "B",
    "c": "C",
    "d": "D",
    "e": "E",
    "f": "F",
    "g": "G",
    "h": "H",
    "i": "I",
    "j": "J",
    "k": "K",
    "l": "L",
    "ll": "LL",
    "m": "M",
    "n": "N",
    "o": "O",
    "p": "P",
    "hola": "HOLA",
    "no": "NO",
    "si": "SI",
    "puedo_salir": "PUEDO SALIR?",
    "buenos_dias": "BUENOS DIAS",
    "buenas_tardes": "BUENOS TARDES",
    "buenas_noches": "BUENAS NOCHES",
    "gracias": "GRACIAS",
    "porfavor": "PORFAVOR",
    "q": "Q",
    "r": "R",
    "s": "S",
    "t": "T",
    "como_estas": "COMO ESTAS?",
    "tengouna_duda": "TENGO UNA DUDA",
    "puedoayudarte": "PUEDO AYUDARTE?",
    "nosvemospronto": "NOS VEMOS PRONTO",
    "me_siento_bien": "ME SIENTO BIEN",
}