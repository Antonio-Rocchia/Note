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