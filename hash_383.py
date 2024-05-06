ransomNote = "aa"
magazine = "aab"

def func(ransomNote, magazine):
    cn = 0
    for c in ransomNote:
        if c in magazine:
            magazine = magazine.replace(c, "", 1)
            cn += 1

    return cn == len(ransomNote)



res = func(ransomNote, magazine)
print(res)



