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

# Change the IP of the server
There are multiple ways of making people connect to your server.
For testing purposes, changing "my_ip" to "localhost" works perfectly. But there are limits when it comes to connecting with someone outside of your network.
You could use Radmin VPN or Hamachi to establish a connection between 2 users and you could use the IP found there.
The best way to make this would be to port-forward your own router so that anyone could connect to your IP from *anywhere* in the world. 
While testing we've used both Radmin VPN and Hamachi, and both have worked without any errors. We were able to run the virus from Sweden to Croatia and back which is 1982km (3964km in total).

# Errors and bugs
First of all, the code is all messy, we get it.
But, please, don't click "EXECUTE" if there is NO COMMAND to be sent. There is a bug where it just stops the tkinter because you are sending nothing and receiving nothing, therefore making the GUI crash.
We are working to get it fixed, ASAP!
