import random  
def number_guessing():  
    print("hello this is number guessing game")
    print("choose the number between 1 to 100")
    target_number=random.randint(1,100)
    attempt=10
    print(f"you have only {attempt} to guess the number")
    for attempt in range(1,attempt+1):
        try:
            guess=int(input(f"attempt{attempt}:guess the number:"))
            if(guess<target_number):
                print("too small!wrong guess")
            elif(guess>target_number):
                print("too big!wrong guess")
            else:
                print(f"congratulations!!,you guessed the{target_number}in{attempt}attempts")
                break
        except ValueError:
            print("pls enter the valid number")
        if attempt==attempt:
            print(f"you are out of attempts! the number was{target_number}.")
            break 
number_guessing()
