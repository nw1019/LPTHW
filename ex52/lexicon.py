# Allow different forms of user input (Capital, no punctuation and no space among words).
def clasify(userinput):

		if userinput in ['shoot!','SHOOT', 'shoot', 'SHOOT!', 'Shoot!']:
			return 'shoot!'

		elif userinput in ['dodge!','DODGE', 'Dodge', 'DODGE!', 'Dodge!']:
			return 'dodge!'

		elif userinput in ['tell a joke','TELL A JOKE', 'Tell a joke', 'Tell A Joke', 'Tellajoke', 'tellajoke', 'TELLAJOKE']:
			return 'tell a joke'

		elif userinput in ['throw the bomb','THROW THE BOMB', 'Throw the bomb', 'Throw The Bomb', 'Throwthebomb', 'throwthebomb', 'THROWTHEBOMB']:
			return 'throw the bomb'

		elif userinput in ['slowly place the bomb','SLOWLY PLACE THE BOMB', 'Slowly place the bomb', 'Slowly Place The Bomb', 'SlowlyPlaceTheBomb','SLOWLYPLACETHEBOMB']:
			return 'slowly place the bomb'

		else:
			return userinput
