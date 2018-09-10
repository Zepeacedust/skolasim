outputscript = open("output.txt", "a+")
what = input("what ")
for x in range(int(input("how many? "))):
    outputscript.write(what + "\n")
originscript = open("output.txt", "r+")
print(originscript.read())