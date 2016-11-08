import pickle
f = open('copickle','r')
(vocab, numbered_vocab, dictionary, tweet_list) = pickle.load(f)
f.close()

# for hashtag1 in vocab:
# 	for hashtag2 in vocab:
# 		if dictionary[hashtag1].has_key(hashtag2) and dictionary[hashtag1][hashtag2]>10: #This condition is necessary in case hash1 and hash2 have never occurred together.
# 			print(hashtag1,hashtag2,dictionary[hashtag1][hashtag2])

for hashtag1 in vocab:
	for hashtag2 in vocab:
		if dictionary[hashtag1].has_key(hashtag2): #This condition is necessary in case hash1 and hash2 have never occurred together.
			print(hashtag1,hashtag2,dictionary[hashtag1][hashtag2])