# ------------------------ IMPORTS ------------------------
from flask import Flask

# ----------------------- VARIABLES -----------------------

starting_gif = "https://media.giphy.com/media/gnFXgKBmLJXxe/giphy.gif"
low_answer = "https://media.giphy.com/media/ajeAXAu2Pkx6U/giphy.gif"
high_answer = "https://media.giphy.com/media/3otPowzRBqAi3h9uM0/giphy.gif"
good_answer = "https://media.giphy.com/media/ymkUFbGgt3loA/giphy.gif"

good_guess = 6


# ----------------------- DECORATOR -----------------------
def highlow_decorator(decorated_function):
    def highlow_wrapper(**kwargs):
        guess = kwargs["number"]
        print(guess)

        if guess < good_guess:
            print(f"The guess was {guess}")
            return "<h1 style='color:crimson'>Too Low!!</h1>" \
                   "<p></p>"\
                   + f"<img src={low_answer} width=600>"
        elif guess > good_guess:
            print(f"The guess was {guess}")
            return "<h1 style='color:crimson'>Too High!!</h1>" \
                   "<p></p>"\
                   + f"<img src={high_answer} width=600>"
        elif guess == good_guess:
            print(f"The guess was {guess}")
            return "<h1 style='color:crimson'>You've got it right!!</h1>" \
                   "<p></p>"\
                   + f"<img src={good_answer} width=600>"
    return highlow_wrapper


# ---------------------- FLASK SETUP ----------------------
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1 style='color:crimson'>🍔 Hello! 😎</h1>" \
           "<p>Let's play a pulp-fiction-based guessing game.</p>" \
           "<p>I'm thinking about a number between 0 and 10, type in the number in the link field!<p>" \
           "<p><b>Hint:</b> It's based on the password for the most important object in the entire movie! 💼" \
           "<p></p>" \
           f"<img src={starting_gif} width=600>"


@app.route("/<int:number>")
@highlow_decorator
def guess_the_number(number):
    return f"Your number is {number}"


# ------------------- RUNNING THE SERVER ------------------

if __name__ == "__main__":
    app.run(debug=True)

