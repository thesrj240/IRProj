import all_func as af
import os
import pickle
filename = 'all_tweets.txt'
tweet_list = []
print 'before functions'

freq_table_hashtags = dict.fromkeys([])
af.extract_hash(filename,tweet_list)
af.duplicate_remove(tweet_list,freq_table_hashtags,0.95)
print 'after duplicates'
vocab,co_hash_matrix = af.co_hashtags(tweet_list,freq_table_hashtags)
print 'before co_hashtags'
numbered_vocab = []
count =1

for word in vocab:
	numbered_vocab.append([word,count])
	count +=1

g = open('all_copickle2','w')
pickle.dump([vocab, numbered_vocab, co_hash_matrix, tweet_list],g)
g.close()



# f = open('graph2','w')
# e=0
# for hashtag1 in vocab:
# 	for hashtag2 in vocab:
# 		if co_hash_matrix[hashtag1].has_key(hashtag2) and not hashtag1==hashtag2:
# 			e+=1
# e = e/2
# print 'after cohash'
# f.write('{} {} 001\n'.format(len(vocab),e))

# for pair1 in numbered_vocab:
# 	for pair2 in numbered_vocab:
# 		hashtag1  = pair1[0]
# 		hashtag2 = pair2[0]
# 		pair2_num = pair2[1]
# 		if co_hash_matrix[hashtag1].has_key(hashtag2) and not hashtag1==hashtag2:
# 			f.write('{} {} '.format(pair2_num, co_hash_matrix[hashtag1][hashtag2]))
# 	f.write('\n')
# f.close()
# print 'before metis'

# os.system('gpmetis graph2 25')
# f = open('graph2.part.25','r')
# ourdickt = dict.fromkeys([])
# st = f.read()
# f.close()
# print 'after metis'
# num_list = st.split('\n')

# linecount = 1
# for num in num_list:
# 	if len(num)>0:
# 		if ourdickt.has_key(num):
# 			ourdickt[num].append(vocab[linecount-1])
# 			linecount+=1
# 		else:
# 			ourdickt[num] =[]
# 			ourdickt[num].append(vocab[linecount-1])
# 			linecount+=1
# count = 1
# for key in ourdickt:
# 	goo = ''
# 	for hashtag in ourdickt[key]:
# 		goo = goo + hashtag + ' ' + str(co_hash_matrix[hashtag][hashtag]) + ' '
# 	print(goo)
# 	print('\n_________________ {}\n'.format(count))
# 	count += 1
