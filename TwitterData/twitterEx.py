import json

f = open("tweetData.json", "r")
tweetData = json.load(f)
f.close()

#Print the id and text from the first tweet.
i = 0
while True:
    print(tweetData[i]["id"])
    print(tweetData[i]["text"])
    if i > (len(tweetData)-2):
        break
    i += 1

# for i in range(len(tweetData)):
#     print(tweetData[i]["id"])
#     print(tweetData[i]["text"])
# Does the same thing as while loop!

#for i in tweetData:
#     print(i["text"])
# Does the same thing as while loop!
