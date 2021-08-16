import argparse
import json
import pathlib

ENCODE_DIRECTORY = pathlib.Path("./encode_directory.json")

parser = argparse.ArgumentParser("Capture and encode a directory structure using Javascript object notation")
parser.add_argument('root', type=pathlib.Path)

args = parser.parse_args()

def ignore_dotfiles(p: pathlib.Path) -> bool:
    return p.name.startswith(".")

def traverse_directory(root: pathlib.Path, filter=ignore_dotfiles):
    result = {
        "name": root.name,
        "directory": root.is_dir(),
    }
    if root.is_dir():
        result["children"] = [
            traverse_directory(child) for child in root.iterdir() if not filter(child)
        ]
    return result

json.dump(
    traverse_directory(args.root),
    ENCODE_DIRECTORY.open(
        mode='w'
    )
)