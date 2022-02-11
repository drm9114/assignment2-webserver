# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a server socket
  serverSocket.bind(("127.0.0.1", port))
  #Fill in start
  serverSocket.listen(1)
  #Fill in end

  while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Fill in start      #Fill in end
    try:

      try:
        message = connectionSocket.recv(1024).decode() #Fill in start    #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        #print('file open...')
        outputdata = f.read() #Fill in start     #Fill in end
        #print(outputdata)
        #Send one HTTP header line into socket.
        #Fill in start
        http_str = "HTTP/1.1 200 OK\r\n\r\n"
        #print(http_str)
        connectionSocket.send(http_str.encode())
        #Fill in end
        #print("sent http_str")

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
          #print("In the loop", i)
          connectionSocket.send(outputdata[i].encode())
        #print("left for loop")
        #connectionSocket.send("\r\n".encode())
        connectionSocket.close()
        #print("socket closed")
      except IOError:
        # Send response message for file not found (404)
        #print("IOError")
        http_str = "HTTP/1.1 404 Not Found\r\n\r\n"
        #Fill in start
        connectionSocket.send(http_str.encode())
        http_str = "404 Not Found \r\n"
        connectionSocket.send(http_str.encode())
        #Fill in end


        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end

    except (ConnectionResetError, BrokenPipeError):
      #print("connection err")
      pass
    finally:
      f.close()

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)