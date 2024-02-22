#https://youtu.be/ef0gYGs98W0
from pystyle import *


print(Box.Lines("[+]learn python with michel[+]"))
Write.Print("[+] this program for login page \n",Colors.purple_to_red,interval=0.1)
Write.Print("[+] write username and password\n\n",Colors.purple_to_red,interval=0.1)
print(Box.DoubleCube("Example[1]"))
while True:
    username = Write.Input("Write username: ", Colors.blue_to_green, interval=0.1)
    password = Write.Input("Write password: ", Colors.blue_to_green, interval=0.1)
    if username == "michel" and password == "123456":
        Write.Print("[+] welcome admin\n ",Colors. green, interval=0.1)
        input('\n press any key to exit ...')
    else:
        Write.Print("[+] Error Try again\n\n ",Colors.red, interval=0.1)


