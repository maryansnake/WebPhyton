import socket
import datetime

host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()

print(f"Сервер слухає на {host}:{port}...")

client_socket, client_address = server_socket.accept()
print(f"З'єднано з {client_address}")
data = client_socket.recv(1024).decode('utf-8')

import time
time.sleep(5)

if data:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Отримано від клієнта ({client_address}): {data}")
    print(f"Час отримання: {current_time}")
    response = "Дані успішно отримано."
else:
    response = "Помилка при отриманні даних."

client_socket.send(response.encode('utf-8'))

client_socket.close()
server_socket.close()
