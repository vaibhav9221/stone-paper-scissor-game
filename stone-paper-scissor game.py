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



#
#input == snake / water / gun only
#play a game with programmed computer
# x=input("")
# import random
# y=("snake","water","gun")
# z=random.choice(y)
# if x=="snake":
#     if z=="water":
#         print ("snake vs water" + "  Brave.U   Won")
#     elif z=="gun":
#         print ("snake vs gun" + " U lost.Better luck next time")
#     elif z=="snake":
#         print ("snake vs snake" + " \n DRAW")
# elif x=="water":
#     if z=="snake":
#         print ("water vs snake" + " U lost.Better luck next time")
#     elif z=="gun":
#         print ("water vs gun" +" Wow Mr.Cool.Won")
#     elif z=="water":
#         print ("gun vs gun " + "\n DRAW")
# elif x=="gun":
#     if z=="snake":
#         print ("gun vs snake" + "U won")
#     elif z=="water":
#         print ("gun vs water" + "Yeah superb.Won")
#     elif z=="gun":
#       print ("gun vs gun" + "\n DRAW")