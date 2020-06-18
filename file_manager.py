import os
import shutil

class Manage(object):

    def __init__(self, path, start=0, end=2):
        '''Initialize working path'''
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
        '''move files'''
        t_file = f"{self.path}/{file}"
        t_folder = self.create_folder(folder)
        shutil.move(t_file, t_folder)

    def sort_files(self):
        '''Read all files from specified path'''
        with os.scandir(self.path) as files:
            for f in files:
                if not f.name.startswith('.') and f.is_file():
                    self.move_file(f.name, f.name[start:end])


if __name__ == '__main__':
    path = input('Select path to be managed:\n')

    start, end = [(int(n), int(m)) for n, m in (input('Create folder name from start and end(exclude), (first 2 letters by default) index by space: \n').split(' '))]
    
    manage = Manage(path, start, end)
    manage.sort_files()