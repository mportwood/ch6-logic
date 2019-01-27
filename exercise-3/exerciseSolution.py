# This script contains a program for a simple guessing game!

# Define a function `print_hot_or_cold()` that takes in two arguments (the 
# `target` and the `guess`), and prints out an appropriate message based on 
# how close the guess is to the target:
#
# Distance    Message
# -------------------
# The same    "got it!"
# Within 1	  "scalding hot"
# Within 3	  "very warm"
# Within 5	  "warm"
# Within 8	  "cold"
# Within 13	  "very cold"
# > 13 away	  "icy freezing miserably cold"
#
# Be sure to consider both positive AND negative distances!
# BONUS: Also print out whether the guess is high or low
def print_hot_or_cold(target, guess): 
    dist = abs(target - guess)
    if dist == 0: #same number
        print("Got it!")
    elif dist <= 1: 
        print("Scalding Hot")
    #if distance >= 2 and distance <=3 #This works but there's a better way, change above to elif
    elif dist <= 3:  #You've already checked above
        print ("very warm")
    elif dist <= 5: 
        print("warm")
    elif dist <=8: 
        print("cold")
    elif dist <=13: 
        print("very cold")
    else:
        print("icy freezing miserably cold")

#at this point is does nothing...need to call function we created



# Define a function `guess_number()` that takes a single argument (a target number)
# and prompts the user for a guess using the `input()` method. Your function should
# then print how close the user's guess is to that target (use your previous 
# function!). Note that you will need to convert the input into a number.
#
# Once you have a single guess working, modify your function so that the user can
# make MULTIPLE guesses. You can either do this using a loop (see the next chapter)
# or by simply calling your `guess_number() method again IF the user didn't get
# the answer right. The later is an example of **recursion**.

def guess_number(target): 
    guess = int(input("Guess a number!"))
    print_hot_or_cold(target, guess)
    if guess != target: 
        guess_number(target)

# If the file is run as a top-level script, your script should pick a random number
# between 1 and 50 as the target and then start the game. You should inform the
# user of the range of numbers before asking them for a guess.

#_______Script v. Module________
# Write all functions at top and add this to bottom
##This part means only run if run from the command line

if __name__ == "__main__":
    #print_hot_or_cold(50, 49)
    #guess_number(50)
    import random 
    target = random.randint(1,50)
    print("Try guessing a random # from 1-50!")
    guess_number(target)

##__name__ is a special var that refers to the name of the script that is currently running
##not the name of the file (as a top level script)
## 39.55 on lecture 4
##This way others can import and run the cool functions you built
##This makes your code reusable. (so like the print...(12, 10) above won't run)
##imagine like if you created a package and tried to import it like "import math"