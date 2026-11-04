# An example script to connect to Google using socket
# programming in Python
import socket
import sys

port = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket successfully created")

# connecting to the server
host_ip = "142.250.192.36"
s.connect((host_ip, port))

print ("the socket has successfully connected to google")
