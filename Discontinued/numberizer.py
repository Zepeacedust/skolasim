startnum = int(input("Starting number: "))
modulo = int(input("Modlulo: "))
for x in range(int(input("number of iterations? "))):
    print((startnum ** x) % modulo)