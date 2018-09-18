power = float(input("enter power: "))
length = int(input("enter length: "))
output = 0
for x in range(1, length):
    output += 1 / (x ** power)
print(output)
#conclusion: actually successful