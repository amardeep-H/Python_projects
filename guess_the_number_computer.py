import random 

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int (input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again , its too low. ")
        elif guess > random_number:
            print("Sorry , guess again , its too high. ")
    
    print(f"Yeah, congratulations, You have guessed the number {random_number} correctly!")
    
guess(100)