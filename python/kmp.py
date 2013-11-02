def set_next(pattern):
    next = [0 for i in xrange(len(pattern)+1)]
    next[0] = -1
    i = 0
    j = -1
    while(i<len(pattern)-1):
        if (j == -1 or pattern[i] == pattern[j]):
            i += 1
            j += 1
            if pattern[i] != pattern[j]:
                next[i] = j
            else:
                next[i] = next[j]
        else:
            j = next[j]
    return next
def search(src, pan):
    next_val = set_next(pan)
    i = 0
    j = 0
    while (i < len(src) and j < len(pan)):
        if (j == -1 or src[i] == pan[j]):
            i += 1
            j += 1
        else:
            j = next_val[j]
    print i - len(pan) 
if __name__=='__main__':
    pattern = 'abab'
    src = 'aabcabcebafabcabceabcaefabcacdabcab'
    pan = 'abac'
    search(src, pan)
