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
fi
sudo mkdir /etc/openvpn/nordVPN


sudo wget https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip
sudo mv ovpn.zip /etc/openvpn/nordVPN

sudo unzip /etc/openvpn/nordVPN/ovpn.zip
sudo rm /etc/openvpn/nordVPN/ovpn.zip

sudo python3 file_manager.py

sudo python3 country_codes.py

sudo python3 run.py