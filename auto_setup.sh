#!/bin/bash

clear
echo " -> To atomate setup process options are: "
echo " o -> if you need to install OpenVPN else leave blank"
echo " "

read -p "Enter options: " options

if [[ "$options" == *"o"* ]]
then
    echo " "
    echo "-> updating system"
    sudo apt-get update
    
    echo " "
    echo "-> installing openvpn"
    sudo apt-get install openvpn -y
    sudo apt-get update
fi
echo " "
echo "-> creating nordVPN folder"
sudo mkdir /etc/openvpn/nordVPN


sudo wget https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip
sync

sudo unzip ovpn.zip -d /etc/openvpn/nordVPN/
sync

sudo rm -rf ovpn.zip
sync

clear
echo "Do not close or terminate terminal"
printf '%s\0' /etc/openvpn/nordVPN/ovpn_tcp/* | sudo xargs -0 mv -t /etc/openvpn/nordVPN/
printf '%s\0' /etc/openvpn/nordVPN/ovpn_udp/* | sudo xargs -0 mv -t /etc/openvpn/nordVPN/
sync

sudo rm -rf /etc/openvpn/nordVPN/ovpn_tcp
sudo rm -rf /etc/openvpn/nordVPN/ovpn_udp
sync

sudo python3 file_manager.py
sync 

sudo python3 country_codes.py
sync

sudo python3 run.py
sync