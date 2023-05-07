from socket import *
import sys

#Menentukan socket ke alamat dan port yang telah ditentukan
server_host = 'localhost'
port = 8081

# Membuat TCP socket
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((server_host, port))
server_socket.listen(1)
print('The server is ready to receive')

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, address = server_socket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]

        if filename == '/' or filename == '/ ':
            filename = 'index.html'
        f = open(filename[1:])

        outputdata = f.read()
        
        #Send one HTTP header line into socket
        http_ok_response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        connectionSocket.send(http_ok_response.encode())
        
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
        
        connectionSocket.close()
    except IOError:
        #Send response message forfile not found
        not_found_response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<!DOCTYPE html><html><head><title>404 Not Found</title></head><body><h1>404 Not Found</h1><p>The requested file could not be found.</p></body></html>"
        connectionSocket.send(not_found_response.encode())

        #Close client socket
        connectionSocket.close()

server_socket.close()
#Terminate the program after sending the corresponding data
sys.exit()
