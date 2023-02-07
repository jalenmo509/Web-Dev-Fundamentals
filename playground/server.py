from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def level1():
    return render_template('index.html')

@app.route('/play/<int:num>')
def play(num):
    return render_template('index2.html', num=num)

@app.route('/play/<int:num>/<color>')
def color(num,color):
    return render_template('index3.html', num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)