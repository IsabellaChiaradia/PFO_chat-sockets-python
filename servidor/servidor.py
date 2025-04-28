import socket
import sqlite3
import datetime
import threading

# ---------------------------
# Inicializar base de datos
# ---------------------------
def inicializar_db():
    try:
        conexion = sqlite3.connect("chat.db")
        cursor = conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mensajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contenido TEXT NOT NULL,
                fecha_envio TEXT NOT NULL,
                ip_cliente TEXT NOT NULL
            )
        ''')
        conexion.commit()
        conexion.close()
    except Exception as e:
        print(f"Error al inicializar la base de datos: {e}")
        exit()

# ---------------------------
# Guardar mensaje en la DB
# ---------------------------
def guardar_mensaje(contenido, ip_cliente):
    try:
        conexion = sqlite3.connect("chat.db")
        cursor = conexion.cursor()
        fecha_envio = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO mensajes (contenido, fecha_envio, ip_cliente) VALUES (?, ?, ?)",
                       (contenido, fecha_envio, ip_cliente))
        conexion.commit()
        conexion.close()
        return fecha_envio
    except Exception as e:
        print(f"Error al guardar el mensaje: {e}")
        return None

# ---------------------------
# Manejar conexión con cliente
# ---------------------------
def manejar_cliente(conexion, direccion):
    ip_cliente = direccion[0]
    print(f"Cliente conectado desde {ip_cliente}")
    while True:
        try:
            mensaje = conexion.recv(1024).decode()
            if not mensaje:
                break
            fecha = guardar_mensaje(mensaje, ip_cliente)
            if fecha:
                respuesta = f"Mensaje recibido: {fecha}"
            else:
                respuesta = "Error al guardar el mensaje"
            conexion.send(respuesta.encode())
        except Exception as e:
            print(f"Error en la conexión con {ip_cliente}: {e}")
            break
    conexion.close()
    print(f"Conexión con {ip_cliente} cerrada")

# ---------------------------
# Configuración del socket TCP/IP
# ---------------------------
def iniciar_servidor():
    host = '127.0.0.1'
    puerto = 5000
    try:
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.bind((host, puerto))
        servidor.listen(5)
        print(f"Servidor escuchando en {host}:{puerto}...")
        while True:
            conexion, direccion = servidor.accept()
            hilo = threading.Thread(target=manejar_cliente, args=(conexion, direccion))
            hilo.start()
    except OSError as e:
        print(f"Error con el socket: {e}")
    except Exception as e:
        print(f"Error general en el servidor: {e}")

# ---------------------------
# Main
# ---------------------------
if __name__ == "__main__":
    inicializar_db()
    iniciar_servidor()
