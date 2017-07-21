#import regex
import re
import time
#import enchant

#start process_tweet
def processTweet(tweet):
    # process the tweets

    #Convert to lower case
    tweet = tweet.lower()
    #d = enchant.Dict("en_US")
    #d.check(tweet)
    #Convert www.* or https?://* to URL
    #tweet = re.sub('((www\.[\s]+)|(http?://[^\s]+))','URL',tweet,flags=re.DOTALL)
    #tweet=tweet.replace('http','')
    #tweet=tweet.replace('//','')
    #tweet=tweet.replace('\\','')
    #tweet=tweet.replace('//\\','')
    #tweet=tweet.replace('///','')
    #tweet=tweet.replace('\\\\','')
    #tweet=tweet.replace('://','')
    #if tweet.startswith('::\\')==True:
		#tweet = re.sub('[^0-9a-zA-Z]+', " ", tweet)
    result = re.sub(r"http\S+", "", tweet)
    result=" ".join(result.split())
    tweet=result
    b=['\\','http','/',':','//','\\\\','////','//\\']
    for char in b:
		tweet=tweet.replace(char,'')
    #lt=['::\\']
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #regex_url = 'http[^\s]*'
    #for url in re.findall(regex_url, tweet):
		#tweet = tweet.replace(url, '')
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    #tweet=tweet.encode('ascii',errors='ignore')
    tweet = tweet.strip('\'"') 
    #tweet=re.sub(r'([a-z])\1+', r'\1',tweet)
    tweet=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet).split())
    if tweet.startswith('rt'):
		tweet=tweet.replace(tweet,'')
    return tweet
#end

#Read the tweets one by one and process it
def preprocess():
	fp = open('twitDB4.csv', 'r')
	saveFile = open('twitDB5.csv','a')
	junkfile=open('junkDB.csv','a')
	for line in fp.readlines():
		#print line
		#time.sleep(3)
	#print line
		if (((line[0:3]=='::\\') or ('\\u' in line))):
			#print "*****************decode starts***********************"
			#line=line.decode('unicode_escape')
			#line=line.split('\\u')
			#print line
			#print "*****************decode ends***********************"
			#print line
			#time.sleep(3)
			junkfile.write(line)
			pass
		else:
			#print"*********************will process now******************************"
			#print line
			while line:
				processedTweet = processTweet(line)
				#print processedTweet
				saveThis = processedTweet
				saveFile.write('\n')
				saveFile.write(saveThis)
				line = fp.readline()
			#print "***********************proces ends *****************************"
	#end loop
	fp.close()
	saveFile.close()
	junkfile.close()
	f1=open('twitDB5.csv','r')
	f2=open('twitDB1000.csv','w')
	for line in f1.readlines():
		if line.strip() == '':
			continue
		f2.write(line)
	f1.close()
	f2.close()

	inFile = open('twitDB1000.csv','r')
	outFile = open('3.csv','w')

	listLines = []

	for line in inFile:

		if line in listLines:
			continue

		else:
			outFile.write(line)
			listLines.append(line)

	outFile.close()
	inFile.close()