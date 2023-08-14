l1=[]
ul=[]

for i in range(10):
    num=int(input("Enter number : "))
    l1.append(num)

print(l1)
for i in l1:
    if i not in ul:
        ul.append(i)


print("unique list : ",ul)
