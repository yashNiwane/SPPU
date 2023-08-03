from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/fy')
def firstyear():
  return render_template("fy.html")

@app.route('/sy')
def secondYear():
  return render_template("sy.html")

@app.route('/ty')
def thirdYear():
  return render_template("ty.html")

@app.route('/be')
def fourthYear():
  return render_template("be.html")


if __name__ == '__main__':
    app.run(debug=True)