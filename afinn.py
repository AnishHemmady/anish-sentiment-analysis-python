#!/usr/bin/python 
#
# (originally entered at https://gist.github.com/1035399)
#
# License: GPLv3
#
# To download the AFINN word list do:
# wget http://www2.imm.dtu.dk/pubdb/views/edoc_download.php/6010/zip/imm6010.zip
# unzip imm6010.zip
#
# Note that for pedagogic reasons there is a UNICODE/UTF-8 error in the code.

import math
import re
import sys
reload(sys)
import time
import matplotlib.pyplot as plt
from pylab import*
sys.setdefaultencoding('utf-8')

# AFINN-111 is as of June 2011 the most recent version of AFINN
filenameAFINN = 'AFINN-111.txt'
afinn = dict(map(lambda (w, s): (w, int(s)), [ 
            ws.strip().split('\t') for ws in open(filenameAFINN) ]))

# Word splitter pattern
pattern_split = re.compile(r"\W+")

'''def showchar(pos,neg,neu):
	labels='Positive','Negative','Neutral'
	sizes=[pos,neg,neu]
	colors=['gold','lightskyblue','green']
	explode=(0.1,0.3,0)
	plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)
	plt.axis('equal')
	plt.show()
	plt.savefig('tweet_by_country123.png')'''


def sentiment(text):
    """
    Returns a float for sentiment strength based on the input text.
    Positive values are positive valence, negative value are negative valence. 
    """
    words = pattern_split.split(text.lower())
    sentiments = map(lambda word: afinn.get(word, 0), words)
    
    if sentiments:
        # How should you weight the individual word sentiments? 
        # You could do N, sqrt(N) or 1 for example. Here I use sqrt(N)
        sentiment = float(sum(sentiments))/math.sqrt(len(sentiments))
          
    else:
        sentiment = 0
    return sentiment




def affin_sent():
	countpos=0
	countneg=0
	countneu=0
	fp = open('3.csv', 'r')
	for text in fp.readlines():
		processedTweet=("%6.2f %s" %(sentiment(text),text))
		value1=sentiment(text)
		if value1>0:
			countpos=countpos+1
		elif value1<0:
			countneg=countneg+1
		else:
			countneu=countneu+1
	pos=arange(3)+.5
	barh(pos,(countpos,countneg,countneu),align='center',color='#b8ff5c')
	yticks(pos,('positive','negative','neutral'))
	xlabel('sentiment count')
	ylabel('sentiment')
	title('analysis dude')
	grid(True)
	plt.savefig('static/tweet.png', format='png')
	

	
