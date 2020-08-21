import os
import random
from setup import *
from tools import head_foot, display_list, clear_screen

class ApplyVpn(object):

    def __init__(self):
        self.main_path = NORD_VPN_COUNTRIES
        self.server_path = None


    def select_vpn(self):
        clear_screen()
        head_foot('Welcome to openvpn')
        all_countries = os.listdir(self.main_path)
        country = display_list(all_countries)
        single_country_servers = f"{self.main_path}/{country}"
        list_of_vpns = os.listdir(single_country_servers)

        tcp_vpn = []
        udp_vpn = []
        vpn_server = None
        x, y = 0, 0
        for vpn in list_of_vpns:
            category = (vpn.split('.'))[-2]
            if category.startswith('tcp'):
                tcp_vpn.append((vpn, x))
                x += 1
            elif category.startswith('udp'):
                udp_vpn.append((vpn, y))
                y += 1

        if self.vpn_type() in ['tcp', 't']:
            vpn_server = self.select_server(tcp_vpn)
        else:
            vpn_server = self.select_server(udp_vpn)

        self.server_path = f"{single_country_servers}/{vpn_server}"


    def vpn_type(self):
        clear_screen()
        vpn_type = None
        condition = ['u', 'udp', 't', 'tcp']
        while True:
            vpn_type = input('Choose udp(u), tcp(t): ')
            if vpn_type.lower() in condition:
                break
            else:
                print("Your selections are: u, udp, t, tcp: ")
        return vpn_type


    def select_server(self, vpns):
        selection_by = input("Select manualy(m) | random(r): ")
        index = None
        if selection_by.lower() in ['m', 'manualy']:
            for vpn, idx in vpns:
                print(f"{idx} => {vpn}")

            while True:
                index = input('Select server (nr): ')
                if index.isnumeric() and int(index) > 0 and int(index) < len(vpns):
                    break
                else:
                    print(f"Select a number between 0 and {len(vpns) - 1}")
        elif selection_by.lower() in ['random', 'r']:
            index = random.randrange(0, len(vpns))
        else:
            return self.select_server(vpns)

        return (vpns[int(index)][0])
