import random
import sys

option = int(input("Now what would you like to do?\n1 - Hit\n2 - Stand\n3 - Quit\n"))
y = random.randrange(1,11)
z =  random.randrange(1,11)
w = y + z
while 1:
    if option == 1:
        if w > 21:
            print("You busted sorry!")
            print(w)
            sys.exit()    
        else:
            print("Your new card has a value of"  .format(y))
            print("And your current score is:" .format(w))
            break    
    elif option == 2:
        print ("You chosen to stand with a score of" .format(z))
        break
    elif option == 3:
        print("Thanks playing!  Goodbye....")
        sys.exit()
    else:
        print("You must enter 1, 2, 3")
        break
print("Now let is see what the dealer has...")
dealer1 = random.randrange(1,11)
dealer2 = random.randrange(1,12)
dealer3 = random.randrange(1,11)
a = dealer1 + dealer2
b = dealer3 + a
print("The dealer is first card has a value of" .format(dealer1))
print("The dealer is second card has a value of" .format(dealer2))
print("The dealer is current total is" .format(a))
while 1:
    if a <= 16:
        print("The dealer hits...")
        if b > 21:
            print("The dealer has busted, you win!!")
            sys.exit()
        else:
            print("The dealer has a total of" .format(b))
            break
    else:
        print("The dealer stands with" .format(a))
        
while w < 22 and b < 22:
    if b > w:
        print("The dealer is the winner")
        sys.exit()
    elif b == 21:
        print("The dealer got 21 and is the winner")
        sys.exit()
    elif w == 21:
        print("You got 21 and are the winner!! w00t!")
        sys.exit()
    else:
        print("You are the winner!")
        sys.exit()
