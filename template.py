'''
    A file called input.txt contains numbers on each line. 
    
    Boss: "SOLIDER! IT IS YOUR MISSION TO FIND THE TWO NUMBERS THAT SUM TO 2020
    AND THEN RETURN THEIR MULTIPLICATION!"
    Me: "YESSSIR! ... do you mind if its in python? *right finger gun* *left finger gun*"
    Boss: *sigh*

'''

# Read from input file
values = []
with open('input.txt', 'r') as f:
    for x in f:
        values.append(int(x.replace('\n','')))


# Logic TODO
