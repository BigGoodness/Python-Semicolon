number = int(input("enter a number: "))

for number in range(20):

    if number % 2 == 0:
        break
    print("The number is: ", number)
