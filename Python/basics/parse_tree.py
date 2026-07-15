from ast import parse
from ast import dump

tree = parse("x = 5")
print(dump(tree))
