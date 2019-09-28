import sys
import socket
from tracks import solidPulse
from utils import lampOff
from threading import Thread
import subprocess
import multiprocessing

MAX_LENGTH = 4096
END_PROCESS = False

def programs(inn):

	if inn == "on":
		solidPulse.controller("1")
		return "on"
	if inn == "off":
		END_PROCESS = True
		solidPulse.controller("0")
#		stop_threads = True		
#		subprocess.call("./utils/processKiller.sh")
#		lampOff.run()
		return "off"
	if inn == "quit":
		serversocket.close()
		sys.exit(0)
	return"err"
	

def handle(clientsocket):
  while 1:
	buf = clientsocket.recv(MAX_LENGTH)
	out = programs(buf)
	print out

    #print buf
#    if buf == '': return #client terminated connection

  
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 10000
HOST = '127.0.0.1'

serversocket.bind((HOST, PORT))
serversocket.listen(10)

while 1:
	#accept connections from outside
	(clientsocket, address) = serversocket.accept()
#	print sys.path
#	ct = Thread(target=handle, args=(clientsocket,))
#	ct = multiprocessing.Process(target=handle, args=(clientsocket,))
#	ct.start()
#	if END_PROCESS:
#		ct.terminate()
	handle(clientsocket)



