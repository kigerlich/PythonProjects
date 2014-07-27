# These are sample exercises from the Girl Develop It: Intro to Python course!
#
# Let's Develop It Exercise for class 2: write a program that asks the user to 
# guess a number in a range. The program should prompt the user when they are 
# too high or too low. The computer will need to have a random number for the u
# user to guess. 
#
# First, let's import the randint function from the random module
from random import randint
# The computer will generate a random number between 1 and 10
random_number = randint(1,10)
# Now we will ask the user to guess a number in the range
guess = raw_input('Im thinking of a number between 1 and 10. Guess a number!')
# We need to convert the input string into an integer
guess_int = int(guess)
# Now let's go through the possibilities for answers
while guess_int > random_number:
	print('Your guess is too high.')
	guess = raw_input('Im thinking of a number between 1 and 10. Guess a number!')
	guess_int = int(guess)

while guess_int < random_number:
	print('Your guess is too low.')
	guess = raw_input('Im thinking of a number between 1 and 10. Guess a number!')
	guess_int = int(guess)

while guess_int == random_number:
	print('You guessed right!')
	break






