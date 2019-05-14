from flask import Flask, render_template, request, jsonify
import pymongo

app = Flask(__name__)


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/books',methods=['GET','POST'])
def books():
	if request.method == 'GET':
		mongo_url = 'mongodb+srv://madmongo:wldms97@cluster0-jay67.mongodb.net/test?retryWrites=true'
		client = pymongo.MongoClient(mongo_url)
		db =pymongo.database.Database(client, 'Cluster0')
		LibLib=pymongo.collection.Collection(db,'LibLib')
		book = LibLib.find()
		return render_template('books.html', result=book)

	if request.method == "POST":
		mongo_url = 'mongodb+srv://madmongo:wldms97@cluster0-jay67.mongodb.net/test?retryWrites=true'
		client = pymongo.MongoClient(mongo_url)
		db =pymongo.database.Database(client, 'Cluster0')
		LibLib=pymongo.collection.Collection(db,'LibLib')
		LibLib.insert_one(request.form.to_dict(flat='true'))
		book = LibLib.find()
		return render_template('books.html', result=book)

if __name__=='__main__':
	app.run(host='0.0.0.0',port=5000)