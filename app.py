from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []


@app.get("/begin")
def display_survey():
    """Display survey start template"""
    title = survey.title
    instructions = survey.instructions

    # turning survey questions into dictionary
    # questions = {}
    # index = 0
    # for question in survey.questions:
    #     questions[index] = question.question
    #     index += 1

    questions = []
    for question in survey.questions:
        questions.append(question)
    print (questions)

    return render_template("survey_start.html", title=title,
                           instructions=instructions, questions=questions)
