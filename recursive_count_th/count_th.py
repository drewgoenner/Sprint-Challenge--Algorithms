'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    # if the word is too short, return 0 (set base)
    if len(word) < 2:
    	return 0
    # if the first two letters are 'th', return 1 + recursive search at index to the
    if word[0] == 't' and word[1] == 'h':
    	return 1 + count_th(word[1:])
    # otherwise return recursive search at index to the right of 1
    else:
    	return count_th(word[1:])
    # return the count
    return(count_th)
    
    
    
    
