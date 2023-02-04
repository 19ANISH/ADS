import socket
import os
import threading
import tkinter as tk
from tkinter import ttk
clients = []
ThreadCount = 0
messages = []
def acceptConnections():
    global ThreadCount
    while ThreadCount < 4:
        Client, address = ServerSocket.accept()
        clients.append(Client)
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        ThreadCount += 1
        newThread = threading.Thread(target=threaded_client, args=(Client, ThreadCount))
        newThread.start()
        print('Thread Number: ' + str(ThreadCount))
        connected.config(text="connected clients = " + str(ThreadCount))
def broadcastPrepare():
    print(clients)
    for i in clients:
        i.sendall(str.encode("< Prepare T >"))

ServerSocket = socket.socket()
host = ''
port = 1233
clients = []
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)

def broadcast(message):
    for i in clients:
        i.send(message.encode())

def threaded_client(connection, number):
    while True:
        data = connection.recv(2048)
        if data.decode("utf-8") == "ready":
            tree.insert("", "end", values=["site " + str(number), "< Ready T >"])
            messages.append("ready")
            break
        if data.decode("utf-8") == "abort":
            tree.insert("", "end", values=["site " + str(number), "< Abort T >"])
            messages.append("abort")
            break
    while ThreadCount != len(messages):
        pass
    if "abort" in messages:
        connection.send(str.encode("< Abort T >"))
        decision.config(text="< Abort T >")
        action.config(text="Abort the transaction")
    else:
        connection.send(str.encode("< Commit T >"))
        decision.config(text="< Commit T >")
        action.config(text="Commit the transaction")
    connection.close()

root = tk.Tk()
root.geometry("700x350")
root.title("Server")
preparetbtn = tk.Button(root, text="<Prepare T>",
bg='#3DB2FF', command=broadcastPrepare)
preparetbtn.place(x=20, y=50, width=75)
tree = ttk.Treeview(root, show='headings', height=5)
tree.place(x=20, y=90)
verscrlbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
style = ttk.Style(root)
style.configure('Treeview', rowheight=20)
verscrlbar.pack(side='right', fill='x')
fields = ["Site", "Response"]
tree["columns"] = fields
for i in fields:
    tree.heading(i, text=i)
decisionlbl = tk.Label(root, text="Decision -")
decisionlbl.place(x=20, y=250)
decision = tk.Label(root, text="")
decision.place(x=100, y=250)
actionlbl = tk.Label(root, text="Action -")
actionlbl.place(x=20, y=300)
action = tk.Label(root, text="")
action.place(x=100, y=300)
connected = tk.Label(root, text="connected clients = 0")
connected.place(x=500, y=0)
connThread = threading.Thread(target=acceptConnections)
connThread.start()
root.mainloop()
ServerSocket.close()