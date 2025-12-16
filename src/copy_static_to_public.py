from pathlib import Path
import pathlib
from shutil import rmtree
import shutil
import os


def copy_static_to_public(current: str, target: str, target_emptyed=False):
    # delete content in public if not done
    if not target_emptyed:
        empty_directory(target)

    current_path = pathlib.Path(current)
    target_path = pathlib.Path(target)

    # foreach item in static_path:
    for item in current_path.glob("*"):
        if item.is_file():
            shutil.copy(item.absolute(), target_path.absolute())
        elif item.is_dir():
            subdir = target + item.name + "/"
            os.mkdir(subdir)
            copy_static_to_public(str(item.absolute()), subdir, True)


def empty_directory(path: str):
    dir = Path(path)
    for item in dir.glob("*"):
        if item.is_file():
            item.unlink()
        elif item.is_dir():
            rmtree(item.absolute())
