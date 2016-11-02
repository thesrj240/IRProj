import tweet_class as tc 
import hashlib
import pickle
import sets

def jaccard(set1,set2):
	return float(len(set1 & set2))/float(len(set1 | set2))

f = open('tweets_picke','rb')
tweet_group = dict.fromkeys([])
tweet_list = pickle.load(f)
f.close()

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
print(len(tweet_list))
print(len(tweet_group))
final_tweets = 0
for hashvalue in tweet_group:
	#print(len(tweet_group[hashvalue]))
	# if len(tweet_group[hashvalue])>1 and len(tweet_group[hashvalue])<50:
	# 	for tweet in tweet_group[hashvalue]:
	# 		print(tweet.text)
	# 		print(tweet.hashtags)
	# 		print('---------------------')
	# 	print('_____________________')
	tweets_of_group = []
	for tweet in tweet_group[hashvalue]:
		tweet.createBagOfWords()

	for tweet1 in tweet_group[hashvalue]:
		for tweet2 in tweet_group[hashvalue]:
			if tweet1!=tweet2 and jaccard(tweet1.bagOfWords,tweet2.bagOfWords) > 0.95:
				tweet_group[hashvalue].remove(tweet2)
				# print(tweet1.text)
				# print(tweet2.text)
				# print('____________')
	#print(len(tweet_group[hashvalue]))
	final_tweets = final_tweets + len(tweet_group[hashvalue])
print(final_tweets)
# for hashvalue in tweet_group:
# 	print(len(tweet_group[hashvalue]))
# 	if len(tweet_group[hashvalue])>1 and len(tweet_group[hashvalue])<50:
# 		for tweet in tweet_group[hashvalue]:
# 			print(tweet.text)
# 			print(tweet.hashtags)
# 			print('---------------------')
# 		print('_____________________')

