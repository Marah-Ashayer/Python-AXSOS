from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html",a=8,b=8 ,color1='red',color2='black')	

@app.route('/play/<int:x>')
def index_1(x):
    return render_template("index.html",a=8 , b=x,color1='red',color2='black')

@app.route('/play/<int:x>/<int:y>/<color1>/<color2>')
def index_2(x,y,color1,color2):
    return render_template("index.html",a=x,b=y,color1=color1,color2=color2)

if __name__=="__main__":
    app.run(debug=True)