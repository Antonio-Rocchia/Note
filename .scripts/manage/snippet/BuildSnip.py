# BuildSnip.py

"""
This script iterates through all directories in the
"$NOTE/.scripts/manage/snippet" directory.

For each directory the script first searches a 
build_spec.json file. 

If it finds it, the script parses the json file and stores
the values extracted from it. If at any point a value is blank, 
the scripts prints a warning to the console log as explained in
build_spec.md documentation file.

If it doesn't file the build_spec.json file it prints a warning to
the console log, telling the user that the default option will be used
and then printing the default options.

Once the script has all the setting configured, it will check
if a file with the specified name exist in the specified directory.

If it doesn't, the script checks if it can create a symbolic link
to the specified configuration file in the specified directory with
the specified name. If this fails it just creates an empy file there
with the correct name

The script then recursively takes the content of every file in the 
opened directory with a valid extension, (read build_spec.md docs to check to specify valid 
extensions), and appends it into the output file

This process is repeated for every folder in "$NOTE/.scripts/manage/snippet"
"""

from pathlib import Path

import sys

from sympy import true
sys.path.append(Path(__file__).parents[2].as_posix())
from config import SETTING_PATH

import json


def isBlank(string):
    if(len(string.strip()) == 0):
        return True
    else:
        return False

def tryParsingKey(key, data):
    if(key in data):
        # Check if the string is empty or blank
        print(data[key])
        if(isBlank(data[key])):
            # If it is empty remain default
            return False
        else:
            # If it has a value overwrite default
            return True
    # If key is not found go to default
    else:
        return False

#def exist_and_is_link(path):

snippetPath = Path(__file__).parent 

snippetDirectories = [snipDir for snipDir in snippetPath.iterdir() if snipDir.is_dir()]

for dir in snippetDirectories:
    # default values for build_spec
    out_name = dir.name
    out_dir = SETTING_PATH
    out_path = Path(SETTING_PATH.as_posix() + "/" + out_name)
    soft_link_path = ""
    file_extensions = "*.*"

    build_spec_search = list(dir.glob("build_spec.json"))
    # Saving the result from the query in a list. The query finds 0 or 1 result, either
    # the file is found or it isn't. I make a check based on the fact than empy lists are
    # falsy values in python
    if(build_spec_search):
        build_spec_path = build_spec_search.pop()
        with build_spec_path.open() as spec_p:
            data = json.load(spec_p)
            # Searching for key and saving values if it's not blank, otherwise defaults
            if(tryParsingKey("output_file", data)):
                out_name = data["output_file"]
                out_path = Path(SETTING_PATH.as_posix() + "/" + out_name)
                print("File name = " + out_name)
            else:
                print("Warning, no output file name defined, " + out_name + " will be used")
            if(tryParsingKey("output_dir", data)):
                out_dir = Path(data["output_dir"]).expanduser()
                out_path = Path(out_dir.as_posix() + "/" + out_name)
                print("dir name = " + out_dir.as_posix())
            else:
                print("Warning, no output file name defined, " + out_dir.as_posix() + " will be used")
            if(tryParsingKey("link_to_config", data)):
                soft_link_path = Path(data["link_to_config"].strip()).expanduser()
                print("link to = " + soft_link_path.as_posix())
                out_path.unlink(missing_ok=True)
                out_path.symlink_to(soft_link_path.as_posix())
            else:
                # If soft link path is not defined but a file already exist with this name in the
                # correct defined output folder, check if it is a soft link, otherwise display a warning
                out_search = list(out_dir.glob(out_name))
                if(out_search):
                    out_path = out_search.pop()
                    if(out_path.is_symlink()):
                        print("Warning, no soft link path defined. But the file " + out_path.as_posix() + " already exist and is soft linked to " + out_path.readlink())
                    else:
                        print("Warning, no soft link path defined. The file will be placed in the " + out_dir.as_posix() + " directory")
                else:
                    out_path.touch()
                    print("Warning, no soft link path defined. The file will be placed in the " + out_dir.as_posix() + " directory")
            if(tryParsingKey("input_file_extension", data)):
                file_extensions = "*" + data["input_file_extension"].strip()
                print("Extensions = " + file_extensions)
            else:
                print("Warning getting using all files from " + dir.as_posix())
    else:
        print("Warning, no output file name defined, " + out_name + " will be used")
        print("Warning, no output file name defined, " + out_dir.as_posix() + " will be used")
        # If soft link path is not defined but a file already exist with this name in the
        # correct defined output folder, check if it is a soft link, otherwise display a warning
        out_search = list(out_dir.glob(out_name))
        if(out_search):
            out_path = out_search.pop()
            if(out_path.is_symlink()):
                print("Warning, no soft link path defined. But the file " + out_path.as_posix() + " already exist and is soft linket to " + out_path.readlink())
            else:
                print("Warning, no soft link path defined. The file will be placed in the " + out_dir.as_posix() + " directory")
        else:
            out_path.touch()
            print("Warning, no soft link path defined. The file will be placed in the " + out_dir.as_posix() + " directory")
        print("Warning getting using all files from " + dir.as_posix())

    snippetFiles = list(dir.rglob(file_extensions))

    with out_path.open("a+") as output:
        output.truncate(0)
        for file in snippetFiles:
            with file.open() as f:
                output.write(f.read() + "\n\n")


