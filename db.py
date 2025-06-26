import mysql.connector

# Configuración de tu base de datos MySQL en Laragon
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'lenguaje_senas'
}

def save_translation(palabra):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        query = "INSERT INTO traducciones (palabra) VALUES (%s)"
        cursor.execute(query, (palabra,))
        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error al insertar en la base de datos: {err}")

def get_last_translation():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        query = "SELECT palabra FROM traducciones ORDER BY id DESC LIMIT 1"
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result[0] if result else None
    except mysql.connector.Error as err:
        print(f"Error al obtener última traducción: {err}")
        return None
