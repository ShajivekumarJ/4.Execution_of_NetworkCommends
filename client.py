import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 6000
client.connect((host, port))
print("Connected to Server")
print("You can use commands like: ping google.com, ipconfig, netstat, nslookup google.com")
print("Type 'exit' to quit")
while True:
    command = input("\nEnter Network Command: ")
    client.send(command.encode())
    if command.lower() == "exit":
        break
    output = client.recv(4096).decode()
    print("\n--- Command Output ---")
    print(output)
client.close()