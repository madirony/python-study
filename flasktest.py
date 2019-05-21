from flask import Flask, render_template, request, jsonify, pymongo
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/name/<name>')
def helloName(name):
    return 'Hello, %s!'%name

@app.route('/<int:number>')
def helloNumber(number):
    return"it's %d"%number

@app.route('/score')
def score():
    return render_template('score.html')

@app.route('/result',methods=['GET','POST'])
def result():
    if request.method == 'GET':
        return "It's GET"
    return render_template('result.html',result=request.form)
    

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)