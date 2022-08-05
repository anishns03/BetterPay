import socket
import json

LOCALHOST = "127.0.0.1"
PORT = 8000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)
print("Server started")
print("Waiting for client request..")
clientConnection,clientAddress = server.accept()
print("Connected clinet :" , clientAddress)
msg = ''

def write_json(new_data, filename='users.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["log"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

while True:
  in_data = clientConnection.recv(1024)
  msg = in_data.decode()

  data = {"username": "Client", "message": msg}
  write_json(data)

  if msg=='bye':
    break
  print("From Client :" , msg)
  out_data = input()
  clientConnection.send(bytes(out_data,'UTF-8'))
print("Client disconnected....")
clientConnection.close()
