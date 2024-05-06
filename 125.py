def isPalindrome(s):
    s = ''.join(filter(str.isalnum, s))
    s = s.lower()

    for i, char in enumerate(s[0:len(s)//2]):
        if not char == s[-(i+1)]:
            return False
    return True


# s = "A man, a plan, a canal: Panama"
s = "race a car"
res = isPalindrome(s)
print(res)
