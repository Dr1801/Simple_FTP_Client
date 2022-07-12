###Import module
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

#Server response 
text_servermsg = tkinter.Text(window).place(x=20,y=150)

#Connect
lbl_ip = tkinter.Label(window, text="IP Address : ", fg="red", bg="black").place(x=430,y=20)
ent_ip = tkinter.Entry(window).place(x=500,y=20)
lbl_port = tkinter.Label(window, text="Port : ", fg="cyan", bg="black").place(x=430,y=60)
ent_port = tkinter.Entry(window).place(x=500,y=60)
btn_connect = tkinter.Button(window, text="Connect", command=connectServer, width=12, bg="green", fg="black").place(x=430,y=100)
btn_quit = tkinter.Button(window, text="Disconnect", command=closeConnection, width=12, bg="red", fg="black").place(x=530,y=100)

#Login
lbl_login = tkinter.Label(window, text="Username")
ent_login = tkinter.Entry(window)
lbl_pass = tkinter.Label(window, text="Password")
ent_pass = tkinter.Entry(window)
btn_login = tkinter.Button(window, text="Login", command=loginServer)

#Listing
lbl_dir = tkinter.Label(window, text="Directory listing: ", fg="black", bg="pink", width=34, height=1).place(x=700,y=143)
libox_serverdir = tkinter.Listbox(window, width=40, height=14).place(x=700,y=165)

#File & Directory
lbl_input = tkinter.Label(window, text="Input", fg="black", bg="pink", width=34, height=1).place(x=700,y=400)
ent_input = tkinter.Entry(window, width=40).place(x=700,y=420)
btn_crdir = tkinter.Button(window, text="Create Directory", command=createDirectory, width=15, bg="yellow").place(x=850,y=470)
btn_chdir = tkinter.Button(window, text="Change Directory", command=changeDirectory, width=15, bg="yellow").place(x=700,y=470)
btn_deldir = tkinter.Button(window, text="Delete Directory", command=deleteDirectory, width=15, bg="red").place(x=850,y=540)
btn_delfile = tkinter.Button(window, text="Delete File", command=deleteFile, width=15, bg="red").place(x=700,y=540)
btn_downfile = tkinter.Button(window, text="Download File", command=downloadFile, width=15, bg="cyan").place(x=700,y=505)
btn_upfile = tkinter.Button(window, text="Upload File", command=uploadFile, width=15, bg="cyan").place(x=850,y=505)

window.mainloop()
