# Loop that increments more than 1
counter = 0
max = 20

while counter < max :
    counter += 2
    print(counter)
 
# Range    
custom_range = range(1,11)

while True :
    try:
        number = int(input("Choose a number between 1 and 10: "))

        if number not in custom_range :
            print("You have chosen a number outside of the range.")
        else :
            print(f"You have chosen number: {number}")
            break
    except ValueError:
        print("Enter a whole number.")


