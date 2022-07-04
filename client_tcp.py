import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1)

try:
    client.connect(("google.com", 80))
    client.send("GET / HTTP/1.1\nHost: www.google.com\n\n".encode())
    dados = client.recv(2024).decode()
    print(dados)
except:
    print('Error')