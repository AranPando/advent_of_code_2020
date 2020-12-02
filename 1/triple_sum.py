'''
    A file called input.txt contains numbers on each line. 
    
    Boss: "SOLIDER! IT IS YOUR MISSION TO FIND THE TWO NUMBERS THAT SUM TO 2020
    AND THEN RETURN THEIR MULTIPLICATION!"
    Me: "NANI?! Didn't we just do this sir?"
    Boss: "... UH! I MEANT THE THREE NUMBERS!"
    Me: YES, OF COURSE! ...do you mind if-"
    Boss: "YES! ITS FINE ...as long as you don't do those finger things again... ugh"
    ME: "SIR YESSIR!" 

'''

# import file
values = []
with open('input.txt', 'r') as f:
    for x in f:
        values.append(int(x.replace('\n','')))

# print(values)

# Iterate through the array in a nested loop, such that you have two values and then search the arary for the third possible matching one.
end = False
for i in range(len(values)):
    x = values[i]
    for j in range(i,len(values)):
        y = values[j]
        matching = 2020 - x - y
        # print(x, y, matching)
        if matching in values[j:]: # since we only checking later values in the array, it won't have to check the existance of duplicates
            print(f"The numbers are: {x}, {y}, {matching}")
            print(f"The number is: {x*y*matching}")
            end = True
            break
    if end == True:
        break
        
            

print("End of program")

