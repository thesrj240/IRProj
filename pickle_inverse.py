import tweet_class as tc 
import pickle
f = open('tweets_picke','rb')
tweet_list = pickle.load(f)
for tweet in tweet_list:
	print(tweet.text)
	print(tweet.hashtags)
	print('___________________')
f.close()