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


if CONTEXT["config_position"] == "home":
    if platform.system() == "Windows":
        moved_paths.append((".latexmkrc", "C:\\latexmk\\LatexMk\\latexmkrc"))
        os.system(f"setx %CHKTEXRC% {HOME_DIR}")
    else:
        moved_paths.append((".latexmkrc", "~/.latexmkrc"))
    moved_paths.extend(
        [
            (".chktexrc", "~/.chktexrc"),
            (".latexindent.yaml", "~/.latexindent.yaml"),
        ]
    )
    with (HOME_DIR / ".indentconfig.yaml").open("w+", encoding="utf8") as fp:
        fp.write(f"path:\n  - {HOME_DIR / 'latexindent.yaml'}\n")

elif CONTEXT["config_position"] == "none":
    removed_paths.extend([".chktexrc", ".latexmkrc", ".latexindent.yaml"])

if not context_bool("biblatex"):
    removed_paths.append("references.bib")

remove_paths()
move_paths()
