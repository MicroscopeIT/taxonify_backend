import csv
import fire
import json


def add(node, values):
    """Add values as consecutive levels to the node dictionary
    node -- a dictionary
    values -- a list of string values
    """
    value = values[0]
    if value not in node:
        node[value] = {}
    rest = values[1:]
    if rest:
        add(node[value], rest)


def generate(in_file_name, out_file_name=""):
    taxonomy = {}

    with open(in_file_name, "r") as file_object:
        rows = csv.reader(file_object, delimiter=',')
        for values in rows:
            add(taxonomy, values)

    # if no output file specified produce result to stdout
    if out_file_name == "":
        y = json.dumps(taxonomy, sort_keys=True, indent=4, separators=(',', ': '))
        print(y)
    else:
        with open(out_file_name, 'w') as outfile:
            outfile.write(json.dumps(taxonomy, sort_keys=True, indent=4, separators=(',', ': ')))
            outfile.close()


if __name__ == '__main__':
    fire.Fire(generate)
