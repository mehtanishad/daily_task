d1 = {
    'name':'pankaj', 'age':20, 'study':12
    
    }

d2 = list(d1.keys())
d2.sort()
sorted_dict = {i: d1[i] for i in d2}
print(sorted_dict)
