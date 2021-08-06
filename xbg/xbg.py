import socket
bangrab = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bangrab.connect (("TARGET_IP", TARGET_PORT))
print (bangrab.recv(4096))