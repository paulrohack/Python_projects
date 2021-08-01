import socket
host = socket.gethostbyname(socket.gethostname())
print("Waiting for Valid connection...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.56.1", 1234))
s.sendall(b'Connected')
while True:
    d = input("data: ").encode('utf-8')
    s.sendall(d)
