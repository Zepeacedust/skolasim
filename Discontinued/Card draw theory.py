from random import shuffle
hand = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}
library = ["chup","zap","zap","shrink","teleport", "stab", "fireball", "stab", "zap"]
shuffle(library)
cards = {"chup": "","zap": "", }
def draw(num):
    if num > len(library):
        num = len(library)
    for y in range(num):
        for x in range(len(hand)):
            if hand[x+1] == "":
                hand[x+1] = library.pop(0)
                shuffle(library)
                break
def use(slot):
    library.append(hand[slot])
    print("used " + hand[slot])
    hand[slot] = ""

draw(9)
print(hand)
