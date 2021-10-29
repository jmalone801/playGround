from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def route1():
    return render_template("index.html")

@app.route('/play/<int:num>')
def route2(num):
    return render_template("index2.html", box=num)

@app.route('/play/<int:num>/<color>')
def route3(num, color):
    return render_template("index2.html", box=num, clr=color)

if __name__=="__main__":
    app.run(debug=True)