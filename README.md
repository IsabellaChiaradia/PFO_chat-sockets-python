# 📨 Chat Básico Cliente-Servidor con Sockets y Base de Datos
## 📚 Descripción
Este proyecto implementa un chat básico en Python utilizando sockets TCP para la comunicación entre un cliente y un servidor.
Los mensajes enviados por los clientes se almacenan automáticamente en una base de datos SQLite.

Incluye también un módulo de consultas para visualizar los mensajes almacenados.

---

## 📁 Estructura del proyecto
```
chat_sockets/
├── cliente/
│   └── cliente.py
├── servidor/
│   ├── servidor.py
│   └── chat.db
├── consultas/
│   └── leer_mensajes.py
├── venv/
│   └── (entorno virtual)
├── README.md
```
---

## 🚀 Instrucciones de uso
1. Clonar el proyecto o descargar los archivos
    ```bash
    git clone <https://github.com/IsabellaChiaradia/PFO_chat-sockets-python.git>
    ```
2. Crear y activar el entorno virtual
    ```bash
    python -m venv venv
    .\venv\Scripts\activate      # En Windows
    ```
3. Ejecutar el servidor
    ```bash
    cd servidor
    python servidor.py
    ```
4. En otra terminal. ejecutar el cliente
    ```bash
    cd cliente
    python cliente.py
    ```
Luego vas a poder enviar múltiples mensajes. <b>Escribí "éxito" para salir</b>.

## 📦 Consultar mensajes guardados
Para ver los mensajes almacenados en la base de datos:
```bash
cd consultas
python leer_mensajes.py
```
Te mostrará todos los mensajes, junto a su fecha de envío y la IP del cliente.

## 📋 Notas importantes
- El servidor maneja los errores de conexión (puerto ocupado) y problemas con la base de datos.

- Todos los mensajes se guardan en servidor/chat.db.

- Se recomienda ejecutar siempre primero el servidor y luego cliente.