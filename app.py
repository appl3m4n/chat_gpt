from flask import Flask, render_template, request

app = Flask (__name__)
@app.route ('/')
def index ():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    name = request.form['name']
    age = request.form['age']
    db = request.form ['dateofbirth']
    print(name)
    return render_template ('index.html', n=name, age=age, db=db)

if __name__ == '__main__':
    app.run (debug=True)