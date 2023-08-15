import socket

targethost = "www.google.com.br"
targetport = 80

# creating a socket object

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the client

client.connect((targethost, targetport))

# sending data

client.send(b"GET / HTTP/1.1\r\nHost: google.com.br\r\n\r\n")

response = client.recv(4096)

print(response.decode)

client.close()

