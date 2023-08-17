l = [("x", 1),("x",2),("x",5),("k",6)]
d = {}
for a,b in l:
    d.setdefault(a,[]).append(b)
print(d)
