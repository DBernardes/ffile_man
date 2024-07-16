import os

from ffile_man.manager import Manager

images_folder = os.path.join("FITS")
man = Manager(images_folder)
man.print_list()
