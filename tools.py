import os
import math
from setup import *


class Global_vars(object):
    
    def __init__(self, list_index, list_offset):
        self.list_index = list_index
        self.list_offset = list_offset
        self.slices = 0


def get_screen_size():
    '''find terminal width and height'''
    terminal_width, terminal_height = os.get_terminal_size()
    return terminal_width, terminal_height


def head_foot(greet_text='', delimite='='):
    '''create a greet message @text message @delimiter'''
    terminal_width, terminal_height = get_screen_size()
    left_right_space = ' ' * math.floor(((terminal_width - len(greet_text))/2))
    if len(greet_text) > 0:
        print(delimite * terminal_width)
        print(greet_text.center(terminal_width))
        print(delimite * terminal_width)
    else:
        print(delimite * terminal_width)


def stop_vpn():
    '''Kill all open vpns procesess and reset wireless'''
    stop_instructions = '''
        sudo killall openvpn;
        sudo rm ./nohup.out;
        sudo service NetworkManager restart
    '''
    os.system(stop_instructions)


def clear_screen():
    os.system('clear')


def display_list(iter_elem):
    '''display all countryes in the folder'''
    # set global variables
    g_vars = Global_vars(LIST_INDEX, LIST_OFFSET)
    slices = get_slices(len(iter_elem), g_vars)
    g_vars.slices = slices

    country_nr = None
    if len(iter_elem) > 50:
        list_all = input(f'{len(iter_elem)} records will be displayed, are you sure(yes, no): \n')

        if list_all.lower() in ['y', 'yes']:
            for idx, f in enumerate(iter_elem):
                print(f"{idx} -> {f}")
            country_id = input('nr => country: ')
            if country_id.isnumeric() and int(country_id) < len(iter_elem) and int(country_id) > 0:
                country_nr = int(country_id)
            else:
                clear_screen()
                display_list()
        else:
            while True:
                print_slice(iter_elem, g_vars)
                direction = input('f => previous | j => next | nr => country: ')
                if direction.lower() == 'j':
                    country_slice('next', g_vars)
                    print_slice(iter_elem, g_vars)
                elif direction.lower() == 'f':
                    country_slice('previous', g_vars)
                    print_slice(iter_elem, g_vars)
                elif direction.isnumeric():
                    country_nr = int(direction)
                    if country_nr < len(iter_elem) and country_nr >=0 :
                        break
                    else:
                        print(f"Number must be between 0 and {len(iter_elem) - 1}")
    
    return f"{iter_elem[country_nr]}"


def country_slice(direction, g_vars):
    if direction == 'next' and g_vars.list_index < g_vars.slices:
        g_vars.list_index += 1
    if direction == 'previous' and g_vars.list_index > 0:
        g_vars.list_index -= 1


def print_slice(iter_elem, g_vars):
    clear_screen()
    head_foot()

    start = g_vars.list_offset * g_vars.list_index
    end = (start + g_vars.list_offset) if (start + g_vars.list_offset <= len(iter_elem)) else len(iter_elem)
    display_arr = [(idx, file) for idx, file in enumerate(iter_elem)]
    for idx, f in display_arr[start:end]:
        print(f"{idx} -> {f}")


def get_slices(nr_elems, g_vars):
    return (math.floor(nr_elems/(g_vars.list_offset)))