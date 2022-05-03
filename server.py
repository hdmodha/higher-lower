from flask import Flask
import random
app = Flask(__name__)


@app.route("/")
def greet_user():
    return f"<h1>Guess a number between 0 and 9</h1>" \
           f"<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


a_random_number = random.randint(0, 9)

@app.route("/<int:user_input>")
def check_number(user_input):
    if user_input < a_random_number:
        return f"<h1 style='color: grey'>Number is too low</h1>" \
               f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"

    if user_input == a_random_number:
        return f"<h1 style='color: cyan'>You guessed it right!!!</h1>" \
               f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"

    if user_input > a_random_number:
        return f"<h1 style='color: red'>Number is too high</h1>" \
               "f<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
