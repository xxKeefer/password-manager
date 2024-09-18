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
                # for the amount of characters from the category we need to add
                for _ in range(self.per_category):
                    # add a random one
                    output.append(random.choice(uppers))

            if choice == 'Lowercase':
                lowers = list(string.ascii_lowercase)
                for _ in range(self.per_category):
                    output.append(random.choice(lowers))

            if choice == 'Numbers':
                digits = list(string.digits)
                for _ in range(self.per_category):
                    output.append(random.choice(digits))

            if choice == 'Symbols':
                symbols = list("!@#$%^&*")
                for _ in range(self.per_category):
                    output.append(random.choice(symbols))

        # shuffle the selected characters so the categories aren't all lined up
        random.shuffle(output)
        # trim the list to the desired length "[0:self.length]"
        # this cuts any extra characters because of rounding up self.per_category
        # join the trimmed list into a string and return
        return "".join(output[0:self.length])
