import socket
host = socket.gethostbyname(socket.gethostname())
print("Waiting for Valid connection...")
user = input("Username: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("103.161.57.91", 1234))
s.sendall(b'{user}')

while True:
        d = input("data: ").encode('utf-8')
        s.sendall(d)
