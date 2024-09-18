import random
import string
import math


class Generator:
    def __init__(self, length, categories):
        self.length = length
        self.categories = categories
        # rounding this up so we get more instead of less characters
        # in the case of a fraction, and then cut characters later
        self.per_category = math.ceil(length / len(categories))

    def generate(self):
        # create a list to add the selected characters too
        output = []

        # loop through each category the user selected
        for choice in self.categories:
            if choice == 'Uppercase':
                # create a list of characters for the category
                uppers = list(string.ascii_uppercase)
                # select a random subset of the character
                uppers_selected = random.sample(uppers, self.per_category)
                # add them to the list
                output.extend(uppers_selected)

            if choice == 'Lowercase':
                lowers = list(string.ascii_lowercase)
                lowers_selected = random.sample(lowers, self.per_category)
                output.extend(lowers_selected)

            if choice == 'Numbers':
                digits = list(string.digits)
                digits_selected = random.sample(digits, self.per_category)
                output.extend(digits_selected)

            if choice == 'Symbols':
                symbols = list("!@#$%^&*?")
                symbols_selected = random.sample(
                    symbols, self.per_category)
                output.extend(symbols_selected)

        # shuffle the selected characters so the categories aren't all lined up
        random.shuffle(output)
        # trim the list to the desired length "[0:self.length]"
        # this cuts any extra characters because of rounding up self.per_category
        # join the trimmed list into a string and return
        return "".join(output[0:self.length])
