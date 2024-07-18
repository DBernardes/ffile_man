import os

import pytest

from ffile_man.manager import Manager


def test_no_fits_files(capsys):
    folder_path = os.path.join("FITS/Empty_folder")
    m = Manager(folder_path)
    m.print_list()
    captured = capsys.readouterr()
    assert captured.out == "\n"
