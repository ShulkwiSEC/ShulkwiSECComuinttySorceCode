# Server => Clintes
import socket # NetWork lOw Level
import threading #
import re
import time
from Gold import *

HOST = '0.0.0.0'
PORT = 8000

clients = []

def handle_client(client_socket, client_address):
    clients.append(client_socket)
    print(f"[NEW CONNECTION] {client_address} connected.")

    while True:
        try:
            message = client_socket.recv(1024).decode('UTF-8')
        except ConnectionResetError:
            client.remove(client_socket)
            client_socket.close()
        if not message:
            break
        if(re.search(r"\(.+\)",str(message))):
                time.sleep(1)
                result = Gold(word=str(message)).result
                if client == client_socket:
                    client.send(str(result).encode('UTF-8'))
        for client in clients:
            if client != client_socket:
                client.send(message.encode('UTF-8'))
    
    clients.remove(client_socket)
    client_socket.close()
    print(f"[DISCONNECTED] {client_address} disconnected.")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind((HOST, PORT))
    except OSError:
        print(f'Port {PORT} already in use')
        exit(1)
    server_socket.listen()

    print(f"[SERVER STARTED] Listening on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()

if __name__ == "__main__":
    start_server()