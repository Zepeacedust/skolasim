import random
from math import modf
# determina population & aðra hluti
blebs = int(input("Number of Blebs: "))
oldblebs = 0
blorps = int(input("Number of blorps: "))
duration = int(input("Number of cycles: "))
startfood = int(input("Starting food: "))
growrate = int(input("Food growth rate: "))
food = startfood
for time in range(duration):
    food = food + growrate  # grow food
    for x in range(1, blebs, 3):  # bleb recreation
            if food >= 1:
                blebs += blebs
                food -= food
    for x in range(blebs):  # bleb survuival
        if food <= 1:  # bleb eats
            food -= food
        else:
            if round(random.random == 1):  # bleb starving
                blebs -= blebs
    print(blebs)