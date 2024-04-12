import os
import shutil
from pathlib import Path
from threading import Thread
import logging

EXT = [
    '.jpg','.png','.zip','.doc','.py'
]


def add_file_to_folder(folder,filename,dest:Path):
    pass

def add_to_filegroup(folder, file, extension):
    logging.debug('Replace file "{folder}/{file}" ')
    dest = Path(extension)
    dest.mkdir(exist_ok=True, parents=True)
    shutil.move(os.path.join(folder,file), os.path.join(dest,file))
    logging.debug('Succsseful file relpacement:" {folder}/{file}"')





WORKDIR = os.getcwd()


def is_dir(path):
    return os.path.isdir(path)

def sort_files_by_extensions(folder:Path):
    logging.debug(f"Start sorting {folder}")
    files=os.listdir(folder)
    for file in files:
        if is_dir(os.path.join(WORKDIR,file)):
            ''' Start recursive '''
            next_folder=os.path.join(folder,file)
            t=Thread(target=sort_files_by_extensions, args=(next_folder,))
            t.start()
            logging.debug(f'Start new thread for sorting folder {file}')
        else:
            _, file_extension = os.path.splitext(file)
            for extensions in EXT:
                if file_extension in extensions:
                    add_to_filegroup(folder,file,file_extension)


def check_dir(folder):
    list_dirs=os.listdir(folder)
    for dir in list_dirs:
        if is_dir(os.path.join(WORKDIR,dir)):
           if len(os.listdir(os.path.join(WORKDIR,dir)))==0:
               os.rmdir(os.path.join(WORKDIR,dir))
               

 


if __name__=="__main__":
    directory = os.getcwd()
    sort_files_by_extensions(WORKDIR)
    check_dir(WORKDIR)
    