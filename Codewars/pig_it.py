# Move the first letter of each word to the end of it,
# then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

# def pig_it(text):
#     lst = text.split()
#     return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])


def pig_it(text):
    words = text.split()
    return " ".join([("{0}{1}ay".format(i[1:], i[0]), i)[not i.isalpha()] for i in words])


print(pig_it("Quis custodiet ipsos custodes ?"))
