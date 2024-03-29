import socket
import sys
import time
from datetime import datetime
from socket import gaierror, timeout

sock = None
socket.setdefaulttimeout(5)
class RCON:
    def __init__(self,ip:str,port:int,rcon:str): #type hinting
        self.ip = ip
        self.port = port
        self.rcon = rcon
        global sock
        try:
            sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #IPv4/UDP connection to the server
            sock.connect((self.ip,self.port))
            import logger
            logger.log(f"Connected to RCON @ {ip}:{port}")
            msg = f"\xFF\xFF\xFF\xFFrcon {self.rcon} status"
            byte = bytes(msg.encode("ISO-8859-1"))
            sock.send(byte)
            if sock.recv(20480).decode("ISO-8859-2")[10::]=="Bad rcon":
                print("Invalid rcon password!")
        #exceptions handling
        except gaierror:
            print("ERROR : Host not found!")
            time.sleep(2)
            sys.exit()
        except ConnectionResetError:
            print("ERROR : Check host and port combination!")
            time.sleep(2)
            sys.exit()
        except socket.timeout:
            print("Server Connection timed out!")
            time.sleep(2)
            sys.exit()
    def send(self,cmd):
        global sock
        msg = f"\xFF\xFF\xFF\xFFrcon {self.rcon} {cmd}"
        import logger
        logger.log(f"{datetime.now().strftime('%d/%m/%y %H:%M:%S')} >> Sent : {cmd}")
        byte = bytes(msg.encode("ISO-8859-1"))
        sock.send(byte)
        while True:
            try:
                res = sock.recv(20480).decode("ISO-8859-2")
            except:
                break
            logger.log(f"{datetime.now().strftime('%d/%m/%y %H:%M:%S')} >> Received : \n{res[10::]}\n")
            print(res[10::])