import textwrap
import yaml
import json
import sys

variable_name = sys.argv[1]

with open('tmp.txt') as f:
  input_from_user = f.read()

# step 1: convert to valid yaml
full_definition = f'''\
{variable_name}:
{textwrap.indent(input_from_user, '  ')}
'''

# step 2: convert from yaml to something terraform can read (json?)
yaml_object = yaml.safe_load(full_definition) # yaml_object will be a list or a dict
print(json.dumps(yaml_object))
