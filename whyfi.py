#!/usr/bin/env python
# coding: utf-8



from multiprocessing import Process
from time import sleep
import os
from randmac import RandMac
import random
import string


#VARIABLES TO SET THESE SHOULD BE SET ACORDING TO YOURS
#FIND THEM USING sudo ip link show and set them here

lan = "enp2s0"
wireless = "wlp3s0"
ap = "ap0" #usually you do not how to change it


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def hotspot():
    channels = [3,4,5,8,7,9,10,12,13]#list of channel from which a channel will be used to broadcast
    random_mac = RandMac("00:00:00:00:00:00", True)
    line = "create_ap -c "+str(channels[random.randint(0, len(channels)-1 )])+" --hidden --mac "+str(random_mac)+" "+wireless+" "+lan+" "+"+randomString(random.randint(1,4))+" "+randomString(8)
    print(line)
    os.system(line)

def ttl_shift():
    print("Ditch out the ISP for mac address filtering ^_^...")
    os.system("iptables -w -t mangle -I PREROUTING -i "+ap+" -j TTL --ttl-inc 2")
    os.system("iptables -w -t mangle -I PREROUTING -i "+lan+" -j TTL --ttl-inc 2")
    print("Now you can connect! , press Ctrl+C to disconnect")


def cleanup():
    print("Doing clean up...")
    for file in os.listdir("/tmp"):
        if file.endswith(".lock"):
            case = (os.path.join("/tmp", file))
            if "create_ap" in case:
                os.remove(case)
                print(case," Removed")
    print("done with clean up")




print("HOTSPOT IS STARTING")
p1 = Process(target=hotspot)
p2 = Process(target=ttl_shift)

cleanup()
p1.start()
print("Enabling Hotspot")
sleep(7)
p2.start()
