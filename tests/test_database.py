import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db import save_translation, get_last_translation

def test_save_translation():
    save_translation("a")
    last = get_last_translation()
    print("✅ Última traducción guardada:", last)
    assert last == "a"
