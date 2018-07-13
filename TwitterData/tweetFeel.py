# '''
# In this project, you will visualize the feelings and language used in a set of
# Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
# need!
# '''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweetData.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!

# Textblob sample:

totalPolarity = []
totalSubjectivity = []
for i in tweetData:
    tb = TextBlob(i["text"])
    polarity = tb.polarity
    print(i["text"])
    subjectivity = tb.subjectivity
    totalPolarity.append(polarity)
    totalSubjectivity.append(subjectivity)

averageP = sum(totalPolarity) /len(totalPolarity)
averageS = sum(totalSubjectivity)/ len(totalSubjectivity)

plt.hist(totalPolarity, bins= [0, 0.25, 0.5, 0.75, 1])
plt.title("Polarity Histogram")
plt.xlabel("Polarity")
plt.ylabel("Frequency")
plt.axis([-1, 1, 0, len(totalPolarity)])
plt.grid(True)
plt.show()

plt.hist(totalSubjectivity, bins= [-1,-0.75,-0.5,-0.25, 0, 0.25, 0.5, 0.75, 1])
plt.title("Subjectivity Histogram")
plt.xlabel("Subjectivity")
plt.ylabel("Frequency")
plt.axis([-1, 1, 0, len(totalSubjectivity)])
plt.grid(True)
plt.show()
