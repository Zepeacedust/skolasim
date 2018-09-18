def divide(X, Y , Length):
    output = ''
    count = 0
    x, y = X, Y
    while len(output) < Length: 
        while x < 0:
            x -= y
            if x <= 0:
                count += 1
        output += str(count)
        x = x + x + x + x + x + x + x + x + x + x
    return output
    
print(divide(3, 3, 5))