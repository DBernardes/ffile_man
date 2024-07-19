import os

from ..fits_file import FITS_File

import shutil


class Manager:

    def __init__(self, images_folder, sub_folders=False) -> None:
        """
        Initialize the Manager with the specified folder containing FITS files.

        Args:
            images_folder (str): Path to the folder containing FITS files.
            sub_folders (bool, optional): Whether to include files from subfolders. Defaults to False.
        """
        self.images_folder = images_folder
        self.sub_folders = sub_folders
        self.read_folder()
        return

    def read_folder(self) -> list:
        """
        Read the specified folder and subfolders to find FITS files and extract their header information.

        Returns:
            list: A list of FITS_File objects found in the folder.
        """
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

    def seletec_obstype(self, obstype: str):
        """Select a group of files based on the observation type

        Args:
            obstype (str): observation type (ZERO, DARK, FLAT, FOCUS, or OBJECT).
        """
        self.fits_files = [file for file in self.fits_files if file.OBSTYPE == obstype]

    def print_list(self) -> str:
        """
        Print the list of FITS files.

        Returns:
            str: Formatted string of FITS files.
        """
        print(*self.fits_files, sep="\n")

    def __lt__(self, other):
        """
        Filter the FITS files to include only those with DATEOBS less than the given date.

        Args:
            other (str): Date to compare with.
        """
        filtered_files = []
        for file in self.fits_files:
            if file.DATEOBS < other:
                filtered_files.append(file)
        self.fits_files = filtered_files

    def __gt__(self, other):
        """
        Filter the FITS files to include only those with DATEOBS greater than the given date.

        Args:
            other (str): Date to compare with.
        """
        filtered_files = []
        for file in self.fits_files:
            if file.DATEOBS > other:
                filtered_files.append(file)
        self.fits_files = filtered_files

    def __le__(self, other):
        """
        Filter the FITS files to include only those with DATEOBS less than or equal to the given date.

        Args:
            other (str): Date to compare with.
        """
        filtered_files = []
        for file in self.fits_files:
            if file.DATEOBS <= other:
                filtered_files.append(file)
        self.fits_files = filtered_files

    def __ge__(self, other):
        """
        Filter the FITS files to include only those with DATEOBS greater than or equal to the given date.

        Args:
            other (str): Date to compare with.
        """
        filtered_files = []
        for file in self.fits_files:
            if file.DATEOBS >= other:
                filtered_files.append(file)
        self.fits_files = filtered_files

    def obs_type(self, obs_types):
        """
        Filter the FITS files based on the observation type(s).

        Args:
            obs_types (str or list): Observation type(s) to filter by. Can be a string or a list of strings.

        Raises:
            TypeError: If obs_types is not a string or a list of strings.
        """
        if isinstance(obs_types, str):
            filtered_list = []
            for file in self.fits_files:
                if file.OBSTYPE == obs_types.upper():
                    filtered_list.append(file)
            self.fits_files = filtered_list
        elif isinstance(obs_types, list):
            filtered_list = []
            for obs in obs_types:
                if isinstance(obs, str):
                    for file in self.fits_files:
                        if file.OBSTYPE == obs.upper():
                            filtered_list.append(file)
            self.fits_files = filtered_list
        else:
            raise TypeError("Input must be of type string or list(of strings)")

    def export_to(self,destination_folder,move=False):
        """
        Export FITS files to a specified destination folder.

        Args:
            destination_folder (str): The path to the folder where the FITS files will be exported.
            move (bool, optional): If True, move the files instead of copying them. Defaults to False.
        """
        for file in self.fits_files:
            if move:
                shutil.move(os.path.join(file.folder_path,file.name),os.path.join(destination_folder))
            else:
                shutil.copy(os.path.join(file.folder_path,file.name),os.path.join(destination_folder))
