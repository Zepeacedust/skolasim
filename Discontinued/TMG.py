import math
cycles = 1
end = False
building_list = {"Faulty clock": 1, "Chrono slower": 4}#listi af byggingum sem hægt er að byggja og price
possesions = {"Faulty clock": 1, "Chrono slower": 0}# current posessions
buildcost = {}#bara að segja að þetta sé til
while not end:
    for x in range(len(building_list.keys())):# setta buildcost
        buildcost[list(building_list.keys())[x]] = building_list[list(building_list.keys())[x]] * 1.1 ** possesions[list(building_list.keys())[x]]# buildcost = baseprice * 1.1 ^ number of buildings
    currentaction = input("Action: ")
    if currentaction == "end":
        end = True# simple exit game
    elif currentaction == "buy":
        for x in range(len(building_list.keys())):
            print(list(building_list.keys())[x], list(buildcost.values())[x])
        subaction = input("What do you want to buy? ")


print(buildcost)