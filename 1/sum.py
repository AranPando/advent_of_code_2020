'''
    A file called input.txt contains numbers on each line. 
    
    Boss: "SOLIDER! IT IS YOUR MISSION TO FIND THE TWO NUMBERS THAT SUM TO 2020
    AND THEN RETURN THEIR MULTIPLICATION!"
    Me: "YESSSIR! ... do you mind if its in python? *right finger gun* *left finger gun*"
    Boss: *sigh*

'''

# import file
values = []
with open('input.txt', 'r') as f:
    for x in f:
        values.append(int(x.replace('\n','')))

print(values)

# iterate array and search ('in') for matching value.

for x in values:
    matching = 2020 - x
    print(x, matching)
    if matching in values:
        if matching == x and values.count(x) < 2:
            continue
        print(f"The numbers are: {x} and {matching}")
        print(f"The number is: {x*matching}")
        break

print("End of program")

