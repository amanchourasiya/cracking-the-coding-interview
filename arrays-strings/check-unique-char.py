def checkUnique(s):
    checker = 0
    for i in s:
        val = ord(i) - ord('a')
        if checker & (1 << val) > 0:
            return False
        checker |= 1 << val
    return True


print(checkUnique('abcde'))
print(checkUnique('abca'))

'''
Basic logic is to keep filling all the bits in checker of already read chars and match if those same bits are set again
'''