from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []


@app.get("/")
def display_start():
    """Display survey start page template"""

    title = survey.title
    instructions = survey.instructions

    return render_template("survey_start.html", title=title,
                           instructions=instructions)



@app.post('/begin')
def display_question():
    '''redirect user to first question'''
    responses = []

    return redirect('/question/0')


@app.get('/question/<index>')
def display_single_question(index):
    '''display question with choices depending on index'''

    questions = survey.questions
    question = questions[int(index)]


    return render_template('question.html', question = question)



@app.post("/answer")
def get_response():
    '''append response from each question to responses list
    and redirect to next question'''

    answer = request.form["answer"]
    responses.append(answer)

    if len(responses) == len(survey.questions):

        redirect_page = '/completion'
    else:
        index = len(responses)
        redirect_page = f'/question/{index}'

    return redirect(redirect_page)


@app.get('/completion')
def show_completion():
    '''display thank you completion page'''

    return render_template('completion.html')
