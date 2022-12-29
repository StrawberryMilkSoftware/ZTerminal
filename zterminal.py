import os
print("os imported")
os.system("title Loading...")
import chocoedit
print("chocoedit imported")
from time import strftime
print("strftime imported")
winuser=os.getlogin()
print("username retrieved")
ztver="ZTerminal v1.0.1"
print("ztver defined")
def entcmd():
    global cmd
    cmd=input(ztver+" "+winuser+" > ")
    if "printcd" in cmd:
        printcd()
        entcmd()
    elif "print" in cmd:
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
    if "oscmd" in cmd:
        wincmd(cmd)
        entcmd()
    if "clear" in cmd:
        clear()
        entcmd()
    if "pause" in cmd:
        pause()
        entcmd()
    if "exit" in cmd:
        exit()
    if "ping" in cmd:
        ping(cmd)
        entcmd()
    if "title" in cmd:
        title(cmd)
        entcmd()
    if "delf" in cmd:
        delf(cmd)
        entcmd()
    if "deldir" in cmd:
        deldir(cmd)
        entcmd()
    if "start" in cmd:
        start(cmd)
        entcmd()
    if "credits" in cmd:
        ztcredits()
        entcmd()
    if "choco" in cmd:
        choco(cmd)
        entcmd()
    if "dir" in cmd:
        dir(cmd)
        entcmd()
    if "tree" in cmd:
        tree(cmd)
        entcmd()
    if "cd" in cmd:
        cd(cmd)
        entcmd()
    else:
        print(' %s is not a valid command. Use "help" for a list of all commands.' % cmd)
        entcmd()
print("entcmd func loaded")

def printzt(cmd):
    pecstr=cmd.split("-")
    pecstr.remove("print")
    pecstr=str(pecstr)[1:-1]
    ecstr=str(pecstr)
    ecstr=ecstr.replace("'","")
    ecstr=ecstr.replace("'","")
    if ecstr=="":
        print(" Syntax error. ecstr not defined.")
    else:
        print(" "+ecstr)

print("echo func loaded")

def ver():
    print(" Your current version of ZTerminal is %s" % ztver)

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
    if ndstr=="":
        print(" Syntax error. ndstr not defined")
    else:
        os.system("mkdir %s" % ndstr)
        print("Directory created")

print("ndir func loaded")

def tofile(cmd):
    tfstr=cmd.split("-")
    tfstr.remove("tofile")
    tfcmd="echo "+tfstr[1]+">"+tfstr[0]
    if tfcmd=="":
        print(" Syntax error. tfcmd not defined.")
    else:
        os.system(tfcmd)
        print("Printed to file")

print("tofile func loaded")

def time():
    ctime=(strftime("%H:%M:%S"))
    print("The current time is %s" % ctime)

print("time func loaded")

def help():
    hf = open("help.md", "r")
    print(hf.read())

print("help func loaded")

def wincmd(cmd):
    pwcstr=cmd.split("-")
    pwcstr.remove("oscmd")
    pwcstr=str(pwcstr)[1:-1]
    wcstr=str(pwcstr)
    wcstr=wcstr.replace("'","")
    wcstr=wcstr.replace("'","")
    if wcstr=="":
        print(" Syntax error. wcstr not defined.")
    else:
        os.system(wcstr)

print("wincmd func loaded")

def clear():
    os.system("cls")

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
    if pgstr=="":
        print(" Syntax error. pgstr not defined.")
    else:
        os.system("ping "+pgstr)

print("ping func loaded")

def title(cmd):
    ppgstr=cmd.split("-")
    ppgstr.remove("title")
    ppgstr=str(ppgstr)[1:-1]
    pgstr=str(ppgstr)
    pgstr=pgstr.replace("'","")
    pgstr=pgstr.replace("'","")
    if pgstr=="":
        print(" Syntax error. pgstr not defined.")
    else:
        os.system("title "+pgstr)

print("title func loaded")



print("call func loaded")


def delf(cmd):
    ppgstr=cmd.split("-")
    ppgstr.remove("delf")
    ppgstr=str(ppgstr)[1:-1]
    pgstr=str(ppgstr)
    pgstr=pgstr.replace("'","")
    pgstr=pgstr.replace("'","")
    if pgstr=="":
        print(" Syntax error. pgstr not defined.")
    else:
        os.system("del "+pgstr)

print("delf func loaded")


def deldir(cmd):
    ppgstr=cmd.split("-")
    ppgstr.remove("deldir")
    ppgstr=str(ppgstr)[1:-1]
    pgstr=str(ppgstr)
    pgstr=pgstr.replace("'","")
    pgstr=pgstr.replace("'","")
    if pgstr=="":
        print(" Syntax error. pgstr not defined.")
    else:
        os.system("rd "+pgstr)

print("deldir func loaded")

def start(cmd):
    ppgstr=cmd.split("-")
    ppgstr.remove("start")
    ppgstr=str(ppgstr)[1:-1]
    pgstr=str(ppgstr)
    pgstr=pgstr.replace("'","")
    pgstr=pgstr.replace("'","")
    if pgstr=="":
        print(" Syntax error. pgstr not defined.")
    else:
        os.system("start "+pgstr)

print("start func loaded")

def choco(cmd):
    ppgstr=cmd.split("-")
    ppgstr.remove("choco")
    ppgstr=str(ppgstr)[1:-1]
    pgstr=str(ppgstr)
    pgstr=pgstr.replace("'","")
    pgstr=pgstr.replace("'","")
    if pgstr=="":
        print(" Syntax error. pgstr not defined.")
    else:
        chocoedit.main(pgstr)
    
print("choco func loaded")



def ztcredits():
    print("ZTerminal")
    print("by Strawberry Milk Software")
    print("Commands - Lilaf")
    print(".ZT Handler - Lilaf")
    print("QA - Jware/Revel")
    print("ChocoEdit - Choco Software (now owned by SMSoftware)")
    print("Original Technology - Microsoft")
    print("Open-source hosting - GitHub")
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

def cd(cmd):
    ppgstr=cmd.split("-")
    ppgstr.remove("cd")
    ppgstr=str(ppgstr)[1:-1]
    pgstr=str(ppgstr)
    pgstr=pgstr.replace("'","")
    pgstr=pgstr.replace("'","")
    if pgstr=="":
        print(" Syntax error. pgstr not defined.")
    else:
        try:
            os.chdir(pgstr)
        except:
            print("Directory not found")

def printcd():
    print(os.getcwd())


    
print("tree func loaded")


os.system("title ZTerminal")
print("Changed window title to ZTerminal")
os.system("cls")


#main
print("ZTerminal - Copyright (c) 2022 Strawberry Milk Software")
print(ztver)
entcmd()

