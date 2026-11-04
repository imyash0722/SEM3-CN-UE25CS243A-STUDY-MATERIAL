import socket

echoClient =  socket.socket();

echoClient.connect(("127.0.0.1", 32007));

echoClient.send("Welcome to campus after a long gap!!".encode());

msgReceived = echoClient.recv(1024);

print("At client: %s"%msgReceived.decode());

