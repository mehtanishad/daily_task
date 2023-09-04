def ispolindrume(s):
    return s ==s[::-1]

s = input("enter a string: ")
ans = ispolindrume(s)

if ans:
    print("yes")
else:
    print("no")
