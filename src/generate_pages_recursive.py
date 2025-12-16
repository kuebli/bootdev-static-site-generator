import pathlib
import os
from generate_page import generate_page


def generate_pages_recursive(
    dir_path_content: str, template_path: str, dest_dir_path: str
):
    current_path = pathlib.Path(dir_path_content)

    # foreach item in static_path:
    for item in current_path.glob("*"):
        if item.is_file():
            generate_page(
                str(item.absolute()),
                template_path,
                dest_dir_path + item.name.split(".")[0] + ".html",
            )
        elif item.is_dir():
            subdir_path_content = dir_path_content + item.name + "/"
            dest_subdir_path = dest_dir_path + item.name + "/"
            os.mkdir(dest_subdir_path)
            generate_pages_recursive(
                subdir_path_content, template_path, dest_subdir_path
            )
