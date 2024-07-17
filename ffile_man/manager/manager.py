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

        self.fits_files.sort()

    def print_list(self) -> str:
        """
        print_list

        Prints the list of fits files in the directory in order of oberserved date
        """
        print(*self.fits_files, sep="\n")
