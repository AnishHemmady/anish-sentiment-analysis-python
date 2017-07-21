
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import pu
import sys
#import afinn
import bayes
from tweepy.api import API
#from threading import Thread
ckey='n3rpppqxjgcjuSRu7wac8Xnxs'
csecret='pPZNa07HS0dpfMXBlAYs5PYgF864X6JliYnIpfCYDMXyLlRTf3'
atoken='1290722437-muRPwE5R25pjRELZ8AVwM73tEVE9UCZ5BTOOrSr'
asecret='vHhx7LKPIRsGbJtG1IiMyfFIal3rKUyS22rW2HPCaTyuy'
tweetcount=1

# python c:\Python27\twitterhand.py
class listener(StreamListener):
	def __init__(self, api=None):
		self.api = api or API()
		self.n = 0
		self.m = 250
	def on_data(self,data):
		#try:
			#print data
		global tweetcount
		global saveFile
		#tweetcount+=1
		self.n = self.n+1
		if self.n < self.m:
			tweetcount+=1
			tweet = data.split(',"text":"')[1].split('","source')[0]
			print str(tweetcount ) + ":"+ tweet		#str(time.time())+
			saveThis = '::'+tweet
			saveFile = open('twitDB4.csv','a')
			saveFile.write('\n')
			saveFile.write(saveThis)
			return True
		else:
			saveFile.close()
			pu.preprocess()
			bayes2.hello()
			return False
			
	def on_error(self,status):
		print status
		
auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth, listener())
#twitterStream.filter(track=["car"])
def searchtweet(string):
	#print string
	twitterStream.filter(track=[string])





	




