from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/dojo")
def doj():
    return "Dojo"

@app.route("/say/<name>")
def greet(name):
    return f"Hi {name}"

@app.route("/repeat/<num>/<text>")
def repeat(num,text):
    return  f"  {text }"*int(num)  

if(__name__)=="__main__":
    app.run(debug=True)