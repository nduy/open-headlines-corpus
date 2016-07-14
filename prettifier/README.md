# Text corpus pretifier
This is a python Script that get a JSON file as input, and output anothe
r JSON file after prefifying. Specifically, It do the following things:
- Replace some unicode characters that usually cause error by regular ch
acracters.
- Filter doucuments by lenght (excluded punctuation characters) 

The script will be run with the following syntax:
python prettifier.py input_json_file.json output_json_file.json

Note: the format of fields in input and output file might have some diff
erences. However, when we import it into mongoDB database, the result wi
ll be the same.
