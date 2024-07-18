import os

from ..fits_file import FITS_File


class Manager:

    def __init__(self, images_folder, sub_folders=False) -> None:
        self.images_folder = images_folder
        self.sub_folders = sub_folders
        self.read_folder()
        return

    def read_folder(self) -> list:
        self.fits_files = []
        self.fits_files += [
            FITS_File(file, folder_path=self.images_folder)
            for file in os.listdir(self.images_folder)
            if ".fits" in file
        ]
        dirs = [
            name
            for name in os.listdir(self.images_folder)
            if os.path.isdir(os.path.join(self.images_folder, name))
        ]

        if dirs and self.sub_folders:
            for dir in dirs:
                self.fits_files += [
                    FITS_File(file, folder_path=os.path.join(self.images_folder, dir))
                    for file in os.listdir(os.path.join(self.images_folder, dir))
                    if ".fits" in file
                ]

        for file in self.fits_files:
            file._extractheaderinfo()

        self.fits_files.sort()

    def print_list(self) -> str:
        """print the list of files"""
        print(*self.fits_files, sep="\n")

    def __lt__(self,other):
        filtered_files = []
        for file in self.fits_files:
            if file.DATEOBS < other:
                filtered_files.append(file)
        self.fits_files = filtered_files

    def __gt__(self,other):
        filtered_files = []
        for file in self.fits_files:
            if file.DATEOBS > other:
                filtered_files.append(file)
        self.fits_files = filtered_files

    def __le__(self,other):
        filtered_files = []
        for file in self.fits_files:
            if file.DATEOBS <= other:
                filtered_files.append(file)
        self.fits_files = filtered_files

    def __ge__(self,other):
        filtered_files = []
        for file in self.fits_files:
            if file.DATEOBS >= other:
                filtered_files.append(file)
        self.fits_files = filtered_files


    def obs_type(self,obs_types):
        if isinstance(obs_types,str):
            filtered_list = []
            for file in self.fits_files:
                if file.OBSTYPE == obs_types.upper():
                    filtered_list.append(file)
            self.fits_files = filtered_list
        elif isinstance(obs_types,list):
            filtered_list = []
            for obs in obs_types:
                if isinstance(obs,str):
                    for file in self.fits_files:
                        if file.OBSTYPE == obs.upper():
                            filtered_list.append(file)
            self.fits_files = filtered_list
        else :
            raise TypeError("Input must be of type string or list(of strings)")
        