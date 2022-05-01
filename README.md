# Documentation
This repo contains all my notes and the my configuration for vim with ultisnip

## Settings
The ```.settings``` folder contains soft links for all applications's setting used in the workflow.

The soft links are organized in per application in a folder structure. For example the ```.settings/vs_code``` folder has links to Vs Code's ```settings.json``` and ```latex.hsnip``` for the hsnip plugin.

## Scripts
The ```.scripts``` folder is organized per functionality in a folder structure:
```
.scripts/
├── create
├── manage
│   └── snippet
└── setup
```
- ```.scripts/create```: generate files 
- ```.scripts/manage```: modify files created with other scripts with ease
- ```.scripts/setup```: setup the entire workflow 

### Setup
In setup the ```install_latex.sh``` script will install all the packages you need to compile the .tex notes. 

To use it run 
```bash
chmod +x .script/setup/install_latex.sh
.script/setup/install_latex.sh
```
Input your password to install the packages.

The script uses apt so it works for debian based distribution. You can check which packages the script installs and find them for your package manager using 
```bash
nano .script/setup/install_latex.sh
```

### Snippet
The ```.script/manage/snippet/BuildSnips.py``` script is used to update the snippet configurations for all application.

> See [```BuildSnip.py``` documentation](./.docs/BuildSnip.md)

For each folder in ```.script/manage/snippet```, ```BuildSnip.py``` searches a ```build_spec.json``` file. This files tells the script:
- how to name the output file coming out of that folder
- where should it link to if it is a config file for a particular program
- which input file extensions are used to store each snippet, you can specify more than one

> Read [build_spec.json documentation](./.docs/build_spec.md)

Note that the ```BuildSnip.py``` script does not impose a particular structure. 

It checks all the folders in ```.script/manage/snippet```, if it does not find a ```build_spec.json``` file inside one it produces a warning explaining that it is falling back to using default options for that folder.

As an example, here's a ```hsnip_Latex``` folder inside ```.script/manage/snippet```

