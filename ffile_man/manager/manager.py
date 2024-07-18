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
