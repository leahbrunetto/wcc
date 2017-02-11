import random

# Get the user's guess
# Params: None
# Returns: Integer
#
def get_guess():

    # Get initial guess
    guess = raw_input('Enter your guess: ')

    # Assume it's not valid, until it's proven otherwise
    valid = False

    while valid != True:

        try:
            # Try and convert this number to an integer
            # If it fails, the exception will occur
            guess = int(guess)
        except Exception:
            # Exception was thrown when trying to convert to number,
            # Report the issue and ask again
            print('Invalid input; please enter a whole number.')
            valid = False
            guess = get_guess()

        # If they get here, it means the number must have been valid
        # Set valid to be true to break out of the while loop
        valid = True

    return guess

#
#
#
def play(min, max):

    # Pick a secret number
    secret_number = random.randint(min, max)

    # When building your program, the following line will tell you what
    # the secret_number is; this will make it easier to test the game.
    # When done, remove or comment-out this line.
    #print('TEMPORARY DEBUGGING HELPER -> The secret number is: ' + str(secret_number))

    # Print message at the start the game
    print("\nI'm thinking of a number between " + str(min) + " and " + str(max) + " what do you think it is?")


    # Get the player initial guess
    guess = get_guess()

    # Initialize the total number of guesses available
    counter = 4
    
    for guess_count in range(0,4):
        if counter < 1:
            break
        else:
            results = 0
            if guess > secret_number:
                results = 'high'
            elif guess < secret_number:
                results = 'low'
            else:
                break
            print('Too ' + results + '. You have ' + str(counter) + ' guesses left.\n')
            guess = get_guess()
            counter -=1
    
    if (guess == secret_number):
        print('You got it! The number was ' + str(secret_number) + '.')
    else:
        print('Sorry, you ran out of guesses. The correct number was ' + str(secret_number) + '.')
    
play(10, 50)


        