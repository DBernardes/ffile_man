import os
from dataclasses import dataclass
from datetime import datetime

from astropy.io import fits


@dataclass
class FITS_File:
    """Class for keeping the FITS files"""

    name: str
    folder_path: str
    OBSTYPE: str = ""
    DATEOBS: str = ""

    def _getheaders(self) -> None:
        file_path = os.path.join(self.folder_path, self.name)
        self.header = fits.getheader(file_path)

    def _extractheaderinfo(self) -> None:
        self._getheaders()
        self.OBSTYPE = self.header["OBSTYPE"]
        self.DATEOBS = datetime.fromisoformat(self.header["DATE-OBS"])

    def __lt__(self, other):
        return self.DATEOBS < other.DATEOBS
