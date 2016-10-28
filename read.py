#!/usr/bin/python

def number_hashtag(tweet):
    count =0
    tokens = tweet.split(" ")
    for token in tokens:
        #print(token)
        if len(token)>1 and token[0] == '#':
            count += 1
    return count
#ifile  = open('3.csv', "rb")
text_file = open("Output.txt", "r")
#reader = csv.reader(ifile)
s = text_file.read()
tweet_list = s.split("}\n{")
print len(tweet_list)
tweet_count = 0
for tweet in tweet_list:
    if number_hashtag(tweet) >=2 :
        tweet_count+=1
        print tweet
        print number_hashtag(tweet)
        print '--------------------'
print(tweet_count)
text_file.close()