import random

def create_random():
    return random.randint(1,10)

def guess_number():
    guess_cout = 0
    system_number=create_random()
    while True:
        user_number = int(input("please enter yoyr number :"))
        guess_cout +=1

        if (user_number == system_number):
            print("your gusses is True")
            break   
    print(f"the number of your gusses :{guess_cout}")

guess_number()

