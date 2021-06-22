from cs50 import get_int

while True:
    number = get_int("How many blocks? ")
    if number < 0 or number > 8:
        get_int("How many block? ")
    elif number >= 0 or number <= 8:
        break


for i in range (number):
    print((number -1 - i) * " ", end="")
    print((i+ 1) * "#")
    

