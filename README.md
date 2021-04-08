# KellyV
KellyV is a virus that was developed by Eric and komko.
It is made entirely in Python, using a library called: "socket".

 # Usage
 *How do you use the program?*
 Please, before using it, use it for **EDUCATIONAL PURPOSES ONLY** because this could *potentially* get you into trouble.
 
 First, you are gonna have to open the "KellyV.py" file - upon opening, no GUI is gonna be shown, that is because the connection with the user has not been established yet. To establish a connection, open up the "victim.py" file. 
 After the connection is established, the GUI appears. 
 There are few elements, the output is shown in the Text object, while we are entering commands in the Entry object.
 The button "EXECUTE" sends the command to the user.
 We also have a list of connected victims to our IP:PORT.

# Errors and bugs
First of all, the code is all messy, we get it.
But, please, don't click "EXECUTE" if there is NO COMMAND to be sent. There is a bug where it just stops the tkinter because you are sending nothing and receiving nothing, therefore making the GUI crash.
We are working to get it fixed, ASAP!
