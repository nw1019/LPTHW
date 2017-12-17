# -*- coding: utf-8 -*-
# Basic imports for the game

from sys import exit
from random import randint
import start

# Setting Scenes, the parent class.
class Scene(object):

	def enter(self):
		exit(1)

# Subclass
class Fail(Scene):

# Create a list having various and answers.
	Antwort = [
		 
		 "Bye, at least you've tried.",
		

	]

	def enter(self):
		# Count the numbers of the answers and print the answers randomly.
		print Fail.Antwort[randint(0, len(self.Antwort)-1)]
		exit(1)

class Room(Scene):

	def enter(self):

		print "You wake up and find out you are being locked in a room."
		print "You're panic and can't remember what happened to you. You look around the room and hoping there is a way out... "
		print "There is a small window, a locked door,a paper clip, a shovel and also a poster on the wall..."
		print "Maybe there is way out but you have to plan carefully otherwise it will be dangerous... "
		print "------------------------------------------ "
		print "You start trying any possible ways to get out of the room safely. "
		print "Now,you need to choose which is the best way to escape... "
		print "------------------------------------------ "
		print "1. 'Use the paper clip to open the locked door "
		print "2. 'Use the shovel to break the window "
		print "3. 'Use the shovel to dig a tunnel through the wall and hide it with the use of poster"

		action = raw_input("input number >  ")

		if action == "1":

			print "You can open the door!!"

			print "But there is another locked door with PIN."

			return 'PIN'

		elif  action == "2":

			print "You break the window and climb out. But there is a lake full of piranha. You don't have choice but to jump. You died."
			return 'Fail'

		elif  action == "3":

			print "You finally dig a tunnel out of the room!!"

			print "But there is another locked door with PIN."

			return 'PIN'

		else:
			print "Invalid input!"

			quit(1)


class PIN(Scene):

	def enter(self):

		print "You have to guess what is the PIN now."

		print "2 _ 6\n3 5 7\n1 3 5 "

		print "Just 1 digit is missing"

		pin = "%d" % (randint(1,9))

		guess = raw_input("[keypad]> ")

		guesses = 1

		while guess != pin and guesses < 7:
							print "You have tried %d time" % guesses
							guesses += 1
							guess = raw_input("[keypad]> ")

		if guess == pin:
			print "What a genius!"

			print "You finally get out and find out..."

			return 'Gambling'



		elif guess == "4":

			print "That just proves that you have nice logical mind."

			print "Not bad~ Keep trying!"

			return 'PIN'

		else:

			print "You failed to guess the right number."

			print "Auto defense system is activated. Electric shock!!! You died!"

			return 'Fail'


class Gambling(Scene):

	def enter(self):
		print "You finally get out and find out there is a fat guy sitting in front of a gambling table waiting for you."

		print "Fat guy: Well done.I didn't expect you can get out of the room."
		print "Fat guy: However, you have to win me on the Blackjack(Twenty-one) in order to get out of here."
		print "Fat guy: Betting who will holds the bigger card at the end. Now you know that the dealer has 'J' and 'Six'. "
		
		print "To win,you need to have over 17 points and under 21 points in total"

		# Create two lists to the represent the all the poker cards and refers each other.
		cards = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7:"Seven",

		8:"Eight", 9: "Nine", 10: "Ten", 11: "J", 12: "Q", 13:"K"}
		cards2 = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five" : 5, "Six" : 6, "Seven" : 7,
		
"Eight" : 8, "Nine" : 9, "Ten" : 10, "J" : 11, "Q" : 12, "K" : 13}


		# Take two cards randomly
		
		FirstCard = cards[randint(1,13)]
		NextCard = cards[randint(1,13)]



		FirstCardEQ = cards2[FirstCard]

		NextCardEQ = cards2[NextCard]

		total =  FirstCardEQ + NextCardEQ

		NewTotal = total + randint(1,13)


		print "You have %s and %s, total: %d" % (FirstCard, NextCard, total)


		# List all the situations might encounter for the game Twenty-One.
	
		if total >= 21:
			print "The total is more than  21 points, you lost"

			return'Reverse'


		if total > 17 and total <= 21:
		   print "You finally win and can get out of the room !"
		   print "Congratulation!"
		   quit(1)




		while  total <= 17:
			print " 'Continue' or 'Open' ?"
			action = raw_input(">  ")

			if action == "Continue":
				total = total + randint(1,13)
				print "Add one more card, now you have %d points" % total


				if total > 17 and total < 21:
					print "You finally win and can get out of the room !"
					print "Freedom is here!!"
					quit(1)



				elif total > 21:
					print "The total is more than 21 points, you lost"
					return'Reverse'

			if action == "Open" and total <= 17:

				print "Now you have %d points is less than 17" % total

				print "Such a loser, Bye"

				return 'Reverse'

			elif action == "Open":

				print "Are you stupid?"

				return 'Reverse'

			else:
				print "Please input correct instruction"


class Reverse(Scene):

	def enter(self):

		print "You play tricks on the card and reverse the result without the fat guy's notice."
		print "Just typing the following strings backwards:"
		print "-" * 15
		print "CIGAM"
		print "-" * 15

		action = raw_input("> ")

		if action == "MAGIC":
			print "Amazing!"
			return 'Gambling'

		else:
			print "No hope"
			return 'Fail'

class Map(object):
# create a Map class connect different scenes with a list of words
	scenes = {
	'Room':  Room(),
	'PIN': PIN(),
	'Gambling':Gambling(),
	'Reverse': Reverse(),
	'Fail': Fail(),
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)




a_map = Map('Room')
a_game = start.Start(a_map)
a_game.play()

