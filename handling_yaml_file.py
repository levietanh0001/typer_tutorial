import yaml


with open('fastapi.yml', 'r') as f:
    contents = yaml.safe_load_all(f)
    for i in contents:
        print(i)


