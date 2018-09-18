print("This is an experimental system to store  10 * X black and white images.")
print("Press 1 for Decoding")
print("Press 2 for encoding")
def conv(num,b):
    convStr = "0123456789abcdefghijklmnopqrstuvwxyz"
    if num == 0:
        return("00")
    if num<b:
        return convStr[num]
    else:
        return conv(num//b,b) + convStr[num%b]
state = input()
output = ""
if state == "1":
    decode = input("Text to decode: ")
    for x in range(0, len(decode), 2):
        output = bin(int(decode[x] + decode[x+1], 32))[2:]
        if len(output) != 10:
            output = "0" * (10 - len(output)) + output
        print(output)
elif state == "2":
    length = int(input("Image length: "))
    for x in range(length):
        output = output + conv(int(input("this is line " + str((x + 1)) + ":"),2),32)
    print(outp+ut)