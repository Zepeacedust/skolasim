#þetta reiknar fermetra og leggur þá saman
imput = True
output = 0
def is_number(x):#gáir hvort tala virki sem float
    try:
        float(x)
        return True
    except ValueError:
        return False
while imput == True:
    lengd = input("Lengd: ")#fær lengdir og stærð þeirra
    lengd_size = input("M eða CM? ")
    breidd = input("Breidd: ")
    breidd_size = input("M eða CM? ")
    if (is_number(breidd) and is_number(lengd)):#breitir í metra
        lengd = float(lengd)
        breidd = float(breidd)
        if lengd_size == "CM":
            lengd = lengd / 100
        if breidd_size == "CM":
            breidd = breidd / 100
    else:
        print("Villa ekki tala!")
        break
    currentnum = round(lengd * breidd, 2)#margfaldar
    output = round(currentnum + output, 2)#geimir töluna
    print(currentnum)
    if input("Viltu halda áfram? ") == "já":#spyr hvort það verði önnur tala
        imput = True
    else:
        imput = False
print(str(output), "M^2")