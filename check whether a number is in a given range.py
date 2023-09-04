def test_range(n):
    if n in range(1,15):
        print("% s number for inside of range: "%str(n))
    else:
        print("outside of the range: ")
        
n = int(input("enter a number: "))
print(test_range(n))
