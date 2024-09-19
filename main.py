import inquirer.errors
import typer
import inquirer
from generator import PasswordGenerator, PassphraseGenerator


# validation for the length question, current is the answer the user gave in the terminal
def validate_password_length(_, current):
    if int(current) < 5:
      # inquirer.errors.ValidationError is a pretty error that doesn't crash the program
        raise inquirer.errors.ValidationError(
            "Too short", reason="Your password will be too simple")
    elif int(current) > 128:
      # inquirer.errors.ValidationError is a pretty error that doesn't crash the program
        raise inquirer.errors.ValidationError(
            "Too long", reason="Your password does not need to be longer the 128 characters")

    return True


# validation for the categories question, current is the answer the user gave in the terminal
def validate_categories(_, current):
    if len(current) < 1:
      # inquirer.errors.ValidationError is a pretty error that doesn't crash the program
        raise inquirer.errors.ValidationError(
            "No Categories", reason="You must select at least one category")

    return True


def validate_passphrase_length(_, current):
    if int(current) < 2:
        raise inquirer.errors.ValidationError(
            "Too Few", reason="A passphrase need to be at least two words")
    elif int(current) > 10:
        raise inquirer.errors.ValidationError(
            "Too Many", reason="Let's not go crazy")

    return True


def make_password():
    # make a list of questions to ask in the terminal
    questions = [
        # question one
        inquirer.Text(
            "length",
            message="How long should the password be? (5-128 characters)",
            # this validation function we defined above
            validate=validate_password_length
        ),
        # question two
        inquirer.Checkbox(
            "categories",
            message="What types of characters to include in the password?",
            choices=["Uppercase", "Lowercase", "Numbers", "Symbols"],
            default=["Uppercase", "Numbers"],
            # this validation function we defined above
            validate=validate_categories
        ),
    ]

    # inquirer.prompt iterates of the questions list and asks them in turn
    # and re asks a question if it's answer does not pass validation
    answers = inquirer.prompt(questions)
    password = PasswordGenerator(int(answers['length']), answers['categories'])
    print(password.generate())


def make_passphrase():
    questions = [
        inquirer.Text(
            "length",
            message="How long should the passphrase be? (2-10 words)",
            validate=validate_passphrase_length
        ),

    ]
    answers = inquirer.prompt(questions)
    passphrase = PassphraseGenerator(int(answers['length']))
    print(passphrase.generate())


def main():
    kind = [
        inquirer.List(
            "kind",
            message="What kind of password would you like?",
            choices=["Password", "Passphrase"]
        ),

    ]
    choice = inquirer.prompt(kind)

    if choice['kind'] == "Password":
        make_password()
    else:
        make_passphrase()


if __name__ == "__main__":
    typer.run(main)
