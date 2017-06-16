word_list=[]
wrong_list = []
number_of_letters = []
guess_list = []
#Imports numPy
import numpy

#Words
list = ['hello','test','computer']
word = numpy.random.choice(list)
print word

#Make word into list
for letter in word:
    word_list.append(letter)
print word_list

def print_hangman(wrong_list):
    if len(wrong_list) == 0:
        print "    ______"
        print "   /      \ "
        print "   |       "
        print "   |"
        print "   |"
        print "   |"
        print "   |"
        print "   |"
        print "   |"
        print "___|_____________________"
    elif len(wrong_list) == 1:
        print "    ______"
        print "   /      \ "
        print "   |      0"
        print "   |"
        print "   |"
        print "   |"
        print "   |"
        print "   |"
        print "   |"
        print "___|_____________________"
    elif len(wrong_list) == 2:
        print "    ______"
        print "   /      \ "
        print "   |      0"
        print "   |      |"
        print "   |      |"
        print "   |"
        print "   |"
        print "   |"
        print "   |"
        print "___|_____________________"
    elif len(wrong_list) == 3:
        print "    ______"
        print "   /      \ "
        print "   |      0"
        print "   |     /|"
        print "   |    / |"
        print "   | "
        print "   |"
        print "   |"
        print "   |"
        print "___|_____________________"
    elif len(wrong_list) == 4:
        print "    ______"
        print "   /      \ "
        print "   |      0"
        print "   |     /|\ "
        print "   |    / | \ "
        print "   | "
        print "   |"
        print "   |"
        print "   |"
        print "___|_____________________"
    elif len(wrong_list) == 5:
        print "    ______"
        print "   /      \ "
        print "   |      0"
        print "   |     /|\ "
        print "   |    / | \ "
        print "   |     /"
        print "   |    /"
        print "   |"
        print "   |"
        print "___|_____________________"
    elif len(wrong_list) == 6:
        print "    ______"
        print "   /      \ "
        print "   |      0"
        print "   |     /|\ "
        print "   |    / | \ "
        print "   |     / \ "
        print "   |    /   \ "
        print "   |"
        print "   |"
        print "___|_____________________"
        print "The word was " + word +". Thanks for playing!"

print print_hangman(wrong_list)

for b in word:
    number_of_letters.append("_")
print ' '.join(number_of_letters)s

while set(number_of_letters) != set(word_list) and len(wrong_list) <= 5:
    guess = raw_input("Please enter a letter: ")
    print guess
    if guess in word_list:
        print print_hangman(wrong_list)
        print "Correct!"
        for index, letter in enumerate(word_list):
            if letter == guess:
                number_of_letters[index] = guess
        print ' '.join(number_of_letters)
    else:
        wrong_list.append(guess)
        print print_hangman(wrong_list)
        print "Wrong"
        print ' '.join(number_of_letters)