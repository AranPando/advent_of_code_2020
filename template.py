'''
    A file called input.txt contains numbers on each line. 
    
    Boss: "SOLIDER! IT IS YOUR-"
    Me: "yes yes, I can read, thanks."
    Boss: NANI?!

'''

# Read from input file
values = []
with open('input.txt', 'r') as f:
    for x in f:
        values.append(int(x.replace('\n','')))


# Logic TODO
