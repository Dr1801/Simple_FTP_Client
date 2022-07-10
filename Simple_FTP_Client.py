import tkinter
from tkinter import BOTH, END, LEFT
import ftplib
ftp = ftplib.FTP()

####Manipulating server
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
        
def closeConnection():
    try:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Closing connection...")
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,ftp.quit())
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to disconnect")
        
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
    libox_serverdir.insert(0,"####################################################")
    dirlist = []
    dirlist = ftp.nlst()
    for item in dirlist:
        libox_serverdir.insert(0, item)
        

###FTP commands

#Manipulating files
def deleteFile():
    file = ent_input.get()
    try:
        msg = ftp.delete(file)
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,msg)
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to delete file")
    displayDir()
       
def downloadFile():
    file = ent_input.get()
    down = open(file, "wb")
    try:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Downloading " + file + "...")
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,ftp.retrbinary("RETR " + file, down.write))
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to download file")
    displayDir()
       
def uploadFile():
    file = ent_input.get()
    try:
        up = open(file, "rb")
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Uploading " + file + "...")
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,ftp.storbinary("STOR " + file,up))
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to upload file")
    displayDir()   


#Directory manipulation    
def createDirectory():
    directory = ent_input.get()
    try:
        msg = ftp.mkd(directory)
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,msg)
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to create directory")
    displayDir()
       
def deleteDirectory():
    directory = ent_input.get()
    try:
        msg = ftp.rmd(directory)
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,msg)
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to delete directory")
    displayDir()
    
def changeDirectory():
    directory = ent_input.get()
    try:
        msg = ftp.cwd(directory)
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,msg)
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to change directory")
    displayDir()

    
###Display

#Create window
window = tkinter.Tk()
window.title("FTP Client")
window.wm_iconbitmap("icon.ico")
window.geometry("1000x600")
window.resizable(0,0)
window.configure(bg="black")
