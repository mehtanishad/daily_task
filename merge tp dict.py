d1 = {"k1":100,'k2':200,'k3':20}

d2={'k3':90,'k4':80}

#  ans = {"k1":100,'k2':200,'k3':110,'k4':80}
d = d1.copy()
d.update(d2)
print(d)

