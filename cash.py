from cs50 import get_float

while True:
    c = get_float ("Change owed: ")
    if c < 0:
        get_float ("Change owed: ")
    else:
        break

counter = 0
cents = round(int(c * 100))
while cents > 24:
    cents -= 25
    counter+=1
    if cents < 25:
        break
while cents > 9:
    cents -= 10
    counter += 1
    if cents < 10:
        break
while cents > 4:
    cents -= 5
    counter += 1
    if cents < 5:
        break
while cents > 0:
    cents -= 1
    counter+=1
    if cents < 0:
        break
print(counter)
    