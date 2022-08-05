import socket
import json

SERVER = "127.0.0.1"
PORT = 8000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
client.sendall(bytes("This is from Client",'UTF-8'))

def write_json(new_data, filename='users.json'):
  with open(filename, 'r+') as file:
    # First we load existing data into a dict.
    file_data = json.load(file)
    # Join new_data with file_data inside emp_details
    file_data["log"].append(new_data)
    # Sets file's current position at offset.
    file.seek(0)
    # convert back to json.
    json.dump(file_data, file, indent=4)

while True:
  in_data =  client.recv(1024)
  msg = in_data.decode()

  data = {"username": "Server", "message": msg}
  write_json(data)

  print("From Server :" , msg)
  out_data = input()
  client.sendall(bytes(out_data,'UTF-8'))
  if out_data=='bye':
    break
client.close()