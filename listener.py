import unicornhat as unicorn
import math
import threading
import time
import socket
from tracks import solidPulse
from utils import lampOff
import threading 

class UnicornDaemon(object):

	def __init__(self, track):
		self.__track == track
		thread = threading.Thread(target=self.execute, args=())
		thread.daemon = True                            # Daemonize thread
		thread.start()                                  # Start the execution
		print("Daemon init")

	def execute(self):
		while True:
			if self.__track == "solidPulse":
				solidPulse.run(1)
				

def programs(inn):
	print('~~~~~~~~~~')
	if inn == "1":
		uDaemon = UnicornDaemon("solidPulse")
		return "solidPulse selected"
	if inn == "off":
		return "off"
	if inn == "quit":
		print("exit-server")
		serversocket.close()
		sys.exit(0)
	return "err"

def handle(clientsocket):
	while 1:
		buf = clientsocket.recv(MAX_LENGTH)
		out = programs(buf)
		print out

###############################################
###############################################

PORT = 10000
HOST = '127.0.0.1'
MAX_LENGTH = 4096

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((HOST, PORT))
serversocket.listen(10)

###############################################
###############################################

while 1:
	#accept connections from outside
	(clientsocket, address) = serversocket.accept()
	handle(clientsocket)
	