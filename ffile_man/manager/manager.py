import os

from ..fits_file import FITS_File


class Manager:

    def __init__(self, images_folder) -> None:
        self.images_folder = images_folder
        self._read_folder()
        return

    def _read_folder(self) -> list:
        self.fit_files = [
            FITS_File(file)
            for file in os.listdir(self.images_folder)
            if ".fits" in file
        ] #check

    def print_list(self) -> str:
        print(*self.fit_files, sep="\n")
