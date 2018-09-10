import time


nafn = input("skráðu inn nafn nýa filesins: ")
output = open(nafn, "w")#opna / búa til said file
nafn = input("hvað heitir þú? ")
output.write("# " + nafn + " " + time.asctime(time.gmtime()) + "\n")#setja initial name/datetime comment
output.write("continue = True\n")
output.write("while continue:\n   #setja upp valmynd\n")#setja upp loop
valmyndir = int(input("hversu marga liði viltu hafa:"))
for x in range(valmyndir):#gera eins margar l-valmyndir og userin biður um
    output.write("    print('veldu %i fyrir lið %i')\n" % (x+1, x+1))
output.write("    print('veldu exit til að hætta')\n")
output.write("    liður = input()\n")#láta userinn selcta
output.write("    if liður == '1': \n        # cóði fyrir lið 1\n")#gera if statement fyrir fyrsta liðinn
for x in range(valmyndir-1):
    output.write("    elif liður == '%i': \n        # cóði fyrir lið %i\n" % (x+2, x+2))#gera elif statemenst fyrir alla hina liðina
output.write("    elif liður == 'exit': continue = False# exit condition")