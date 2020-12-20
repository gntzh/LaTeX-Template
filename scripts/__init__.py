from pathlib import Path
import shutil
import click

BASE_DIR: Path = Path(__file__).resolve(strict=True).parent.parent


@click.command()
@click.argument(
    "dest",
    type=click.Path(
        writable=True,
        file_okay=False,
        resolve_path=True,
    ),
)
def main(dest: str):
    dest: Path = Path(dest)
    try:
        dest.rmdir()
    except FileNotFoundError:
        pass
    except OSError as e:
        print(type(e))
        exit()
    dest.mkdir(exist_ok=True, parents=True)
    (dest / "style").symlink_to(BASE_DIR / "style", True)
    (dest / "scripts").symlink_to(BASE_DIR / "scripts", True)
    (BASE_DIR / ".latexmkrc").link_to(dest / ".latexmkrc")
    shutil.copy((BASE_DIR / "main.tex"), (dest / "main.tex"))
    shutil.copy((BASE_DIR / "preamble.tex"), (dest / "preamble.tex"))
    shutil.copy((BASE_DIR / ".gitignore"), (dest / ".gitignore"))


if __name__ == "__main__":
    main()
