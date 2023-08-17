def number(lst1, lst2):
    result = False
    for i in lst1:
        for j in lst2:
            if i ==j:
                result = True
                return result

print(number([1,2,3,4,5],[5,6,7,8,9]))
print(number([1,2,3,4,5],[6,7,8,9]))



    








