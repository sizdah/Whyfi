

from multiprocessing import Process
from time import sleep
import os
from randmac import RandMac
import random
import string
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--paranoid", nargs="?", default=False, help="It defines if your data goes over a VPN or not, the defualt value is False")
args = parser.parse_args()
paranoid = args.paranoid

#VARIABLES TO SET THESE SHOULD BE SET ACORDING TO YOURS
#FIND THEM USING sudo ip link show and set them here

lan = "enp2s0"
wireless = "wlp3s0"
ap = "ap0" #usually you do not how to change it
time_shift = 2 #this is the time for shifting the packets from the conected device to your hotspot to confuse ISP
def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def hotspot():
    channels = [3,4,5,8,7,9,10]#list of channel from which a channel will be used to broadcast
    random_mac = RandMac("00:00:00:00:00:00", True)
    line = "create_ap -c "+str(channels[random.randint(0, len(channels)-1 )])+" --hidden --mac "+str(random_mac)+" "+wireless+" "+lan+" "+randomString(random.randint(1,4))+" "+randomString(8)
    print(line)
    os.system(line)

def ttl_shift():
    print("Ditch out the ISP for mac address filtering ^_^...")
    os.system("iptables -w -t mangle -I PREROUTING -i "+ap+" -j TTL --ttl-inc "+str(time_shift))
    os.system("iptables -w -t mangle -I PREROUTING -i "+lan+" -j TTL --ttl-inc "+str(time_shift))
    print("Catch me if you can, I am in dude wating for your command sir")


def cleanup():
    print("Doing clean up...")
    os.system("sudo ip link set ap0 down")
    os.system("sudo iw dev ap0 del")
    for file in os.listdir("/tmp"):
        if file.endswith(".lock"):
            case = (os.path.join("/tmp", file))
            if "create_ap" in case:
                os.remove(case)
                print(case," Removed")
    print("done with clean up")


def vpn(): #Here I am using ProtonVpn in CLI mode, you already had to install it and configure it with your own account
    print("Rounting the data over VPN...")
    os.system("protonvpn c -f")
    os.system("protonvpn s")



def fun():
    os.system('figlet HOTSPOT IS COMMING') # if have to make figlet installed, else you can comment this line and uncomment the next line
    #print("Hot spot is comming");



def wifi_down():
    os.system('nmcli con down eduroam')



fun()
cleanup()
wifi_down()
p1 = Process(target=hotspot)
p2 = Process(target=ttl_shift)
p3 = Process(target=vpn)


if paranoid == True:
	p3.start()
	sleep(3)
p1.start()
print("Enabling Hotspot")
sleep(7) # So the ap being created and then after we do the time shift
p2.start()





