import os
from time import strftime

import sys
try:
    droppedFile = sys.argv[1] 
except IndexError:
    print("No file dropped")

def entcmd():
    print("Enter a command")
    global cmd
    cmd=input()
    if "print" in cmd:
        printzt(cmd)
        entcmd()
    if "version" in cmd:
        ver()
        entcmd()
    if "ver" in cmd:
        ver()
        entcmd()
    if "wv" in cmd:
        winver()
        entcmd()
    if "ndir" in cmd:
        ndir(cmd)
        entcmd()
    if "tofile" in cmd:
        tofile(cmd)
        entcmd()
    if "time" in cmd:
        time()
        entcmd()
    if "help" in cmd:
        help()
        entcmd()
    if "wincmd" in cmd:
        wincmd(cmd)
        entcmd()
    if "iptvar" in cmd:
        iptvar()
        entcmd()

print("entcmd func loaded")

def printzt(cmd):
    pecstr=cmd.split("-")
    pecstr.remove("print")
    pecstr=str(pecstr)[1:-1]
    ecstr=str(pecstr)
    ecstr=ecstr.replace("'","")
    ecstr=ecstr.replace("'","")
    print(ecstr)

print("echo func loaded")

def ver():
    print("Your current version of ZTerminal is version ZTB-BN.2 v0.2")

print("ver func loaded")

def winver():
    os.system("winver")

print("winver func loaded")

def ndir(cmd):
    pndstr=cmd.split("-")
    pndstr.remove("ndir")
    pndstr=str(pndstr)[1:-1]
    pndstr=str(pndstr)
    pndstr=pndstr.replace("'", '"')
    pndstr=pndstr.replace("'", '"')
    ndstr=pndstr.replace("\\\\", "/")
    os.system("mkdir %s" % ndstr)
    print("Directory created")

print("ndir func loaded")

def tofile(cmd):
    tfstr=cmd.split("-")
    tfstr.remove("tofile")
    tfcmd="echo "+tfstr[1]+">"+tfstr[0]
    os.system(tfcmd)
    print("Printed to file")

print("tofile func loaded")

def time():
    ctime=(strftime("%H:%M:%S"))
    print("The current time is %s" % ctime)

print("time func loaded")

def help():
    hf = open("help.txt", "r")
    print(hf.read())

print("help func loaded")

def wincmd(cmd):
    pwcstr=cmd.split("-")
    pwcstr.remove("wincmd")
    pwcstr=str(pwcstr)[1:-1]
    wcstr=str(pwcstr)
    wcstr=wcstr.replace("'","")
    wcstr=wcstr.replace("'","")
    os.system(wcstr)


print("wincmd func loaded")

def iptvar():
    global ipt
    ipt=input()

print("iptvar func loaded")

def clear():
    os.system("clear")

print("clear func loaded")

def pause():
    input("Press any key to continue")

print("pause func loaded")

def exit():
    os.system("exit")

print("exit func loaded")

def ping(cmd):
    ppgstr=cmd.split("-")
    ppgstr.remove("ping")
    ppgstr=str(ppgstr)[1:-1]
    pgstr=str(ppgstr)
    pgstr=pgstr.replace("'","")
    pgstr=pgstr.replace("'","")
    os.system("ping "+pgstr)

print("ping func loaded")

def title(cmd):
    ppgstr=cmd.split("-")
    ppgstr.remove("title")
    ppgstr=str(ppgstr)[1:-1]
    pgstr=str(ppgstr)
    pgstr=pgstr.replace("'","")
    pgstr=pgstr.replace("'","")
    os.system("title "+pgstr)

print("title func loaded")


def call(cmd):
    ppgstr=cmd.split("-")
    ppgstr.remove("call")
    ppgstr=str(ppgstr)[1:-1]
    pgstr=str(ppgstr)
    pgstr=pgstr.replace("'","")
    pgstr=pgstr.replace("'","")
    os.system("zthandler.exe "+pgstr)

print("call func loaded")


def delf(cmd):
    ppgstr=cmd.split("-")
    ppgstr.remove("delf")
    ppgstr=str(ppgstr)[1:-1]
    pgstr=str(ppgstr)
    pgstr=pgstr.replace("'","")
    pgstr=pgstr.replace("'","")
    os.system("del "+pgstr)

print("delf func loaded")


def deldir(cmd):
    ppgstr=cmd.split("-")
    ppgstr.remove("deldir")
    ppgstr=str(ppgstr)[1:-1]
    pgstr=str(ppgstr)
    pgstr=pgstr.replace("'","")
    pgstr=pgstr.replace("'","")
    os.system("rd "+pgstr)

print("deldir func loaded")

def start(cmd):
    ppgstr=cmd.split("-")
    ppgstr.remove("start")
    ppgstr=str(ppgstr)[1:-1]
    pgstr=str(ppgstr)
    pgstr=pgstr.replace("'","")
    pgstr=pgstr.replace("'","")
    os.system("start "+pgstr)

print("start func loaded")

def ztcredits():
    print("ZTerminal")
    print("by Strawberry Milk Software")
    print("Commands - Lilaf")
    print(".ZT Handler - Lilaf")
    print("Community QA - Jware/Revel")
    print("Original Technology - Microsoft")
    print("and..")
    print("End-User - YOU!")
    print("Thanks for choosing ZTerminal!")

print("ztcredits func loaded")

def dir(cmd):
    ppgstr=cmd.split("-")
    ppgstr.remove("dir")
    ppgstr=str(ppgstr)[1:-1]
    pgstr=str(ppgstr)
    pgstr=pgstr.replace("'","")
    pgstr=pgstr.replace("'","")
    if pgstr=="":
        print(" Syntax error. pgstr not defined.")
    else:
        os.system("dir %s" % pgstr)

print("dir func loaded")

def tree(cmd):
    ppgstr=cmd.split("-")
    ppgstr.remove("tree")
    ppgstr=str(ppgstr)[1:-1]
    pgstr=str(ppgstr)
    pgstr=pgstr.replace("'","")
    pgstr=pgstr.replace("'","")
    if pgstr=="":
        print(" Syntax error. pgstr not defined.")
    else:
        os.system("tree %s" % pgstr)

    
print("tree func loaded")


os.system("clear")

f=open(droppedFile)
lines=f.readlines()


for line in lines:
    if "entcmd" in line:
        entcmd()
    if "print" in line:
        printzt(line)
    if "version" in line:
        ver()
    if "ver" in line:
        ver()
    if "wv" in line:
        winver()
    if "ndir" in line:
        ndir(line)
    if "tofile" in line:
        tofile(line)
    if "time" in line:
        time()
    if "help" in line:
        help()
    if "winline" in line:
        wincmd(line)
    if "iptvar" in line:
        iptvar()
    if "clear" in line:
        clear()
    if "pause" in line:
        pause()
    if "exit" in line:
        exit()
    if "ping" in line:
        ping(line)
    if "title" in line:
        title(line)
    if "call" in line:
        call(line)
    if "delf" in line:
        delf(line)
    if "deldir" in line:
        deldir(line)
    if "start" in line:
        start(line)
    if "credits" in line:
        ztcredits(line)
    if "dir" in line:
        dir(line)
    if "tree" in line:
        tree(line)
        

