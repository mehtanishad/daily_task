
list1 = [100, 75, 100, 20, 75, 12, 75, 25] 

lst = set(list1) 
print("The unique elements of the input list using set(): ") 
list_res = (list(lst))
 
for item in list_res: 
    print(item)


list1 = [100, 75, 100, 20, 75, 12, 75, 25]
unique_list =[]
for i in list1 :
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)
