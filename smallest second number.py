list1 = []
n = int(input("enter a number: "))
for i in range(1,n+1):
    ele=int(input("enter a element: "))
    list1.append(ele)
list1.sort()
print("sorted list: ", list1)
print("smalest list: ", list1[1] )
