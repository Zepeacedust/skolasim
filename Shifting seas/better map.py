from random import randint

def renderdata(tiledata):#breyta tiledata í rendered data
    if tiledata == 0:
        return "O"
    elif tiledata == 1:
        return "~"
    elif tiledata == 2:
        return "#"
    else:
        return "M"


def tiledata(value):#assigna values að tiles eftir input
    if value < 2:
        return 0
    elif value < 6:
        return 1
    elif value == 6:
        return 2
    else:
        return 3


map = []#generatea mapdata layer by layer
for y in range(100):
    current_layer = []
    for x in range(100):
        current_layer.append(tiledata((randint(0, 9))))
    map.append(current_layer)


for layer in map:#render map
    renderlayer = []
    for tile in layer:
        renderlayer.append(renderdata(tile))
    print(" ".join(renderlayer))
