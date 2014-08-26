# These are sample exercises from the Girl Develop It: Intro to Python course!
#
# Let's Develop It Exercise for class 3: To Do List
#
# First we define an empty list
to_do_list = []

# Now we can add things to our to do list!
def add_item():
	item = raw_input('What do you need to do?')
	to_do_list.append(item)

# If they finish something on the to do list, we can delete the item
def delete_item():
	print(to_do_list)
	del_item = raw_input('Here is your list. What have you finished?')
	to_do_list.delitem(del_item)
	print(to_do_list)

# Now we can print the list
	print(to_do_list)

# call the add_item function
add_item()

# ask if they have something else to add to the list
another = raw_input('Have something else to put on your to do list? (Y/N)')
while another == 'Y':
	add_item()
	another = raw_input('Have something else to put on your to do list? (Y/N)')

# ask if they finished anything on the list
finished = raw_input('Did you finish something on your to do list? (Y/N)')
while another == 'Y':
	delete_item()
	finished = inished = raw_input('Did you finish something on your to do list? (Y/N)')


