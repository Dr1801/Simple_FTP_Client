import tkinter
from tkinter import BOTH, END, LEFT
import ftplib

ftp = ftplib.FTP()


#Server commands
def connectServer():
    ip = ent_ip.get()
    port = int(ent_port.get())
    try:
        msg = ftp.connect(ip,port)
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,msg)
        lbl_login.place(x=150,y=20)
        ent_login.place(x=150,y=40)
        lbl_pass.place(x=150,y=60)
        ent_pass.place(x=150,y=80)
        btn_login.place(x=182,y=110)
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to connect")
        
def loginServer():
    user = ent_login.get()
    password = ent_pass.get()
    try:
        msg = ftp.login(user,password)
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,msg)
        displayDir()
        lbl_login.place_forget()
        ent_login.place_forget()
        lbl_pass.place_forget()
        ent_pass.place_forget()
        btn_login.place_forget()
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to login")
        
def displayDir():
    libox_serverdir.insert(0,"----------------------------------------------------")
    dirlist = []
    dirlist = ftp.nlst()
    for item in dirlist:
        libox_serverdir.insert(0, item)
        

#FTP commands        
        
