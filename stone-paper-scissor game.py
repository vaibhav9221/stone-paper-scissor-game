import random
l=['s','p','c']
choice=10
human=0
computer=0
number_of_chances=0
print('stone paper scissor game')
print("s for stone,p for paper,c for scissor")
while number_of_chances<choice:
    n = input("enter a choice :")
    a = random.choice(l)
    if n==a:
        print('tie',n,a)
    elif n=='s' and a=='p':
        computer=computer+1

        print(f'you choice{n} and computer choice is {a}')
        print("you loss")
    elif n=='s'and a=='c':
        human+=1
        print(f'you choice {n} and computer choice is {a}')
        print('you win')


    elif n == 'p' and a == 's':
        human+=1

        print(f'you choice{n} and computer choice is {a}')
        print("you win")
    elif n == 'p' and a == 'c':
        computer= 1
        print(f'you choice {n} and computer choice is {a}')
        print('you lose')
    elif n == 'c' and a == 's':
        computer += 1

        print(f'you choice{n} and computer choice is {a}')
        print("you lose")
    elif n == 'c' and a == 'p':
        human += 1
        print(f'you choice {n} and computer choice is {a}')
        print('you win')
    else:
        print("enter a valid option")


    print(f'computer point is {computer} and human point is {human}')
    number_of_chances=number_of_chances+1
    print(f'{choice-number_of_chances} number_of chances left')
print("game over")
if human>computer:
    print("you win")
elif computer>human:
    print('you lose')
elif computer==human:
    print('tie')



