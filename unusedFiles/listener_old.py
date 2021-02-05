import os
import socket
from tracks import solidPulse
from utils import lampOff
import threading 

MAX_LENGTH = 4096
END_PROCESS = False
TRACK = ""
pross = ""

def programs(inn):
	print('~~~~~~~~~~')
	if inn == "1":
		TRACK = "tracks/solidPulse.py"
		print("1")
		thread = threading.Thread( target=solidPulse.run(1) )
		print("2")
		thread.daemon = True
		print("3")
		thread.start()
		return "on"
	if inn == "off":
		pross.kill()
#		END_PROCESS = True
#		solidPulse.controller("0")
#		stop_threads = True		
#		subprocess.call("./utils/processKiller.sh")
#		lampOff.run()
		return "off"
	if inn == "quit":
		print("exit-server")
		serversocket.close()
		sys.exit(0)
#	if TRACK != "":
	
	return"err"
	

def handle(clientsocket):
  while 1:
	buf = clientsocket.recv(MAX_LENGTH)
	out = programs(buf)
	print out

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 10000
HOST = '127.0.0.1'

serversocket.bind((HOST, PORT))
serversocket.listen(10)

while 1:
	#accept connections from outside
	(clientsocket, address) = serversocket.accept()
	handle(clientsocket)

def run (signal):
        unicorn.set_layout(unicorn.AUTO)
        unicorn.rotation(0)
        unicorn.brightness(0.6)
        width,height=unicorn.get_shape()

        g = -1
        i = 0.0
        offset = 30
        while signal:
                i = i + 0.3
                g += 1
                for y in range(height):
                        for x in range(width):
                                #original(x,y,i,offset)
                                if x == g-1 or x == g or x == g+1:
                                        wave(x,y)
                                else:
                                        spectrum(x,y)
                                if g > 7:
                                        g = -1

                unicorn.show()
                time.sleep(0.8)

