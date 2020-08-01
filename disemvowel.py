def disemvowel(string):
    # Function that remove the vowel
    vowel = ('a', 'e', 'i', 'o', 'u')
    for i in range(0, 5):
        string = string.replace(vowel[i], '')
    return string

print(disemvowel('This website is for losers LOL'))
