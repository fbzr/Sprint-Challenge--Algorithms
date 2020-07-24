'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # find the base case
    if len(word) < 2:
        return 0
    
    # if first char is 't' and second char is 'h'
    if word[0] == 't' and word[1] == 'h':
        # it means 'th' was found: add 1 and call function on the rest of the word
        return 1 + count_th(word[2:])
    
    # if 'th' was not found, check next char
    return count_th(word[1:])
