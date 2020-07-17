import os
import shutil
from setup import *


class Manage(object):

    def __init__(self, path='', start=0, end=2):
        '''Initialize working path'''
        self.path = None
        if path == '':
            self.path = NORD_VPN_COUNTRIES
        else:
            self.path = path
        self.start = start
        self.end = end

    def create_folder(self, folder):
        '''create path if it is missing, return full path'''
        t_folder = f"{self.path}/{folder}"
        if not os.path.exists(t_folder):
            os.mkdir( t_folder )
        return t_folder

    def move_file(self, file, folder):
        '''move files, takes file name and folder name'''
        t_file = os.path.join(self.path, file)
        t_folder = self.create_folder(folder)
        shutil.move(t_file, t_folder)

    def sort_files(self):
        '''Read all files from specified path'''
        files = os.fsencode(self.path)
        for f in os.listdir(files):
            file_name = os.fsdecode(f)
            if file_name.endswith('.ovpn'):
                self.move_file(file_name, file_name[self.start:self.end])


if __name__ == '__main__':
    path = input('Select path to be managed "/etc/openvpn/nordVPN" (enter default):\n')

    print("Create folder related to file name default first 2 leters.\n You can specify start index and end index(exclude), or leave blank (first 2 letters by default): \n")
    manage = None

    start = input('Start index, 0 (enter default): ')
    end = input('End index, 2 (enter default): ')
    if len(start) > 0 and len(end) > 0 and len(path) > 0 and (start.isnumeric() and end.isnumeric()):
        manage = Manage(path, int(start), int(end))
    elif len(path) > 0:
        manage = Manage(path)
    else:
        manage = Manage()

    manage.sort_files()