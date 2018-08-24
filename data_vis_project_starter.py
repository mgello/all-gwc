'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''


import json
from textblob import TextBlob
import matplotlib.pyplot as plt

tweetFile = open("tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

tb = TextBlob("i love mangoes")
print(tb.polarity)

#for idx in range(len(tweetData)):
    #print("Tweet text: " + tweetData[idx]["text"])
#for tweet in tweetData:
#print("Tweet text: " + tweet["text"])

polarity = []
subList = []

for tweet in tweetData:
    tweetblob = TextBlob(tweet["text"])
    polarity.append(tweetblob.polarity)
    subList.append(tweetblob.polarity)

avg = sum(polarity + subList)/len(polarity + subList)


print(avg)
#print(polarity)
#print(subList)


plt.hist(polarity, bins=[ -0.50, -0.25, 0.0, 0.25, 0.50, 0.75, 1, 1.25, 1.50, 2])
plt.xlabel('Values')
plt.ylabel('Number of Items')
plt.title('Histogram of Numbers')
plt.axis([-1.1, 1.1, 0, 12000])
plt.grid(True)
plt.show()
