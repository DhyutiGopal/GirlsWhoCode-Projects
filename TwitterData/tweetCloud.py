# '''
# In this project, you will visualize the feelings and language used in a set of
# Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
# need!
# '''
from wordcloud import WordCloud
import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweetData.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()
filteredWords = {"us", "https"}
string = ""
for i in range(len(tweetData)):
    string = string + (tweetData[i]["text"])

# Continue your program below!
print(string)
# Textblob sample:
#tb = TextBlob(string)
# print(tb.polarity)
# filteredWords[word] = count
for a in string:
    print(a)
    if len(a) < 3:
        if a not in filteredWords:
            if(a.isalpha()) == True:
                wordcloud = WordCloud(max_font_size=40).generate(string)
string.isalpha()
wordcloud = WordCloud().generate(string)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
