from collections import counter
d1 = {"k1":100,'k2':200,'k3':20}
d2={'k3':90,'k4':80}
d = counter(d1)+counter(d2)
print(d)
