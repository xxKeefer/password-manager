import random
import string
import math
from abc import ABC, abstractmethod


class BaseGenerator(ABC):
    def __init__(self, length):
        super().__init__()
        self.length = length

    @abstractmethod
    def generate(self):
        pass


class PasswordGenerator(BaseGenerator):
    def __init__(self, length, categories):
        # Call the parent class constructor
        super().__init__(length)
        self.categories = categories
        # rounding this up so we get more instead of less characters
        # in the case of a fraction, and then cut characters later
        self.per_category = math.ceil(length / len(categories))
        # create a private dictionary of character lists to pick from
        self.__char_set = {
            "Uppercase": list(string.ascii_uppercase),
            "Lowercase": list(string.ascii_lowercase),
            "Numbers": list(string.digits),
            "Symbols": list('!@#$%^&*'),
        }
        # create a private list to add the selected characters too
        self.__characters = []

    def generate(self):
        # loop through each category the user selected
        for category in self.categories:
            # for the amount characters per category
            for _ in range(self.per_category):
                # add a random character from the set to the character list
                self.__characters.append(
                    random.choice(self.__char_set[category]))

        # shuffle the selected characters so the categories aren't all lined up
        random.shuffle(self.__characters)
        # trim the list to the desired length "[0:self.length]"
        # this cuts any extra characters because of rounding up self.per_category
        # join the trimmed list into a string and return
        return "".join(self.__characters[0:self.length])


class PassphraseGenerator(BaseGenerator):
    def __init__(self, length, wordlist=None):
        super().__init__(length)
        self.__phrase = []
        # Use a default wordlist if none is provided
        if wordlist is None:
            self.wordlist = [
                "apple", "banana", "cherry", "dog", "elephant", "frog", "giraffe",
                "house", "ice", "jungle", "kite", "lion", "mountain", "night",
                "ocean", "penguin", "queen", "river", "sun", "tree", "umbrella",
                "violet", "whale", "xylophone", "yellow", "zebra"
            ]
        else:
            self.wordlist = wordlist

    def generate(self):
        # Generate a passphrase by picking random words from the wordlist
        for _ in range(self.length):
            self.__phrase.append(random.choice(self.wordlist))

        return "-".join(self.__phrase)
