# Build specification
The ```build_spec.json``` file is used by the ```BuildSnip.py``` script.

> Read [```BuildSnip.py``` documentation](./BuildSnip.md)

[From README.md](../README.md)
> For each folder in ```.script/manage/snippet```, ```BuildSnip.py``` searches a ```build_spec.json``` file. This files tells the script:
> - how to name the output file coming out of that folder
> - where should it link to if it is a config file for a particular program
> - which input file extensions are used to store each snippet, you can specify more than one

To do that the ```build_spec.json``` will contain 4 keys:
```json
{
"output_file": "",
"output_dir": "",
"link_to_config": "",
"input_file_extension": ""
}
```

## Output file
The ```"output_file"``` key holds the name of the output file and its extension

Example:
```json
"output_file": "latex.hsnips",
```

Not setting this variable produces an error.
## Output directory
The ```"output_dir"``` key holds the name of the desired output directory.

Example
```json
"output_dir": "$NOTE/.settings/vs_code",
```

If left blank it will default to the .settings folder to prevent errors

```json
"output_dir": "", -> Defaults to $NOTE/.settings,
```
## Link to program configuration file
The ```"link_to_config"``` key holds the path to the program to configuration that will be overwritten. 

The ```BuildSnip.py``` script will check if the file ```"output_file"``` exists in ```"output_dir"``` and if it doesn't it will automatically create a soft link from the path specified in ```"link_to_config"``` named ```"output_file"``` in ```"output_dir"```

Example
```json
"link_to_config": "~/.config/Code/User/hsnips/latex.hsnips",
```

Leaving this blank will produce a warning in the console log but will not produce an error. The output file named ```"output_file"``` will be placed in ```"output_dir"```

## Input file extensions
The ```"input_file_extensions"``` key holds the extension type of the file used to store the snippets

The ```BuildSnip.py``` script will only look for files with that extensions.

```json
"input_file_extension": ".hsnips",
```

If this is empty the ```BuildSnip.py``` script will produce a warning and use every file in the folder. 




