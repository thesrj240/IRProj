import pickle
import os
import hashtag_cluster_class as hcc
import tweet_class as tc
NUM_CLUSTER = 200
#Transfer
g = open('all_copickle2','r')
(vocab,numbered_vocab,co_hash_matrix,tweet_list) = pickle.load(g)
#print(vocab)
g.close()
f = open('graph22','w')
e=0
for hashtag1 in vocab:
	for hashtag2 in vocab:
		if co_hash_matrix[hashtag1].has_key(hashtag2) and not hashtag1==hashtag2:
			e+=1
e = e/2
f.write('{} {} 001\n'.format(len(vocab),e))

for pair1 in numbered_vocab:
	for pair2 in numbered_vocab:
		hashtag1  = pair1[0]
		hashtag2 = pair2[0]
		pair2_num = pair2[1]
		if co_hash_matrix[hashtag1].has_key(hashtag2) and not hashtag1==hashtag2:
			f.write('{} {} '.format(pair2_num, co_hash_matrix[hashtag1][hashtag2]))
	f.write('\n')
f.close()
os.system('gpmetis graph2 {}'.format(NUM_CLUSTER))
