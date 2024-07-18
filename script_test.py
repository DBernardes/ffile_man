import os

from ffile_man.manager import Manager

images_folder = os.path.join("FITS")
man = Manager(images_folder, sub_folders=True)
man.print_list()
