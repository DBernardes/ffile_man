from datetime import datetime

from ffile_man.fits_file import FITS_File


def test_fits_atribs():
    f = FITS_File("20240716_s4c1_000001.fits", "FITS/some_fits_files")
    f._extractheaderinfo()
    assert f.OBSTYPE == "ZERO"
    assert f.DATEOBS == datetime(2024, 7, 17, 12, 9, 56, 120813)
    assert f.name == "20240716_s4c1_000001.fits"
    assert f.folder_path == "FITS/some_fits_files"
