import pickle
import tweet_class as tc 

unsorted_dict = dict.fromkeys([])

f = open('tweets_picke','rb')
vocab = []
tweet_list = pickle.load(f)
for tweet in tweet_list:
	hashtags = tweet.hashtags
	for hashtag in hashtags:
		if not unsorted_dict.has_key(hashtag):
			unsorted_dict[hashtag] = []
			vocab.append(hashtag)
vocab = sorted(vocab)
#sorted_dict = sorted(unsorted_dict)
for hashtag in unsorted_dict:
	unsorted_dict[hashtag] = dict.fromkeys(vocab,0)
for tweet in tweet_list:
	for hashtag in tweet.hashtags:
		for hashtag2 in tweet.hashtags:
			unsorted_dict[hashtag][hashtag2]+=1

for hashtag1 in vocab:
	for hashtag2 in vocab:
		if unsorted_dict[hashtag1][hashtag2]!=0:
			print(hashtag1,hashtag2,unsorted_dict[hashtag1][hashtag2])
f.close()