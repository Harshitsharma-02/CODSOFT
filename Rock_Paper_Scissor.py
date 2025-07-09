import random
print("1: Rock \n2: Paper \n3: Scissor")
n=int(input("Enter Your Choice: "))
rand_no=random.randint(1,3)
if(n>=1 and n<=3):
    if(n==1 and rand_no==3):
        print("You Win!")
        print("Computer Choose: Scissor")
    elif(n==2 and rand_no==1):
        print("Computer Choose: Rock")
        print("You Win!")
    elif(n==3 and rand_no==2):
        print("Computer Choose: Paper")
        print("You Win!")
    elif(n==1 and rand_no==1 or n==2 and rand_no==2 or n==3 and rand_no==3):
        print("Draw")
    else:
        if(rand_no==1):
            print("Computer Choose: Rock")
        elif(rand_no==2):
            print("Computer Choose: Paper")
        elif(rand_no==3):
            print("Computer Choose: Scissor")
        print("You Lose!")
else:
    print("Invalid Input")