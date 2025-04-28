import socket

# ---------------------------
# Cliente TCP para enviar mensajes
# ---------------------------
def iniciar_cliente():
    host = '127.0.0.1'
    puerto = 5000

    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((host, puerto))
        print("Conectado al servidor. Escribí 'éxito' para salir.")
        
        while True:
            mensaje = input("Mensaje > ")
            if mensaje.lower() == 'éxito':
                break
            cliente.send(mensaje.encode())
            respuesta = cliente.recv(1024).decode()
            print(f"Servidor: {respuesta}")
            
        cliente.close()
    except Exception as e:
        print(f"No se pudo conectar con el servidor: {e}")

# ---------------------------
# Main
# ---------------------------
if __name__ == "__main__":
    iniciar_cliente()
