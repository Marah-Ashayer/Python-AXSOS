from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'kekijnhjhbhbj' 

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter']=0
    else:
        session['counter']+=1
    return render_template("index.html")

@app.route('/count', methods=['POST'])
def  increament():
    if request.form['visit']=='add':
        session['counter']+=0
    elif request.form['visit']=='reset':
        session['counter']=-1
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)