# consultas/leer_mensajes.py

import sqlite3
from datetime import datetime

def conectar_db(nombre_db):
    """Conecta a la base de datos SQLite"""
    try:
        conn = sqlite3.connect(nombre_db)
        return conn
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def leer_mensajes(conn):
    """Lee y muestra todos los mensajes almacenados"""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, contenido, fecha_envio, ip_cliente FROM mensajes")
        mensajes = cursor.fetchall()

        if mensajes:
            print("\nMensajes almacenados:\n")
            for mensaje in mensajes:
                id, contenido, fecha_envio, ip_cliente = mensaje
                print(f"[{id}] {fecha_envio} - {ip_cliente}: {contenido}")
        else:
            print("No hay mensajes en la base de datos.")

    except sqlite3.Error as e:
        print(f"Error al leer los mensajes: {e}")

def main():
    # Ruta relativa al archivo de base de datos
    db_path = "../servidor/chat.db"

    # Conectar a la base de datos
    conn = conectar_db(db_path)

    if conn:
        leer_mensajes(conn)
        conn.close()

if __name__ == "__main__":
    main()
