import tweet_class as tc 
import hashlib
import pickle
import sets

def jaccard(set1,set2):
	return float(len(set1 & set2))/float(len(set1 | set2))

def extract_hash(filename,tweet_list):
	f = open(filename, 'r')
	tweets_string = f.read()
	tweets = tweets_string.split("}\n{")
	for tweet in tweets:
		tweet_entry = tc.Tweet(tweet)
		if len(tweet_entry.hashtags)>=2:
			tweet_list.append(tweet_entry)
	f.close()
	#return tweet_list

def duplicate_remove(tweet_list,tol):
	tweet_group = dict.fromkeys([])
	for tweet in tweet_list:
		hashstring = ''
		for hashtag in tweet.hashtags:
			hashstring = hashstring + '#' + hashtag
			
		
		hashvalue = hash(hashstring)
		if(tweet_group.has_key(hashvalue)):
			tweet_group[hashvalue].append(tweet)
		else:
			tweet_group[hashvalue] = []
			tweet_group[hashvalue].append(tweet)

	for hashvalue in tweet_group:
		tweets_of_group = []
		for tweet in tweet_group[hashvalue]:
			tweet.createBagOfWords()

		for tweet1 in tweet_group[hashvalue]:
			for tweet2 in tweet_group[hashvalue]:
				if tweet1!=tweet2 and jaccard(tweet1.bagOfWords,tweet2.bagOfWords) > tol:
					tweet_group[hashvalue].remove(tweet2)
	tweet_list = []
	for hashvalue in tweet_group:
		for tweet in tweet_group[hashvalue]:
			tweet_list.append(tweet)

	#return tweet_list

def co_hashtags(tweet_list):
	vocab = []
	unsorted_dict = dict.fromkeys([])
	for tweet in tweet_list:
		hashtags = tweet.hashtags
		for hashtag in hashtags:
			if not unsorted_dict.has_key(hashtag):
				unsorted_dict[hashtag] = []
				vocab.append(hashtag)
	vocab = sorted(vocab)
	#sorted_dict = sorted(unsorted_dict)
	for hashtag in unsorted_dict:
		unsorted_dict[hashtag] = dict.fromkeys([])
	for tweet in tweet_list:
		for hashtag in tweet.hashtags:
			for hashtag2 in tweet.hashtags:
				if unsorted_dict[hashtag].has_key(hashtag2):
					unsorted_dict[hashtag][hashtag2]+=1
				else:
					unsorted_dict[hashtag][hashtag2]=1

	return [vocab,unsorted_dict]