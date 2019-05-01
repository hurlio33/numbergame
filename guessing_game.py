"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
For this first project we will be using Workspaces. 
NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.
"""

import random
    
attempts = (0)


def start_game():        
    print("Welcome to the game. Guess a number between 1-10.")
    answer = random.randint(1, 10)
    guess = int(input("Guess a number: "))   

    while guess:      
        global attempts
        attempts += 1

        try:
            if guess > answer:
                print("It's lower")            
                guess = int(input("Guess a new number: "))
                continue
            elif guess < answer:
                print("It's higher")
                guess = int(input("Guess a new number: "))
                continue
            else: 
                print("Got it")
                print("It took you {} attempts".format(attempts))  
                break
    
        except ValueError:
                print("Guess must be a number between 1-10")
                           
        except TypeError:
                print("Guess must be a number between 1-10")
                

                
                        
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
    

