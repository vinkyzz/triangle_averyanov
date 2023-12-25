import math

def triangle(n):
    num_strr = math.ceil(n / 2)

    for i in range(1, num_strr + 1):
        print(i * '*')
    for j in range(num_strr - 1, 0, -1):
        print(j * '*')

triangle(3) 
