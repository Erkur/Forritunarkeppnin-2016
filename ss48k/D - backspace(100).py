incorrect_word = str(input(""))
correct_word=[]
for letter in incorrect_word:
    if letter == "<":
        correct_word.pop()
    else:
        correct_word.append(letter)
print (''.join(correct_word))
