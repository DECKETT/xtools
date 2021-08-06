import socket
bangrab = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bangrab.connect (("192.168.0.50", 22))
print (bangrab.recv(4096))