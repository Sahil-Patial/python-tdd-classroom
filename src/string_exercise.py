import re
class StringExercise:

    def __init__(self):
           # Do some initial setup in this constructor method, if needed
           pass

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        s = ""
        for i in input_str:
            s = i + s
        return s

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        if (character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u' or character == 'A' or character == 'E' or character == 'I' or character == 'O' or character == 'U'):
            return True
        else:
            return False

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        res = re.findall(r"\w+",sentence)
        n = max(res,key = lambda x : len(x))
        return n

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        text = text.split(' ')
        l=[]
        for words in text:
            l.append(len(words))
        return l

a = StringExercise()
a.reverse_string("sahil")
a.is_english_vowel("e")
a.find_longest_word("hello")
a.get_word_lengths("how are you")