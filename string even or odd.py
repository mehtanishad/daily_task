def count(str):
     upper_ctr, lower_ctr, number_ctr, special_ctr = 0, 0, 0, 0
     for i in range(len(str)):
          if str[i] >= 'A' and str[i] <= 'Z': upper_ctr += 1
          elif str[i] >= 'a' and str[i] <= 'z': lower_ctr += 1
          elif str[i] >= '0' and str[i] <= '9': number_ctr += 1
          else : special_ctr += 1
     return upper_ctr, lower_ctr, number_ctr, special_ctr

def is_even(num):
    return num % 2 == 0

str = "@Hello Ahmedabad2222"
u, l, n, s = count(str)

print('\nUpper case characters:', u)
print('Lower case characters:', l)
print('Number case:', n)
print('Special case characters:', s)

if is_even(n):
    print('Number count is even.')
else:
    print('Number count is odd.')
