import os

import pytest

from ffile_man.manager import Manager

from datetime import datetime


def test_no_fits_files(capsys):
    folder_path = os.path.join("FITS/Empty_folder")
    m = Manager(folder_path)
    m.print_list()
    captured = capsys.readouterr()
    assert captured.out == "\n"


def test_sub_folders(capsys):
    folder_path = os.path.join("FITS/some_fits_files")
    m = Manager(folder_path, sub_folders=True)
    m.print_list()
    captured = capsys.readouterr()
    exp_out = "FITS_File(name='20240716_s4c1_000001.fits', folder_path='FITS/some_fits_files', OBSTYPE='ZERO', DATEOBS=datetime.datetime(2024, 7, 17, 12, 9, 56, 120813))\nFITS_File(name='20240716_s4c1_000002.fits', folder_path='FITS/some_fits_files', OBSTYPE='ZERO', DATEOBS=datetime.datetime(2024, 7, 17, 12, 9, 57, 624311))\nFITS_File(name='20240716_s4c1_000029.fits', folder_path='FITS/some_fits_files/one_more_folder', OBSTYPE='DARK', DATEOBS=datetime.datetime(2024, 7, 17, 12, 11, 13, 852648))\nFITS_File(name='20240716_s4c1_000030.fits', folder_path='FITS/some_fits_files/one_more_folder', OBSTYPE='DARK', DATEOBS=datetime.datetime(2024, 7, 17, 12, 11, 15, 351810))\n"
    assert captured.out == exp_out

def test_comaprison_operators(capsys):
    folder_path = os.path.join("FITS")
    m = Manager(folder_path)
    m>= datetime(2024,7,17,12,11)
    exp_out  ="FITS_File(name='20240716_s4c1_000022.fits', folder_path='FITS', OBSTYPE='DARK', DATEOBS=datetime.datetime(2024, 7, 17, 12, 11, 0, 222371))\nFITS_File(name='20240716_s4c1_000023.fits', folder_path='FITS', OBSTYPE='DARK', DATEOBS=datetime.datetime(2024, 7, 17, 12, 11, 1, 722167))\nFITS_File(name='20240716_s4c1_000024.fits', folder_path='FITS', OBSTYPE='DARK', DATEOBS=datetime.datetime(2024, 7, 17, 12, 11, 3, 224597))\nFITS_File(name='20240716_s4c1_000025.fits', folder_path='FITS', OBSTYPE='DARK', DATEOBS=datetime.datetime(2024, 7, 17, 12, 11, 4, 724791))\nFITS_File(name='20240716_s4c1_000026.fits', folder_path='FITS', OBSTYPE='DARK', DATEOBS=datetime.datetime(2024, 7, 17, 12, 11, 9, 354871))\nFITS_File(name='20240716_s4c1_000027.fits', folder_path='FITS', OBSTYPE='DARK', DATEOBS=datetime.datetime(2024, 7, 17, 12, 11, 10, 852537))\nFITS_File(name='20240716_s4c1_000028.fits', folder_path='FITS', OBSTYPE='DARK', DATEOBS=datetime.datetime(2024, 7, 17, 12, 11, 12, 352386))\n"
    m.print_list()
    captured = capsys.readouterr()
    assert captured.out == exp_out
