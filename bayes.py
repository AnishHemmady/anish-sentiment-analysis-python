import nltk,time

from nltk.probability import FreqDist, ELEProbDist


from nltk.classify.util import apply_features,accuracy

import matplotlib.pyplot as plt
import re

#start replaceTwoOrMore
def unique_filter(str):
	l=str
	a=l.split()
	print(a)
	for k,v in enumerate(a[:-1]):
		if(v==a[k+1]):
			a[k+1]=a[k+1].replace(a[k+1]," ")
	print(a)
	b=" ".join(a)
	b=" ".join(b.split())
	return(b)
#end
#start process_tweet
def processTweet(tweet):
    # process the tweets
    
    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)    
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end 



def showchar(pos,neg,neu):
    labels='Positive','Negative','Neutral'
    sizes=[pos,neg,neu]
    colors=['gold','lightskyblue','lightcoral']
    explode=(0.1,0,0)
    plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)
    plt.axis('equal')
    plt.show()

#start getStopWordList
def getStopWordList(stopWordListFileName):
    #read the stopwords
    stopWords = []
    stopWords.append('AT_USER')
    stopWords.append('URL')
    '''print "---------------------------------------------------"
    time.sleep(10)
    print stopWords
    time.sleep(15)
    print "---------------------------------------------------"'''
    fp = open(stopWordListFileName, 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        #print "---------------------------------------------------"
        #time.sleep(10)
        #print word
        #time.sleep(15)
        #print "---------------------------------------------------"
        stopWords.append(word)
        #print "-----------stop------------"
        #time.sleep(3)
        #print stopWords
        #time.sleep(3)
        #print "-----------stop------------"
        #time.sleep(1)
        line = fp.readline()
    fp.close()
    return stopWords
#end

#start getfeatureVector
def getFeatureVector(tweet, stopWords):
    featureVector = []  
    words = tweet.split()
    #print "-------tweet--------"
    #time.sleep(10)
    #print words
    #time.sleep(5)
    #print"-----end tweet-------"
    for w in words:
        #replace two or more with two occurrences 
        w = replaceTwoOrMore(w) 
        #strip punctuation
        w = w.strip('\'"?,.')
        #print "-------tweet--------"
        #time.sleep(10)
        #print w
        #time.sleep(5)
        #print"-----end tweet-------"
        #check if it consists of only words
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*[a-zA-Z]+[a-zA-Z0-9]*$", w)
        #ignore if it is a stopWord
        if(w in stopWords or val is None):
            continue
            #print "-------tweet--------"
            #time.sleep(5)
            #print w
            #time.sleep(5)
            #print"-----end tweet-------"
        else:
            featureVector.append(w.lower())
            #print "-------tweet--------"
            #time.sleep(5)
            #print featureVector
            #time.sleep(5)
            #print"-----end tweet-------"
    return featureVector    
#end
    
 
tweets=[]
posfile=open('positive_tweets123.csv')
stopWords = getStopWordList('stopwords.txt')
count = 0;
featureList = []

for line in posfile.readlines():
	line=line.replace('positive,','positive|')
	line=line.replace('\n','')
	line=line.split('|')
    #tweet=line[1]
	#print line
	#time.sleep(2)
	words_filtered=[e.lower() for e in line[1].split() if len(e)>=3]
	tweet=line[1]
	processedTweet = processTweet(tweet)
	featureVector = getFeatureVector(processedTweet, stopWords)
	featureList.extend(featureVector)
	tweets.append((featureVector, line[0]));
	#tweets.append((words_filtered,line[0]))
#print tweets


posfile=open('negative_tweets124.csv')
for line in posfile.readlines():
	line=line.replace('negative,','negative|')
	line=line.replace('\n','')
	line=line.split('|')
	#print line
	#time.sleep(2)
	words_filtered=[e.lower() for e in line[1].split() if len(e)>=3]
	tweet=line[1]
	processedTweet = processTweet(tweet)
	featureVector = getFeatureVector(processedTweet, stopWords)
	featureList.extend(featureVector)
	tweets.append((featureVector, line[0]));
	#tweets.append((words_filtered,line[0]))
#print tweets

posfile=open('neutral_tweets.csv')
for line in posfile.readlines():
	line=line.replace('neutral,','neutral|')
	line=line.replace('\n','')
	line=line.split('|')
	#print len(line), line
	#print line
	#time.sleep(2)
	words_filtered=[e.lower() for e in line[1].split() if len(e)>=3]
	tweet=line[1]
	processedTweet = processTweet(tweet)
	featureVector = getFeatureVector(processedTweet, stopWords)
	featureList.extend(featureVector)
	tweets.append((featureVector, line[0]));
	#tweets.append((words_filtered,line[0]))
#print tweets

#word_features = get_word_features(get_words_in_tweets(tweets))
# Remove featureList duplicates
featureList = list(set(featureList))





#start extract_features
def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in featureList:
        features['contains(%s)' % word] = (word in tweet_words)
    return features
#end	
                       
 
training_set = apply_features(extract_features, tweets)

#test_training_set=apply_features(extract_features, test_tweets)
#test_training_set=extract_features(test_tweets)
print "-----------------------------------------------"
print(training_set)
print"------------------------"
#print(test_training_set)
print "-----------------------------------------------"

classifier = nltk.classify.NaiveBayesClassifier.train(training_set)
#print classifier
def graph():
    countpos=0
    countneg=0
    countneu=0
    fp = open('twitDB5.csv', 'r')
    for text in fp.readlines():
        value1= classifier.classify(extract_features(text.split()))
        if value1=="positive":
	        countpos=countpos+1
        elif value1=="negative":
	        countneg=countneg+1
        else:
	        countneu=countneu+1
	
showchar(countpos,countneg,countneu)