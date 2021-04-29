# This project makes up the 5th lesson in CodeCademy's Python 2 course. I've made some slight adjustments but overall things are very basic. 

# This program takes a string and translates it to Pig Latin
# Very little processing is done on the input string, so this doesn't work for phrases or strings

# suffix
pyg = 'ay'

# Apparently there are security issues with 'input()', so CodeCademy suggests raw_input() instead.
original = raw_input('Enter a word: ')

# Checks for empty, alphabetic string
if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]

  new_word = word + " " + first + pyg
  new_word = new_word[1:len(new_word)]
  print new_word
else:
  print 'cannot convert input to Pig Latin'
