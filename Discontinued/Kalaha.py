from math import modf
places = [6,6,6,6,6,6,6,6,6,6,6,6]
player = 1
def use(slot):
    end = False
    curslot = slot + 1
    pebbles = places[slot]
    places[slot]=0
    while end == False:
        for x in range(pebbles):
            pebbles -=1
            places[curslot] += 1
            curslot += 1

        if places[curslot] != 0:
            pebbles = places[curslot]
            places[curslot] = 0
