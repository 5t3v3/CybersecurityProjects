### PORT SCANNER

import sys
import pyfiglet
import socket
from datetime import datetime
import argparse

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

ap = argparse.ArgumentParser();
ap.add_argument("-t","--target",required=True,help="target ip adderss")
args = vars(ap.parse_args())

print("Scanning started at "+ str(datetime.now()))
host_name = args["target"]
host = socket.gethostbyname(host_name)
print("IP Address of "+host_name+ " is "+host)

print("Checking for open ports....\n")

try:
    for port in range(1,65535):
        s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(2)

        result = s.connect_ex((host,port))
        if result == 0:
            print ("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()

