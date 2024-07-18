from ffile_man.manager import Manager
import pytest
import os

def test_no_fits_files(capsys):
    folder_path = os.path.join("FITS/Empty_folder")
    m = Manager(folder_path)
    m.print_list()
    captured = capsys.readouterr()
    assert captured.out == "\n"

