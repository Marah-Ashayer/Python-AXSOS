from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def index():
    return render_template("index.html")	

@app.route('/play/<int:num_of_boxes>')
def index_1(num_of_boxes):
    return render_template("index.html", times=num_of_boxes)

@app.route('/play/<int:num_of_boxes>/<color>')
def index_2(num_of_boxes,color):
    return render_template("index.html", times=num_of_boxes,color=color)



if __name__=="__main__":
    app.run(debug=True)

