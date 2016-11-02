import tweet_class as tc 
import pickle

f = open('twist.txt', 'r')
tweets_string = f.read()
tweets = tweets_string.split("}\n{")
tweet_list = []
for tweet in tweets:
	tweet_entry = tc.Tweet(tweet)
	if len(tweet_entry.hashtags)>=2:
		tweet_list.append(tweet_entry)
# for tweet in tweet_list:
# 	if len(tweet.hashtags)>=2:
# 		print(tweet.text)
# 		print(tweet.hashtags)
# 		print('__________________')
f.close()
f = open('tweets_picke','w')
pickle.dump(tweet_list,f)
f.close()
#print(truncateHashtag('hasth?sdad'))
