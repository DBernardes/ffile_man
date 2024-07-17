import os

from ..fits_file import FITS_File


class Manager:

    def __init__(self, images_folder) -> None:
        self.images_folder = images_folder
        self._read_folder()
        return

    def _read_folder(self) -> list:
        self.fits_files = [
            FITS_File(file, folder_path=self.images_folder)
            for file in os.listdir(self.images_folder)
            if ".fits" in file
        ]
        for file in self.fits_files:
            file._extractheaderinfo()

        self.fits_files.sort()

    def print_list(self) -> str:
        print(*self.fits_files, sep="\n")
