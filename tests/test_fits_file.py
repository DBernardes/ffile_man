from ffile_man.fits_file import FITS_File
from datetime import datetime

def test_fits_works():
    f = FITS_File("20240716_s4c1_000001.fits","FITS")
    f._extractheaderinfo()
    assert f.OBSTYPE == 'ZERO'
    assert f.DATEOBS == datetime(2024, 7, 17, 12, 9, 56, 120813)