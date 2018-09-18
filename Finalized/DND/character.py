from random import randint
def roll(number,size):
    result = 0
    while (number > 0):
        result = (randint(1,(size)) + result)
        number = (number - 1)
    return result
def noot(string):
    f = open("newchar.txt","a")
    f.write (string)
    f.close()
#finna age og decida die size
age = input("enter age ")
if (int(age) < 21):
    events =1
elif (int(age) < 31):
        events = 3
elif (int(age) < 41):
        events = 6
elif (int(age) < 51):
        events = 8
elif (int(age) < 61):
        events = 10
else:
    events = 12
#rolla fyrir life events
output = ""
events = roll(1,events)
while (events > 0):
    currentroll = roll(1,100)
    if (currentroll < 10):
        subroll = roll(1,12)
        if subroll < 3:
            subsubroll = roll(1,12)
            if subsubroll == 1:
                output = "died by unknown casues"
            elif subsubroll == 2:
                output = "was murdered"
            elif subsubroll == 3:
                output = "was killed in battle"
            elif subsubroll == 4:
                output = "was in a class or occupation related accident"
            elif subsubroll == 5:
                output = "was in a class or occupation urelated accident"
            elif subsubroll < 8:
                output = "died by natural causes"
            elif subsubroll == 8:
                output = "appearently commited suicide"
            elif subsubroll == 9:
                output = "was torn apart by wild animals"
            elif subsubroll == 10:
                output = "was consumed by monsters"
            elif subsubroll == 11:
                output = "was executed for a crime or tortured to death"
            else:
                output = "died by a bizzare event"
            output = ("family member or close friend " + output)
        elif subroll == 3:
            output = "a friendship ended bitterly and the other party is now hostile"
        elif subroll == 4:
            output = "lost all posessions in a natural disaster and had to rebuild"
        elif subroll == 5:
            output = ("you were falsly imprisoned for %d years" % (roll(1,6)))
        elif subroll == 6:
            output = "war destroyed home, had to rebuild"
        elif subroll == 7:
            output = "a lover disappeared without a trace"
        elif subroll == 8:
            output = "a terrible blight occurred and many siblings starved"
        elif subroll == 9:
            output = "did something that brought great shame tou you in the eyes of your family"
        elif subroll == 10:
            output = "you were exiled from your community"
        elif subroll == 11:
            output = "a romantic relationship ended"
        else:
            subsubroll = roll(1, 12)
            if subsubroll == 1:
                output = "died by unknown casues"
            elif subsubroll == 2:
                output = "was murdered"
            elif subsubroll == 3:
                output = "was killed in battle"
            elif subsubroll == 4:
                output = "was in a class or occupation related accident"
            elif subsubroll == 5:
                output = "was in a class or occupation urelated accident"
            elif subsubroll < 8:
                output = "died by natural causes"
            elif subsubroll == 8:
                output = "appearently commited suicide"
            elif subsubroll == 9:
                output = "was torn apart by wild animals"
            elif subsubroll == 10:
                output = "was consumed by monsters"
            elif subsubroll == 11:
                output = "was executed for a crime or tortured to death"
            else:
                output = "died by a bizzare event"
            output = ("a lover " + output)
    elif currentroll < 21:#rolla boons table
        subroll = roll(1,10)
        if subroll == 1:
            output = "a friendly wizard gave you a cantrip scroll"
        elif subroll == 2:
            output = "saved the life of a commoner that now owes you a life dept"
        elif subroll == 3:
            output = "found a riding horse"
        elif subroll == 4:
            output = ("found %d GP" % (roll(1,20)))
        elif subroll == 5:
            output = "got given a simple weapon"
        elif subroll == 6:
            output = "found a trinket"
        elif subroll == 7:
            output = "helped a temple, next visit you can fully heal"
        elif subroll == 8:
            output = "got given a potion of healing or a flask of acid"
        elif subroll == 9:
            output = "found a treasure map"
        else:
            output = ("a distant relative gave you a stripend for a comfortable lifestyle for %d years" % (roll(1,20)))
    elif (currentroll < 31):
        output = "fell in love or got married if you get this result multiple times you can have a child instead"
    elif (currentroll < 41):
        output = "made an enemy out of an adventurer"
    elif (currentroll < 51):
        output = "made friends with an adventurer"
    elif (currentroll < 71):#worked
        output = ("worked for %d GP" % roll(2,6))
    elif (currentroll < 76):#met an important person
        output = "met an important person"
    elif (currentroll < 81):#adventures table
        subroll = roll(1,100)
        if (subroll < 10):
            subsubroll = roll(1,3)
            if (subsubroll == 1):
                output = "Nearly died, lost an ear."
            elif (subsubroll == 2):
                output = ("Nearly died, lost %d finger/s" % roll(1,3))
            else:
                output = ("Nearly died, lost %d toe/s" % roll(1,4))
        elif (subroll < 21):
            output = "Wounded, mostly healed"
        elif (subroll < 31):
            outpur = "Wounded, fully healed"
        elif (subroll < 41):
            output = "contracted a disease"
        elif (subroll < 51):
            output = "poisioned, next poison save has disadvantage"
        elif (subroll < 61):
            output = ("lost a trinket")
        elif (subroll < 71):
            output = "horribly frightened"
        elif (subroll < 81):
            output = "learned a great deal"
        elif  (subroll < 91):
            output = ("found %d gold pieces" % roll(2,6))
        elif (subroll < 100):
            output = ("found %d gold pieces" % (roll(1,20)+50))
        else:
            output = "found a common magic item"
        output = ("went on an adventure, "+ output)
    elif (currentroll < 86):#rolla supernatural event
        subroll = roll(1,100)
        if subroll < 6:
            output = ("ensorcelled for %d years" % (roll(1,6)))
        elif subroll < 11:
            output = "saw a demon and ran away"
        elif subroll < 16:
            output = ("tempted by a devil, dc 10 wisdom save or gain %d gold and shift towards evil" % (roll(1,20)))
        elif subroll < 21:
            output = "you woke up a mile away from home, no idea how"
        elif subroll < 31:
            output = "visited a holy site and felt the presence of the divine"
        elif subroll < 41:
            output = "saw a strange thing and is convinved that it is an omen"
        elif subroll < 51:
            output = "escaped certain death and is convinced it was godly intervention"
        elif subroll < 61:
            output = "witnessed a minor miracle"
        elif subroll < 71:
            output = "explored an empty house and discovered it was haunted"
        elif subroll < 76:
            subsubroll = roll(1,6)
            if subsubroll == 1:
                output = "celestial"
            elif subsubroll == 2:
                output = "devil"
            elif subsubroll == 3:
                output = "demon"
            elif subsubroll == 4:
                output = "fey"
            elif subsubroll == 5:
                output = "elemental"
            else:
                output = "undead"
            output = ("was briefly possessed by " + output)
        elif subroll < 81:
            output = "saw a ghost"
        elif subroll < 86:
            output = "saw a ghoul eat a person"
        elif subroll < 91:
            output = "celestial or fiend warned you of dangers yet to come"
        elif subroll < 96:
            output = "brief visit in the feywild or shadowfell"
        else:
            outpu = "saw a portal to another plane"
    elif (currentroll < 91):#rolla war tabe
        subroll = roll(1,12)
        if (subroll == 1):
            output = "knocked out and left for dead, no memory of the battle"
        elif (subroll < 4):
            output = "badly injured, still have scars"
        elif (subroll == 4):
            outpuy = "ran away from battle, still feel shame."
        elif (subroll < 8):
            output = "suffered minor injuries, no scars"
        elif (subroll < 10):
            output = "you survived the battle but suffer horrible nightmares"
        elif (subroll < 12):
            output = "but escaped unharmed but many of your friends were injured or lost"
        else:
            output = "you returned a hero"
        output = ("you went to war, "+ output)
    elif (currentroll < 96):#crime table
        subroll = roll(1,8)
        if (subroll == 1):
            output = "murder"
        elif (subroll == 2):
            output = "theft"
        elif (subroll == 3):
            output = "burglary"
        elif (subroll == 4):
            output = "assault"
        elif (subroll == 5):
            output = "smuggling"
        elif (subroll == 6):
            output = "kidnapping"
        elif (subroll == 7):
            output = "extortion"
        else:
            output = "counterfeiting"
        subroll = roll(1,12)
        if (subroll < 4):
            output = ("accused of but did not commit " + output)
        elif (subroll < 7):
            output = ("commited or helped commit " + output + " but the authorities did not conivct")
        elif (subroll < 9):
            output = ("you were nearly cought commiting " + output + " and are wanted in the area")
        else:
            output = ("you were caught and covicted commiting " + output + " and were sentanced to %d years in jail" % roll(1,4))
    elif (currentroll < 100):#rolla arcane matters
        subroll = roll(1,10)
        if (subroll == 1):
            output = "you were charmed or frightened by a spell"
        elif (subroll == 2):
            output = "injured by a spell"
        elif (subroll == 3):
            output = "you saw a powerful spell being cast"
        elif (subroll == 4):
            output = "drank a potion"
        elif (subroll == 5):
            output = "cast a spell scroll"
        elif (subroll == 6):
            output = "teleported"
        elif (subroll == 7):
            output = "turned invisible for a bit"
        elif (subroll == 8):
            output = "saw an illusion"
        elif (subroll == 9):
            output = "saw a conjured creature"
        else:
            output = "fortune was read by diviner"
    else:#rolla wierd stuff
        subroll = roll(1,12)
        if (subroll == 1):
            output = ("you were turned into a toad for %d week/s" % roll(1,4))
        elif (subroll == 2):
            output = "petrified and remained so until freed"
        elif (subroll == 3):
            output = ("enslaved for d% years" % roll(1,6))
        elif (subroll == 4):
            output = ("a dragon held you prisoner for %d month/s" % roll(1,4))
        elif (subroll == 5):
            output = "taken slave by evil humanoids"
        elif (subroll == 6):
            output = "served an adventurer as a hireling"
        elif (subroll == 7):
            output = ("went insane for %d year/s" % roll(1,6))
        elif (subroll == 8):
            output = "a lover was secretly a silver dragon"
        elif (subroll == 9):
            output = "almost sacrificed by a cult"
        elif (subroll == 10):
            output = "met a really poweful being and survived"
        elif (subroll == 11):
            output = "swallowed for a month by a fish"
        else:
            output = "a poweful being granted you a wish, fucked it up"
    events = (events - 1)
    print (output)
    output = ""

input()