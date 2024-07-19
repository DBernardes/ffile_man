import os
from dataclasses import dataclass
from datetime import datetime

from astropy.io import fits


@dataclass
class FITS_File:
    """
    Class for keeping the FITS files.

    Attributes:
        name (str): The name of the FITS file.
        folder_path (str): The path to the folder containing the FITS file.
        OBSTYPE (str): The observation type of the FITS file. Defaults to an empty string.
        DATEOBS (str): The date of the observation. Defaults to an empty string.
    """

    name: str
    folder_path: str
    OBSTYPE: str = ""
    DATEOBS: str = ""

    def _getheaders(self) -> None:
        """
        Retrieve the header information from the FITS file.
        """
        file_path = os.path.join(self.folder_path, self.name)
        self.header = fits.getheader(file_path)

    def _extractheaderinfo(self) -> None:
        """
        Extract relevant information from the FITS file header and set the OBSTYPE and DATEOBS attributes.
        """
        self._getheaders()
        self.OBSTYPE = self.header["OBSTYPE"]
        self.DATEOBS = datetime.fromisoformat(self.header["DATE-OBS"])

    def __lt__(self, other):
        """
        Compare FITS files based on the DATEOBS attribute.

        Args:
            other (FITS_File): The other FITS_File object to compare with.

        Returns:
            bool: True if the DATEOBS of the current file is less than the DATEOBS of the other file.
        """
        return self.DATEOBS < other.DATEOBS
