import socket
import time

s = socket.socket()
s.bind(("172.16.14.50", 5002))
s.listen()
print("Listening!")
#time.sleep(5)
print("Ready to accept")
conn, address = s.accept()
print(address)
conn.send(b"Hello World! Will this get sent?")