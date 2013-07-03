def first(word):
	return word[0]

def last(word):
	# print word[-1]
	return word[-1]

def middle(word):
	print word[1:-1]
	
	return word[1:-1]

middle('no')

def is_palindrome(word):
	first_letter = word[0]
	last_letter = word[-1]
	middle_word = word[1: -1]
	inverse_middle = word[-2: 0: -1]

	if first_letter == last_letter:
		if middle_word == inverse_middle:
			print True
			return True
	else:
		print False
		return False

is_palindrome("Becca")