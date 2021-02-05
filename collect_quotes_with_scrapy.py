#!/usr/bin/python3
# -*- coding:utf8 -*-

import json
import random

"""
This file provides function to read data from files, process them and print out.
"""

def message(character, quote):
	""" Format a message """
	n_character = character.capitalize()
	n_quote = quote.capitalize()
	return '{} a dit : {}'.format(n_character, n_quote)


def read_values_from_json(path, key):
	""" This function returns a list of values read from a Json file. """
	values = []
	with open(path) as f:
		data = json.load(f)
		for entry in data:
			values.append(entry[key])
	return values

def clean_strings(sentences):
	""" Removes white spaces around sentences and returns them as a list. """
	cleaned_sentences = []
	for sentence in sentences:
		cleaned_sentences.append(sentence.strip())
	return cleaned_sentences

def get_random_item(items):
	""" Returns a random item from the item list. """
	position = random.randint(0, len(items) - 1)
	return items[position]

def random_value(source_path, key):
	""" Returns a random value from a Json file. """
	values = read_values_from_json(source_path, key)
	cleaned_values = clean_strings(values)
	return get_random_item(cleaned_values)


# QUOTES
def get_random_quote():
	""" Gather quotes from San Antonio """
	return random_value("quotes.json", "quote")


# CHARACTERS
def get_random_character():
	""" Gather character from wikipedia """
	return random_value("characters.json", "character")

# INTERACTION
def print_random_sentence():
	""" Print a random sentence """
	quote = get_random_quote()
	character = get_random_character()
	print(message(character, quote))

def main_loop():	
	running = True
	while running:
		print_random_sentence()
		user_choice = input('Tapez Entrée [Enter] pour voir une autre citation ou B pour quitter le programme ! ')
		if user_choice == 'B':
			running = False

#main_loop()
if __name__ == "__main__":
	main_loop

