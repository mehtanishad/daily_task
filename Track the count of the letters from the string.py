from collections import defaultdict, Counter
str1 = 'w3resource' 
d1 = {}
for letter in str1:
    d1[letter] = d1.get(letter, 0) + 1
print(d1)
