import socket
import subprocess
import platform
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 6000
server.bind((host, port))
server.listen(1)
print("Server started... Waiting for connection...")
conn, addr = server.accept()
print("Connected to:", addr)
while True:
    command = conn.recv(1024).decode()
    if command.lower() == "exit":
        print("Client disconnected.")
        break
    print("Command received:", command)
    try:
        output = subprocess.check_output(command, shell=True)
        conn.send(output)
    except Exception as e:
        conn.send(str(e).encode())
conn.close()
server.close()