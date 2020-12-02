'''
    A file called input.txt contains numbers on each line. 
    
    Boss: "SOLIDER! IT IS YOUR-"
    Me: "yes yes, I can read, thanks."
    Boss: NANI?!

'''

# Logic
# split each line by spaces; #0 == range, #1 == lettter, #2 == string
# strip separate letter, range values and string.
# using count method on string, check if character in range
# example: "1-3 a: abcde"
def check_validity(input_str):
    vals = input_str.split(' ')
    letter = vals[1][0]
    clean_str = vals[2].strip()
    min_max = vals[0].split('-')
    mini = int(min_max[0])
    maxa = int(min_max[1])
    # print(mini, maxa)
    ltr_cnt = clean_str.count(letter)
    # print(ltr_cnt)

    if ltr_cnt >= mini and ltr_cnt <= maxa:
        return True
    return False


if __name__ == "__main__":
    
    # # Read from input file
    count = 0
    with open('input.txt', 'r') as f:
        for x in f:
            if check_validity(x) == True:
                count += 1
    
    print(count)
