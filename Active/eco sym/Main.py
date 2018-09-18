import pprint
import Creatures
import map
x = Creatures.Cow()
pprint.pprint(map.cellular_automata(255, 255))
grid = [[1,1,1],[1,1,1],[1,1,1]]
map.scan_neighborhood(grid,1,1)