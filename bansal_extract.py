import pickle
f = open('cohash_pickle','r')
bansal = pickle.load(f)
vocab = bansal[0] #List of all our hashtags sorted
dictionary = bansal[1] #dictionary[hash1][hash2] give co-occurence of hash2
f.close()

# for hashtag1 in vocab:
# 	for hashtag2 in vocab:
# 		if dictionary[hashtag1].has_key(hashtag2) and dictionary[hashtag1][hashtag2]>10: #This condition is necessary in case hash1 and hash2 have never occurred together.
# 			print(hashtag1,hashtag2,dictionary[hashtag1][hashtag2])

list_ = []
for hashtag1 in vocab:
	
	list_.append([hashtag1,dictionary[hashtag1][hashtag1]])

sorted_list = sorted(list_,key= lambda x: x[1], reverse = True)
for element in sorted_list:
	print(element[0],element[1])