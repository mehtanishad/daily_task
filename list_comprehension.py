fruits = ["apple", "mango", "banana", "kiwi"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)


fruits = ["apple", "mango", "banana", "kiwi"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
