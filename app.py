from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)




@app.get("/")
def display_start():
    """Display survey start page template"""
    session["responses"] = []
    return render_template("survey_start.html", survey = survey)



@app.post('/begin')
def display_question():
    '''redirect user to first question'''

    return redirect('/question/0')


@app.get('/question/<int:index>')
def display_single_question(index):
    '''display question with choices depending on index'''

    questions = survey.questions

    if index != len(session["responses"]):
        index = len(session["responses"])
        return redirect(f'/question/{index}')
    else:
        question = questions[index]
        return render_template('question.html', question = question)



@app.post("/answer")
def get_response():
    '''append response from each question to responses list
    and redirect to next question'''

    answer = request.form["answer"]

    responses = session["responses"]
    responses.append(answer)
    session["responses"] = responses

    if len(session["responses"]) == len(survey.questions):

        redirect_page = '/completion'
    else:
        index = len(session["responses"])
        redirect_page = f'/question/{index}'

    return redirect(redirect_page)


@app.get('/completion')
def show_completion():
    '''display thank you completion page'''

    return render_template('completion.html')

# redirect to completion or question/index
