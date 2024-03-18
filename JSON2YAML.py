import yaml, json

with open("QLAB01_LiveCycle.json") as json_file:
    with open('result.yaml', 'w') as yaml_file:
        yaml.dump(json.load(json_file), yaml_file, default_flow_style=False)

