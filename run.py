import os
import math
import apply_vpn
from tools import head_foot, stop_vpn, clear_screen
import getpass
from setup import *


class Run(object):
    
    def __init__(self):
        self.vpn = apply_vpn.ApplyVpn()
        self.vpn.select_vpn()
        self.full_path = self.vpn.server_path

    
    def linux_commands(self):
        clear_screen()
        user_name = input("VPN User name: ")
        password = getpass.getpass("VPN Password:")
        self.create_sh(user_name, password)

        start_vpn = f'''
            sudo chmod +x ./vpn_changer.sh
            sudo ./vpn_changer.sh
        '''
        os.system(start_vpn)

        remove_files = f'''
            sudo service NetworkManager stop
            sudo service NetworkManager start
            clear

            echo "Connecting ...."
            sleep 5
            clear
            sudo rm '{NORD_VPN_COUNTRIES}/credentials'
            sudo rm 'vpn_changer.sh'
            echo "-> connected to [ {self.full_path.split('/')[-1]} ]"
            echo "-> test your location: [ https://tools.keycdn.com/geo ]"
        '''
        os.system(remove_files)



    def create_sh(self, user_name, password):
        # https://hide.me/en/vpnsetup/ubuntu/openvpn-command-line/
        commands = f'''
        #!/bin/bash

        sudo touch '{NORD_VPN_COUNTRIES}/credentials'
        sudo printf '%s\n' '{user_name}' '{password}' > '{NORD_VPN_COUNTRIES}/credentials'
        # >>> if NORD_VPN_COUNTRIES path is modified modify  "\/etc\/openvpn\/nordVPN\/credentials" too
        sudo sed -i 's/auth-user-pass/auth-user-pass \/etc\/openvpn\/nordVPN\/credentials/g' '{self.full_path}'
        sudo nohup openvpn --config '{self.full_path}' &
        '''
        with open('./vpn_changer.sh', 'w+') as vpn_bash:
            vpn_bash.write(commands)
    
    
    @staticmethod
    def start_vpn():
        os.system('clear')
        greet_text = 'after using vpn and not stoping sevice may cause internet connection problem'
        head_foot(greet_text, '*')
        start = input('kill(k) | start(s) vpn: ')
        stop_vpn()

        if start.lower() in ['s', 'start']:
            return True
        return False



if __name__ == "__main__":
    if Run.start_vpn():
        run = Run()
        # stop_vpn()
        run.linux_commands()