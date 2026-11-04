import socket

echoSocket = socket.socket();

echoSocket.bind(("127.0.0.1", 32007));

echoSocket.listen();

while(True):

    (clientSocket, clientAddress) = echoSocket.accept();

    while(True):

        data = clientSocket.recv(1024);

        print("At Server: %s"%data);


        if(data!=b''):


            clientSocket.send(data);

            break;
