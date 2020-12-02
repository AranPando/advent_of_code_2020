'''
    A file called input.txt contains numbers on each line. 
    
    Boss: "SOLIDER! IT IS YOUR-"
    Me: "yes yes, I can read, thanks."
    Boss: NANI?!

'''

""" 
    split each line by spaces; #0 == range, #1 == letter, #2 == string
    strip separate letter, index values and string.
    Count++ if index-1 position contains the letter
    If count > 1, not valid
    example: "1-3 a: abcde"
"""


def check_validity(input_str):
    # sanitise and separate input
    vals = input_str.split(' ')
    letter = vals[1][0]
    clean_str = vals[2].strip()
    range = vals[0].split('-')
    i1 = int(range[0])-1
    i2 = int(range[1])-1

    # Count++ if a supplied index contains letter
    count = 0
    if clean_str[i1] == letter:
        count += 1
    if clean_str[i2] == letter:
        count += 1
    
    # Less than or more than 1 instance of the letter is invalid
    if count == 1:
        return True
    
    return False


if __name__ == "__main__":
    
    # print(check_validity("1-3 a: abcde"))
    
    # Read from input file
    count = 0
    with open('input.txt', 'r') as f:
        for x in f:
            if check_validity(x) == True:
                count += 1
    
    print(count)
