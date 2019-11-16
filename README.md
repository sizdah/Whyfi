# Whyfi
a simple script to autoconfig create_ap so you can create hotspot on linux, also by pass mac address filtering and stay anonymous

First you should install create_ap script from here or in arch linux simply use "sudo pacman -S create_ap"
https://github.com/oblique/create_ap

This script also require RandMac library which you should install using pip install randmac

everytime this script uses a random MAC and also a random name and a random channel and random password and establish a hidden hotspot

in the beginning of the script there are some variable you should choose according to your hardware 
they are name of ethernet and wireless you can see with the command sudo ip link show
