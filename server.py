import asyncio
import base64
import cv2
import numpy as np
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from mediapipe.python.solutions.holistic import Holistic
from keras.models import load_model

from helpers import mediapipe_detection, extract_keypoints, get_word_ids, there_hand
from constants import *
from evaluate_model import normalize_keypoints

# --- Constantes de Configuración (adaptadas de main.py) ---
MARGIN_FRAME = 1
DELAY_FRAMES = 3

# --- Inicialización de la App FastAPI ---
app = FastAPI()

# --- Configuración de CORS ---
# Permite que tu frontend (ej. localhost:3000) se comunice con este backend.
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5173", # Añadido para el servidor de desarrollo de Vite
    "http://localhost:8080",
    "http://192.168.137.251:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Lógica de Detección de Señas (adaptada de main.py) ---
class SignLanguageProcessor:
    def __init__(self):
        self.holistic_model = Holistic()
        self.model = load_model(MODEL_PATH)
        self.word_ids = get_word_ids(WORDS_JSON_PATH)
        self.kp_seq = []
        self.sentence = []
        self.count_frame = 0
        self.fix_frames = 0
        self.recording = False
        print("LSM Processor initialized.")

    def process_frame(self, frame):
        """Procesa un solo frame y retorna la palabra detectada si la hay."""
        
        # Lógica de detección principal
        results = mediapipe_detection(frame, self.holistic_model)
        
        hand_detected = there_hand(results)
        
        if hand_detected or self.recording:
            self.recording = False
            self.count_frame += 1
            if self.count_frame > MARGIN_FRAME:
                self.kp_seq.append(extract_keypoints(results))
            
            # --- LOG DE DEPURACIÓN ---
            print(f"-> Mano detectada. Acumulando frames... Total: {len(self.kp_seq)}")

        else:
            # --- LOG DE DEPURACIÓN ---
            if self.count_frame > 0:
                print(f"!! Mano perdida. Se habían acumulado {self.count_frame} frames.")

            if self.count_frame >= MIN_LENGTH_FRAMES + MARGIN_FRAME:
                self.fix_frames += 1
                if self.fix_frames < DELAY_FRAMES:
                    self.recording = True
                    return None
                
                self.kp_seq = self.kp_seq[: - (MARGIN_FRAME + DELAY_FRAMES)]
                
                if len(self.kp_seq) >= MIN_LENGTH_FRAMES:
                    # --- LOG DE DEPURACIÓN ---
                    print(f"** Intentando predecir con una secuencia de {len(self.kp_seq)} frames.")
                    
                    kp_normalized = normalize_keypoints(self.kp_seq, int(MODEL_FRAMES))
                    res = self.model.predict(np.expand_dims(kp_normalized, axis=0))[0]
                    confidence = res[np.argmax(res)]
                    
                    # --- LOG DE DEPURACIÓN ---
                    print(f"** Predicción: {self.word_ids[np.argmax(res)]} | Confianza: {confidence:.4f}")
                    
                    if confidence > 0.7:
                        word_id = self.word_ids[np.argmax(res)].split('-')[0]
                        sent = words_text.get(word_id)
                        self.sentence.insert(0, sent)
                        
                        # Reiniciar y retornar la palabra detectada
                        self.reset_state()
                        return sent

            self.reset_state()

        return None

    def reset_state(self):
        """Resetea el estado para la siguiente detección."""
        self.recording = False
        self.fix_frames = 0
        self.count_frame = 0
        self.kp_seq = []


# --- Endpoint de WebSocket ---
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Client connected")
    processor = SignLanguageProcessor()
    
    try:
        while True:
            # Recibir frame del frontend (en formato de bytes)
            image_bytes = await websocket.receive_bytes()
            
            # Decodificar la imagen directamente desde los bytes
            nparr = np.frombuffer(image_bytes, np.uint8)
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            # Procesar el frame
            detected_word = processor.process_frame(frame)
            
            # Si se detectó una palabra, enviarla de vuelta al frontend
            if detected_word:
                print(f"Detected word: {detected_word}")
                await websocket.send_text(detected_word)

    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"An error occurred: {e}")


@app.get("/")
def read_root():
    return {"message": "Servidor de LSM (Lenguaje de Señas Mexicano) funcionando."}

# --- Ejecución del Servidor ---
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)