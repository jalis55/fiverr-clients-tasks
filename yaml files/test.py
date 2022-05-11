import yaml
import deepdiff
import json


try:
    file1=open('example.yaml','r')
    file2=open('example2.yaml','r')

    # parsed_yaml=yaml.safe_load(stream)
    dict1=yaml.safe_load(file1)
    dict2=yaml.safe_load(file2)


    


    diff = dict(deepdiff.DeepDiff(dict1, dict2))
    print(diff.keys())
    print(diff)
    # print(json.dumps(json.loads(diff.to_json()), indent=4))  
except yaml.YAMLError as exc:
    print(exc)