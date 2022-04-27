from pathlib import Path


with open('./output.snipbld', 'a') as output_build:
    output_build.truncate(0)
    for path in Path('snipFiles').rglob('*.snipbld'):
        with open(path, 'r') as input_f:
            output_build.write(input_f.read())
            output_build.write('\n')
