# Whyfi
a simple script to auto-config create_ap so you can create a hotspot on Linux, also bypass mac address filtering and stay anonymous

First, you should install create_ap script from the given Github link or if you are using arch Linux use "sudo pacman -S create_ap"

create_ap link:
https://github.com/oblique/create_ap

This script uses IPTABLES which you should install on your machine if you already dont have. ( sudo apt install iptables )

This script also requires RandMac library which you should install using pip install randmac

every time this script uses a random MAC and also a random name and a random channel and random password and establish a hidden hotspot and then show the output on terminal something like:

create_ap -c 10 --hidden --mac '52:34:95:14:7d:8a' wlp3s0 enp2s0 uy fxjqygyx

here the "uy" is the name of the hidden wifi and "fxjqygyx" is the password (every time it changes)


at the beginning of the script, there are some variable you should choose according to your hardware 
they are the names of ethernet and wireless device which you can see with the command "sudo ip link show"

This script also changes the TTL of packets of devices connected to your laptop, so ISP can not detect them and block them
