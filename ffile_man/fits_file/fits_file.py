from dataclasses import dataclass
import os
from astropy.io import fits
from datetime import datetime


@dataclass
class FITS_File:
    """Class for keeping the FITS files"""

    name: str
    folder_path: str
    OBSTYPE: str = ""
    DATEOBS: str = ""

    def _getheaders(self) -> None:
        file_path = os.path.join(self.folder_path,self.name)
        self.header = fits.getheader(file_path)

    def _extractheaderinfo(self) -> None:
        self._getheaders()
        self.OBSTYPE = self.header["OBSTYPE"]
        self.DATEOBS = datetime.fromisoformat(self.header["DATE-OBS"])
