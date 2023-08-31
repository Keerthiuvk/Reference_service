import os
from ruamel.yaml import YAML

def update_yaml_file(file_path, replacements):
    yaml = YAML()
    yaml.indent(offset=2)

    with open(file_path, 'r') as f:
        data = yaml.load(f)

    for key, new_value in replacements.items():
        update_key_value(data, key, new_value)

    with open(file_path, 'w') as f:
        yaml.dump(data, f)

def update_key_value(data, target_key, new_value):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == target_key:
                data[key] = new_value
            if isinstance(value, (dict, list)):
                update_key_value(value, target_key, new_value)
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, (dict, list)):
                update_key_value(item, target_key, new_value)

def main():
    # Extract input keys and values from Jenkins environment variables
    keys_input = os.environ.get("KEYS_PARAM")
    values_input = os.environ.get("VALUES_PARAM")

    # Convert the input strings into lists
    keys = keys_input.split(",")
    values = values_input.split(",")

    # Common replacements
    shared_replacements = {
        "name": os.environ.get("NAME_PARAM"),
        "repository": os.environ.get("REPO_PARAM"),
        "tag": os.environ.get("TAG_PARAM")
    }
    workspace_path = os.environ.get("WORKSPACE")

    specific_file_replacements = {
        os.path.join(workspace_path, "charts/values.yaml"): ["env", "iam_config","dbsecret","replicaCount","probePath"],
        os.path.join(workspace_path, "charts/Chart.yaml"): ["name"],
        os.path.join(workspace_path, "charts/dev-values.yaml"): ["labels", "globalsecret"],
        os.path.join(workspace_path, "charts/hotfix-values.yaml"): ["labels", "globalsecret"],
        os.path.join(workspace_path, "charts/paas3-values.yaml"): ["labels", "globalsecret"],
        os.path.join(workspace_path, "charts/premerge-dev-values.yaml"): ["labels", "globalsecret"],
        os.path.join(workspace_path, "charts/preqa-values.yaml"): ["labels", "globalsecret"],
        os.path.join(workspace_path, "charts/qa3-values.yaml"): ["labels", "globalsecret"],
    }

    for file_path, keys in specific_file_replacements.items():
        print(f"Working on '{os.path.basename(file_path)}':")
        if os.path.exists(file_path):
            replacements = {}
            for key, value in zip(keys, values):
                replacements[key] = value
            update_yaml_file(file_path, {**shared_replacements, **replacements})
            print(f"Replacements in '{os.path.basename(file_path)}' done.")
        else:
            print(f"'{os.path.basename(file_path)}' does not exist. Skipping.")

if __name__ == "__main__":
    main()
