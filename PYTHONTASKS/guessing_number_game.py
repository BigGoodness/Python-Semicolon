number = 50
number_guessed = 0

while number_guessed != 50:
    number_guessed = int(input("Guess a number: "));
       
    if number_guessed > number:
        print("the guessed number is too high")
    elif number_guessed < number: 
        print("the guessed number is too low")
    elif number_guessed == number:        
        print("the guessed number is just right")








