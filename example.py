import os
from datetime import datetime

from ffile_man.manager import Manager

# ==================== Example 1 =================
images_folder = os.path.join("FITS")
man = Manager(images_folder, sub_folders=True)
man.print_list()

# ==================== Example 2 =================
# images_folder = os.path.join("FITS")
# man = Manager(images_folder, sub_folders=True)
# man >= datetime(2024, 7, 17, 12, 11)
# man.print_list()

# ==================== Example 3 =================
# images_folder = os.path.join("FITS")
# man = Manager(images_folder, sub_folders=True)
# man.seletec_obstype("FLAT")
# man.print_list()
