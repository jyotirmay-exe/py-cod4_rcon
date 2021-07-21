import socket
import sys
import time

sock = None
socket.setdefaulttimeout(5)
try:
    class RCON:
        def __init__(self,ip:str,port:int,rcon:str): #type hinting
            self.ip = ip
            self.port = port
            self.rcon = rcon
            global sock
            sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #IPv4/UDP connection to the server
            sock.connect((self.ip,self.port))
        
        def send(self,cmd):
            global sock
            msg = f"\xFF\xFF\xFF\xFFrcon {self.rcon} {cmd}"
            byte = bytes(msg.encode("ISO-8859-1"))
            sock.send(byte)
            res = sock.recv(1024).decode("ISO-8859-2")
            print(res[10::])

except socket.gaierror:
    print("ERROR : Host not found!")
    time.sleep(2)
    sys.exit()
except ConnectionResetError:
    print("ERROR : Check host and port combination!")
    time.sleep(2)
    sys.exit()