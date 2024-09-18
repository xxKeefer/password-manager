import random
import string
import math


class Generator:
    def __init__(self, length, categories):
        self.length = length
        self.categories = categories
        self.per_category = math.ceil(length / len(categories))

    def generate(self):
        output = []

        for choice in self.categories:
            if choice == 'Uppercase':
                uppers = list(string.ascii_uppercase)
                uppers_selected = random.sample(uppers, self.per_category)
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

        random.shuffle(output)

        return "".join(output[0:self.length])
