import json

# construct tree
p = "./encode_directory.json"
f = open(p)
s = f.read()

o = json.loads(s)

def pretty_print(root) -> list[str]:
    toReturn = [f"{root['name']}"]

    if 'children' in root:
        for c in root['children']:
            toReturn += [" " + s for s in pretty_print(c)]

    return toReturn

for l in pretty_print(o):
    print(l)
