import socket
host = socket.gethostbyname(socket.gethostname())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Listening...")
s.bind(("192.168.56.1", 1234))
s.listen(1)
conn, address = s.accept()
n = ''
if conn:
    print(f"Connection from {address} has been established.")
    while True:
        data = conn.recv(1024)
        data = data.decode('utf-8')
        if data != '':
            print(f"{data}")
        else:
            break
else:
    s.close()
        