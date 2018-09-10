import random
#formattið er númerið sem mánuðurinn er, [venjuleg lengd, lengd á hlauári]
manadarlengdir = {1: [31,31], 2: [28,29], 3: [31,31], 4: [30,30], 5: [31,31], 6: [30, 30], 7: [31,31], 8: [30,30], 9: [31,31], 10: [31,31], 11: [30,30], 12:[31,31]}
#DD MM YY RRR Ö
manudur = 1
year = random.randint(1000, 3000)
#allar raglur með hlaupar.
if year % 4 == 0 and ((not year % 100 == 0) or year % 400 == 0):
    dagur = random.randint(1,366)
    hlaupar = 1
else:
    dagur = random.randint(1,365)
    hlaupar = 0
#að finna hvaða manudur dagurinn er í og hvaða mánaðardagur
while dagur > manadarlengdir[manudur][hlaupar]:
    dagur -= manadarlengdir[manudur][hlaupar]
    manudur += 1
if len(str(dagur)) < 2: kennitala = "0" + str(dagur)#passa að allt sé tveggja stafa
else: kennitala = str(dagur)
if len(str(manudur)) < 2: kennitala += "0" + str(manudur)#passa að allt sé tveggja stafa
else: kennitala = kennitala + str(manudur)
kennitala = kennitala + str(year)[-2:]#seinustu tveir stafir í ártalinu
kennitala = kennitala + str(random.randint(1,999))#3 random tölur
kennitala =  kennitala + str(year)[-3]#öldin
print(kennitala)