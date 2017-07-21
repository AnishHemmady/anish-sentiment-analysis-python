import flask, postg
app=flask.Flask(__name__)
app.debug=True 

@app.route('/')
def tweb():
	return flask.render_template('pos.html')

@app.route('/pos', methods=['GET','POST'])
def pos():
	return flask.render_template('pos.html')

def get_resource_as_string(name, charset='utf-8'):
    with app.open_resource(name) as f:
        return f.read().decode(charset)

@app.route('/senti12', methods=['GET','POST'])
def senti12():
	return flask.render_template('sentiment.html')
	
@app.route('/senti12/searchtweet', methods=['GET','POST'])
def searchtweet():
	return flask.render_template('pytohn123.py')

app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string

@app.route('/posg',methods=['POST'])	
def posg():
	tweet_string=flask.request.form['SEARCH_BOX']
	print tweet_string
	a,b,c=postg.search_pos(tweet_string)
	list=[]
	list=postg.senti_pos()
	return flask.render_template('pos.html',recs=a,recs1=c,recs2=b,recs3=list)
if __name__=='__main__':
	app.run()
