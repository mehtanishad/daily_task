import random
def game_win(comp, you):
    if comp == you:
        return none
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
print("comp turn:snake(s), water(w) or gun(g)?")
randno = random.randint(1,3)
if randno == 1:
    comp = 's'
    
elif randno == 2:
    comp = 'w'
elif randno == 2:
    comp = 'g'
you = input("your turn: snake(s) water(w) or gun(g)")
a = game_win(comp, you)

print(f"computer chose {comp}")
print(f"computer chose {you}")

if a == none:
    print("the game is tie")
elif a:
    print("you win")
else:
    print("you loos")
    


















        
