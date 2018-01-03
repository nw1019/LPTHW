from nose.tools import *
import lexicon

def test_input():
	assert_equal(lexicon.clasify('SHOOT'), 'shoot!')
	assert_equal(lexicon.clasify('DODGE!'), 'dodge!')
	assert_equal(lexicon.clasify('TELL A JOKE'), 'tell a joke')
	assert_equal(lexicon.clasify('Throw the bomb'), 'throw the bomb')
	assert_equal(lexicon.clasify('SLOWLY PLACE THE BOMB'), 'slowly place the bomb')
