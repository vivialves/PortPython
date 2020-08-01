""" A function that takes in a string of one or more words, and returns the same string,
but with all five or more letter words reversed. """

"""
def spin_words(sentence):
    # sentence = input('Report a sentence: ')
    words = sentence.split(" ")
    new_sentence = []
    for word in words:
        if (len(word)) >= 5:
            new_sentence.append(word[::-1])
        else:
            new_sentence.append(word)
    new_sentence_string = ' '.join(new_sentence)
    return new_sentence_string


print(spin_words('testing'))

"""