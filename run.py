import rcon
import pickle
import stdiomask
import json
import sys
import time
import socket
from socket import gaierror
foundData = -1

try:
    with open(".\data\svr.dat","rb") as f:
        pickle.load(f)
    foundData = 1
except EOFError as ex:
    foundData = 0

loadData = 'n'

if foundData == 1:
    loadData = input("Load server connection from previous session? (y/n) : ").lower()
elif foundData == 0:
    ip = input("Enter IP : ")
    port = int(input("Enter Port : "))
    pswd = stdiomask.getpass(prompt = "Enter RCON Password : ", mask = '*')

    conn = rcon.RCON(ip,port,pswd)

if loadData == 'y':
    with open('.\data\svr.dat','rb') as f:
        conn = pickle.load(f)
    with open('.\data\serverparams.json','r') as f:
        params = json.load(f)
        print(params)
        conn.__init__(params["ip"],params["port"],params["rcon"])

if loadData == 'n' and foundData != 0:
    ip = input("Enter IP : ")
    port = int(input("Enter Port : "))
    pswd = stdiomask.getpass(prompt = "Enter RCON Password : ", mask = '*')

    conn = rcon.RCON(ip,port,pswd)

with open(".\data\svr.dat","wb") as f:
    pickle.dump(conn,f)

if loadData == 'n':
    with open(".\data\serverparams.json","w") as f:
        params = {"ip":ip,"port":port,"rcon":pswd}
        json.dump(params,f,indent=4)

while True:
    cmd = input(r"\rcon ")
    conn.send(cmd)
