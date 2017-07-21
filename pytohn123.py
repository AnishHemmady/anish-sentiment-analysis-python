import flask, twitterhand
import postggr
app=flask.Flask(__name__)
app.debug=True 

@app.route('/')
def tweb():
	return flask.render_template('sentiment.html')

@app.route('/sentiment', methods=['GET','POST'])
def sentiment():
	return flask.render_template('sentiment.html')

@app.route('/pos007', methods=['GET','POST'])
def pos007():
	return flask.render_template('pos.html')
	
@app.route('/pos007/posg', methods=['GET','POST'])
def posg():
	return postggr.posg()

@app.route('/pos007/senti12', methods=['GET','POST'])
def senti12():
	return postggr.senti12()
	
@app.route('/pos007/pos', methods=['GET','POST'])
def pos():
	return postggr.pos()


def get_resource_as_string(name, charset='utf-8'):
    with app.open_resource(name) as f:
        return f.read().decode(charset)

app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string

@app.route('/SearchTweet',methods=['POST'])	
def searchtweet():
	tweet_string=flask.request.form['SEARCH_BOX']
	print tweet_string
	twitterhand.searchtweet(tweet_string)
	tweet=[]
	file=open('twitDB5.csv')
	for line in file.readlines():
		line=line.replace('\n','')
		tweet.append(line)
	file.close()
	return flask.render_template('results.html',tweets=tweet)
	#return  "Searching the tweet complete with filtering also done!!!!"	
if __name__=='__main__':
	app.run()