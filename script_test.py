import os
from datetime import datetime
from ffile_man.manager import Manager

images_folder = os.path.join("FITS")
man = Manager(images_folder,sub_folders=True)
man>= datetime(2024,7,17,12,11)
man.print_list()
