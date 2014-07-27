# These are sample exercises from the Girl Develop It: Intro to Python course!
#
# Let's Develop It Exercise for Class 2: write a program that obtains user input but
# does not exit until the user types "quit"
#
# Let's ask the user if they want to play or quit, then keep asking until they say 'quit'.
# 
guess = raw_input('Do you want to play or quit?')
while guess == 'play':
    print('yay!')
    guess = raw_input('Do you want to play or quit?')
