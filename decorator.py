'''def my_fuction():
    print("i am a fuction")
description = my_fuction
print(description())'''


def outer_fuction():
    def inner_fuction():
        print("i am a fuction")
    inner_fuction()
    
outer_fuction()

