import os
import pandas as pd

KEYPOINTS_DIR = "data/keypoints"

for fname in os.listdir(KEYPOINTS_DIR):
    if fname.endswith(".h5"):
        path = os.path.join(KEYPOINTS_DIR, fname)
        try:
            data = pd.read_hdf(path, key='data')
            if "sample" not in data.columns:
                print(f"❌ El archivo {fname} NO tiene columna 'sample'")
            else:
                print(f"✅ {fname} OK")
        except Exception as e:
            print(f"⚠️ Error al leer {fname}: {e}")
