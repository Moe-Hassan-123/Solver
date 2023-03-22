from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """Returns a html with all available Lessons."""

    return render_template("index.html")


# Part 1 -> Select Subject and exercise, then Add answers.
# Part 2 -> Solve subject and exercise.
# Part 3 -> Edit Answers of a specified subject and exercise. # Last..

if __name__ == "__main__":
    app.run(debug=True)
