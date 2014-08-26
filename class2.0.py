# These are sample exercises from the Girl Develop It: Intro to Python course!
#
# Let's Develop It Exercise from Class 1 with some new concepts
# 
# Kaleigh Gerlich
# Version 0.0
# Updated 07/21/2014
# 
# Dessert Cart Program
# This program allows the user to pick any dessert (really, anything they want to eat) 
# and then queries the user for their beverage choice to go with the dessert.
#
dessert = raw_input('What is your favorite type of dessert?')
coffee = raw_input('Would you like coffee with that? (regular/decaf/no)')
if coffee == 'no':
	alt = raw_input('Would you like another beverage? (water/tea/alcohol/nothing)')
	if alt == 'water':
		print('Okay, Ill get you '+ dessert + ' with water!')
	elif alt == 'tea':
		tea_type = raw_input('We have two kinds of tea, green and black. What kind?')
		if tea_type == 'green':
			print('Okay, Ill get you '+ dessert +' with green tea!')
		elif tea_type == 'black':
			print('Okay, Ill get you '+ dessert +' with black tea!')
		else:
			print('Im sorry, we dont have that type of tea!')
	elif alt == 'alcohol':
		alc_type = raw_input('We have red wine, white wine, or beer. What kind?')
		if alc_type == 'red wine':
			print('Okay, Ill get you '+ dessert +' with red wine!')
		elif alc_type == 'white wine':
			print('Okay, Ill get you '+ dessert +' with white wine!')
		elif alc_type == 'beer':
			print('Okay, Ill get you '+ dessert +' with beer!')
		else:
			print('Im sorry, we dont have that type of alcohol')
	elif alt == 'nothing':
		print('Okay, Ill get you '+ dessert +' with nothing to drink!')
	else:
		print('Im sorry, we dont have that on the menu!')
else:
	print("Okay, I'll get you "+ dessert + " with "+coffee+" coffee!")


