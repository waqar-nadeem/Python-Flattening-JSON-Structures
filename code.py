import json

def flatten_json(data, parent_key='', sep='.'):
    items = {}
    if isinstance(data, dict):
        for k, v in data.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            items.update(flatten_json(v, new_key, sep=sep))
    elif isinstance(data, list):
        for i, v in enumerate(data):
            new_key = f"{parent_key}{sep}{i}" if parent_key else str(i)
            items.update(flatten_json(v, new_key, sep=sep))
    else:
        items[parent_key] = data
    return items

if __name__ == "__main__":
    with open("input.json", "r") as f:
        data = json.load(f)
    flat = flatten_json(data)
    with open("output.json", "w") as f:
        json.dump(flat, f, indent=4)
