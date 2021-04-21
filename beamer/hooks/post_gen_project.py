import os
import platform
from collections import OrderedDict
from pathlib import Path
from typing import List, Tuple, Union

HOME_DIR = Path.home()
PROJECT_DIR = Path.cwd()
CONTEXT: OrderedDict = {{cookiecutter}}

removed_paths: List[Union[str, Path]] = []
moved_paths: List[Tuple[Union[str, Path], Union[str, Path]]] = [
    ("_gitignore", ".gitignore"),
]


def make_path(path: Union[str, Path]) -> Path:
    if isinstance(path, str):
        path = Path(path).expanduser()
    return path


def context_bool(key: str) -> bool:
    if CONTEXT[key] == "True":
        return True
    return False


def remove_paths():
    for path in removed_paths:
        path = make_path(path)
        path.unlink()


def move_paths():
    for src, dest in moved_paths:
        src = make_path(src)
        dest = make_path(dest)
        src.rename(dest)

remove_paths()
move_paths()
