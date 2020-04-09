import pandas as pd
import threading
from flask import Flask
from flask import render_template, request, session,  redirect, url_for

app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.secret_key = 'goeqmo3infle@@$21wf3'


def save_on_exit(score, total):
    lock = threading.Lock()
    with lock:
        score_df = pd.read_csv('scores.csv')
        score_df = score_df.append({'Correct' : score,
                         'Total' : total}, ignore_index=True)

        score_df.to_csv('scores.csv', index=False)


@app.route("/test", methods=['POST', 'GET'])
def test():

    if request.method == 'POST':
        session['line_no'] += 1
        if session['line_no' ] % 50 == 0:
            df = pd.read_csv('lines.csv')
            df = df.sample(frac=1)
            lines = [line for line in df['Line']]
            chars = [char for char in df['Character']]
            session['count'] += 1
            session['chars'] = chars[50*(session['count']):50*(session['count'])+50]
            session['lines'] = lines[50*(session['count']):50*(session['count'])+50]
            session['line_no'] = 0

        pos = session['line_no']
        line = session['lines'][pos]
        answer = request.form['answer']
        if answer == session['chars'][session['line_no']-1]:
            session['score'] += 1

        return render_template('line.html', title='Home', line=line, line_no=session['line_no']+50*session['count'])

    else:
        pos = session['line_no']
        line = session['lines'][pos]
        return render_template('line.html', title='Home', line=line, score=session['score'])


@app.route("/")
def welcome():
    df = pd.read_csv('lines.csv')
    df = df.sample(frac=1)
    lines = [line for line in df['Line']]
    chars = [char for char in df['Character']]
    session['lines'] = lines[:50]
    session['chars'] = chars[:50]
    session['line_no'] = 0
    session['score'] = 0
    session['count'] = 0
    return redirect(url_for('test'))


@app.route('/shutdown', methods=['GET', 'POST'])
def shutdown():
    save_on_exit(session['score'], session['line_no'])
    return 'Your score was: '+str(session['score'])+'/'+str(session['line_no']+50*session['count'])+'!\n Thank you for participating!'


if __name__ == "__main__":
    app.run(debug=True)