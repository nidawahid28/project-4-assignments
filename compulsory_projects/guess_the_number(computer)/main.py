import random

print("Welcome to the Number Guessing Game!")

low = 1
high = 10

print("Think of a number between 1 and 10. The computer will guess it.")

if low <= high:
    guess = random.randint(low, high)
    print(f"Computer guessed: {guess}")
    
    while True:
        feedback = input("Is the guess too high (H), too low (L), or correct (C)? ").strip().upper()
        
        if feedback == 'C':
            print("Yay! The computer guessed your number correctly.")
            break
        elif feedback == 'H':
            high = guess - 1
        elif feedback == 'L':
            low = guess + 1
        else:
            print("Invalid input. Please enter H, L, or C.")
            continue

        if low > high:
            print("The number is out of range based on your hints. Please try again.")
            break

        guess = random.randint(low, high)
        print(f"Computer guessed: {guess}")

             
  