import inquirer.errors
import typer
import inquirer
from generator import Generator


# validation for the length question, current is the answer the user gave in the terminal
def validate_length(_, current):
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


def main():
    # make a list of questions to ask in the terminal
    questions = [
        # question one
        inquirer.Text(
            "length",
            message="How long should the password be? (5-128 characters)",
            # this validation function we defined above
            validate=validate_length
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
    password = Generator(int(answers['length']), answers['categories'])
    print(password.generate())


if __name__ == "__main__":
    typer.run(main)
