# Modelo LSTM para Reconocimiento de Lengua de Señas Peruana (LSP)
# LSTM Model for Peruvian Sign Language (LSP) Recognition

## Descripción / Description

**Español:**
Este es un modelo de una red neuronal LSTM que traduce Lengua de Señas Peruana (LSP) a texto y voz. Utiliza MediaPipe para obtener los puntos clave de las señas y TensorFlow/Keras para el entrenamiento de la red neuronal. El proyecto incluye una interfaz gráfica de usuario (GUI) para facilitar su uso.

**English:**
This is an LSTM neural network model that translates Peruvian Sign Language (LSP) to text and speech. It uses MediaPipe to extract keypoints from sign gestures and TensorFlow/Keras for neural network training. The project includes a graphical user interface (GUI) for ease of use.

## Requisitos del Sistema / System Requirements

- Python 3.7 o superior / Python 3.7 or higher
- Cámara web / Webcam
- Windows 10/11 o Linux Ubuntu 18.04+ / Windows 10/11 or Linux Ubuntu 18.04+
- Git

## Instalación / Installation

### Windows (PowerShell)

1. **Clonar el repositorio / Clone the repository:**
   ```powershell
   git clone https://github.com/tu-usuario/modelo_lstm_lsp.git
   cd modelo_lstm_lsp
   ```

2. **Crear un entorno virtual / Create a virtual environment:**
   ```powershell
   python -m venv venv
   ```

3. **Activar el entorno virtual / Activate the virtual environment:**
   ```powershell
   .\\venv\\Scripts\\Activate.ps1
   ```
   
   *Nota: Si hay problemas con la política de ejecución, ejecutar:*
   *Note: If there are execution policy issues, run:*
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

4. **Instalar dependencias / Install dependencies:**
   ```powershell
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

### Linux/macOS

1. **Clonar el repositorio / Clone the repository:**
   ```bash
   git clone https://github.com/tu-usuario/modelo_lstm_lsp.git
   cd modelo_lstm_lsp
   ```

2. **Crear un entorno virtual / Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

3. **Activar el entorno virtual / Activate the virtual environment:**
   ```bash
   source venv/bin/activate
   ```

4. **Instalar dependencias / Install dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Uso / Usage

### Ejecutar la aplicación principal / Run the main application
```bash
python app.py
```

### Scripts individuales / Individual scripts
```bash
# Capturar muestras / Capture samples
python capture_samples.py

# Normalizar muestras / Normalize samples
python normalize_samples.py

# Crear keypoints / Create keypoints
python create_keypoints.py

# Entrenar modelo / Train model
python training_model.py

# Evaluar modelo / Evaluate model
python evaluate_model.py

# Ejecutar con GUI / Run with GUI
python main.py
```

## Scripts Principales / Main Scripts

- **capture_samples.py** → Captura las muestras y las ubica en la carpeta frame_actions / Captures samples and places them in the frame_actions folder
- **normalize_samples.py** → Normaliza las muestras para que todas tengan la misma cantidad de frames (importante) / Normalizes samples so they all have the same number of frames (important)
- **create_keypoints.py** → Crea los keypoints que se usarán en el entrenamiento / Creates keypoints to be used in training
- **training_model.py** → Entrena la red neuronal / Trains the neural network
- **evaluate_model.py** → Donde se realiza la prueba de la red neuronal / Where neural network testing is performed
- **main.py** → GUI para usar el traductor / GUI to use the translator
- **app.py** → Aplicación principal con interfaz web / Main application with web interface

## Scripts Secundarios / Secondary Scripts

- **model.py** → Aquí se ajusta el modelo de la red neuronal / Neural network model configuration
- **constants.py** → Ajustes de la red neuronal / Neural network settings
- **helpers.py** → Funciones que se utilizan en los scripts principales / Functions used in main scripts

## Pasos para Probar la Red Neuronal / Steps to Test the Neural Network

**Español:**
1. Capturar las muestras con `capture_samples.py`
2. Normalizar las muestras con `normalize_samples.py`
3. Generar los archivos .h5 (keypoints) de cada palabra con `create_keypoints.py`
4. Entrenar el modelo con `training_model.py`
5. Realizar pruebas con `evaluate_model.py`
6. Ejecutar la aplicación final con `main.py` o `app.py`

**English:**
1. Capture samples with `capture_samples.py`
2. Normalize samples with `normalize_samples.py`
3. Generate .h5 files (keypoints) for each word with `create_keypoints.py`
4. Train the model with `training_model.py`
5. Test with `evaluate_model.py`
6. Run the final application with `main.py` or `app.py`

## Estructura del Proyecto / Project Structure

```
modelo_lstm_lsp/
├── data/                    # Datos de entrenamiento / Training data
├── frame_actions/           # Muestras capturadas / Captured samples
├── models/                  # Modelos entrenados / Trained models
├── venv/                    # Entorno virtual / Virtual environment
├── app.py                   # Aplicación web principal / Main web application
├── main.py                  # GUI principal / Main GUI
├── capture_samples.py       # Captura de muestras / Sample capture
├── normalize_samples.py     # Normalización / Normalization
├── create_keypoints.py      # Creación de keypoints / Keypoint creation
├── training_model.py        # Entrenamiento / Training
├── evaluate_model.py        # Evaluación / Evaluation
├── model.py                 # Configuración del modelo / Model configuration
├── constants.py             # Constantes / Constants
├── helpers.py               # Funciones auxiliares / Helper functions
├── requirements.txt         # Dependencias / Dependencies
└── README.md               # Este archivo / This file
```

## Solución de Problemas / Troubleshooting

### Windows
- **Error de política de ejecución:** Ejecutar PowerShell como administrador y usar `Set-ExecutionPolicy RemoteSigned`
- **Problemas con OpenCV:** Instalar Visual C++ Redistributable
- **Error de cámara:** Verificar que no esté siendo usada por otra aplicación

### Linux
- **Problemas con TensorFlow:** Instalar `python3-dev` y `build-essential`
- **Error de permisos de cámara:** Agregar usuario al grupo `video`
- **Dependencias del sistema:** `sudo apt install python3-tk python3-dev`

### General
- **Memoria insuficiente:** Reducir batch_size en constants.py
- **Modelo no carga:** Verificar que el archivo .h5 existe en la carpeta models/
- **Rendimiento lento:** Verificar que TensorFlow detecta la GPU (si está disponible)

## Video Explicativo / Explanatory Video

https://youtu.be/3EK0TxfoAMk

*Nota: Pronto subiré otro video explicando las mejoras.*
*Note: I will soon upload another video explaining the improvements.*

## Contribuir / Contributing

1. Fork el proyecto / Fork the project
2. Crear una rama para tu feature / Create a feature branch
3. Commit tus cambios / Commit your changes
4. Push a la rama / Push to the branch
5. Abrir un Pull Request / Open a Pull Request

## Licencia / License

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Autor / Author

Alan Guzmán

---

**¡Gracias por usar este proyecto! / Thank you for using this project!**
