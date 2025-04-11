#imports for another function
import os
import time
from math import floor

#make a function that adds a delay before printing each character
def specPrint(text, spd=0.03, nl=False): #called the spd just in case we want to change it later on, also called nl just in case we want a new line later on
	for character in text:
		print(character, end="", flush=True) #prints each character one by one, flush is necessary as if its False it will just print it normally, flush enables it to be seen getting printed one by one
		time.sleep(spd) #an interval the same as the spd at top, this is necessary so it wont print the characters instantly
	if(nl): #this is in case we want it to print a new line
 		print("") 

#make a function that produces a loading animation at the start
def animatedCenter(text):
	#functions that will get the terminal size and setup the necessary animation variables
	center = os.get_terminal_size().columns
	arrows = 1
	duration = 6
	max_arrows = 3

	#main animation loop (while loop)
	while duration > 0:
		space = floor(center / 2) - (floor(len(text) / 2) + 1 + max_arrows)
		spacer = " " * space

		#functions for the animation of arrows going to the center (appearing)
		print(spacer + f"{('>' * arrows) + ' ' * (max_arrows - arrows)} {text} {' ' * (max_arrows - arrows) + ('<' * arrows)}" + spacer, end="\033[H", flush=True)
		time.sleep(0.1)
		duration -= 0.1
		arrows += 1

		#if loop for the animation that makes the arrows disappear
		if arrows > max_arrows:
			spaces_that_eats_the_arrows = 0
			arrows = max_arrows

			time.sleep(0.3)
			duration -= 0.3
			
			while arrows != 0: 
				spaces_that_eats_the_arrows += 1
				arrows -= 1
				print(spacer + f"{(' ' * spaces_that_eats_the_arrows) + '>' * arrows} {text} {'<' * arrows + ' ' * spaces_that_eats_the_arrows}" + spacer, end="\033[H", flush=True)
				time.sleep(0.1)
				duration -= 0.1

			time.sleep(0.3)
			duration -= 0.3
			
	#clears the terminal once the animation has finished
	print("\033[H\033[J", end="")
  
#make a function
# make a function
def createQuiz(filename):
	animatedCenter("loading...")
	with open(filename, "a") as f:
		choices = ["a", "b", "c", "d"]
		while True:
			specPrint('Enter a question (type "stop" to finish): ')
			question = input()
			if question.lower() == "stop":
				break

			answers = {}
			correct = ""
			for choice in choices:
				ans = input()
				is_correct = input().lower()
				answers[choice] = ans
				if is_correct == "y":
					correct = choice

			#animated file-writing style print
			index = 0
			while index < len(question):
				print(f"{filename} < {question[index:]}")
				index += 1
				time.sleep(0.1)
				
			# write to file
			f.write(f"Question: {question}\n")
			for key in choices:
				f.write(f"{key}) {answers[key]}\n")
			f.write(f"Correct answer: {correct}\n\n")

#run
createQuiz("quiz.txt")
