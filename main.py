import inquirer.errors
import typer
import inquirer
from generator import Generator


def validate_length(_, current):
    if int(current) < 8:
        raise inquirer.errors.ValidationError(
            "Too short", reason="Your password will be too simple")
    elif int(current) > 26:
        raise inquirer.errors.ValidationError(
            "Too long", reason="Your password may be rejected for being to long in some cases")

    return True


def validate_categories(_, current):
    if len(current) < 1:
        raise inquirer.errors.ValidationError(
            "No Categories", reason="You must select at least one category")

    return True


def main():
    questions = [
        inquirer.Text(
            "length",
            message="How long should the password be? (8-26 characters)",
            validate=validate_length
        ),
        inquirer.Checkbox(
            "categories",
            message="What types of characters to include in the password?",
            choices=["Uppercase", "Lowercase", "Numbers", "Symbols"],
            default=["Uppercase", "Numbers"],
            validate=validate_categories
        ),
    ]

    answers = inquirer.prompt(questions)
    password = Generator(int(answers['length']), answers['categories'])
    print(password.generate())


if __name__ == "__main__":
    typer.run(main)
