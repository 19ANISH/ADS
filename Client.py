import socket
import threading
import tkinter as tk
from tkinter import ttk
ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233
message = ""
decisionMsg = ""
print('Waiting for connection')
try:
	ClientSocket.connect((host, port))
except socket.error as e:
    print("Unable to connect")
    print(str(e))
    exit()
print("\nconnected")
def readMessage(client):
    global message
    global decisionMsg
    global serverMsg
    global decision
	message = client.recv(1024).decode("utf-8")
    serverMsg.config(text=message)
    decisionMsg = client.recv(1024).decode("utf-8")
    decision.config(text=decisionMsg)
    print(decisionMsg)
def sendReady():
    ClientSocket.send(str.encode("ready"))
def sendAbort():
    ClientSocket.send(str.encode("abort"))
root = tk.Tk()
root.geometry("700x350")
root.title("GUI")
serverMsgLbl = tk.Label(root, text="Message from server: ")
serverMsgLbl.place(x=20, y=30)
serverMsg = tk.Label(root, text=message)
serverMsg.place(x=150, y=30)
readybtn = tk.Button(root, text="< Ready T >", bg='#3DB2FF', command=sendReady)
readybtn.place(x=40, y=150, width=75)
abortButton = tk.Button(root, text="< Abort T >", bg='#3DB2FF', command=sendAbort)
abortButton.place(x=150, y=150, width=75)
decisionlbl = tk.Label(root, text="Decision from server: ")
decisionlbl.place(x=20, y=250)
decision = tk.Label(root, text=decisionMsg)
decision.place(x=150, y=250)
connThread = threading.Thread(target=readMessage, args=(ClientSocket,))
connThread.start()
root.mainloop()
ClientSocket.close()