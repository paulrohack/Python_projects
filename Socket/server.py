import socket
host = socket.gethostbyname(socket.gethostname())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Listening...")
s.bind(("27.59.72.111", 1234))
s.listen(1)
conn, address = s.accept()

if conn:
    print(f"Connection from {address} has been established.")
    data = conn.recv(1024)
    name = data.decode('utf-8') 
    print(f"{data} joined in ....")

    while True:
        data = conn.recv(1024)
        data = data.decode('utf-8')     
        if data != '':
            print(f"{name}: {data}")
        else:
            s.close()
else:
    s.close()
         