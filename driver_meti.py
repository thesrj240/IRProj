import pickle
import os
import hashtag_cluster_class as hcc
import tweet_class as tc
import re
from sklearn.feature_extraction.text import TfidfVectorizer
#Transfer
def tokenizer_of_tweets(tweet_text): 
    temp_list = tweet_text.split(' ')
    useful_list = []
    for ele in temp_list:
        
        if len(ele)<2 or ele.startswith('https://') or ele.startswith('@') or ele.startswith('#'):
            continue
        useful_list.append(ele)
        
    useful_text = " ".join(useful_list)
    tokens = re.split('[,.;?! ]',useful_text)
    real_tokens = []
    for token in tokens:
        if len(token)>0:
            real_tokens.append(token)
    return real_tokens



NUM_CLUSTER = 25

g = open('copickle','r')
(vocab,numbered_vocab,co_hash_matrix,tweet_list) = pickle.load(g)
#print(vocab)
g.close()
f = open('graph2','w')
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
print 'before metis'

os.system('gpmetis graph2 {}'.format(NUM_CLUSTER))
f = open('graph2.part.{}'.format(NUM_CLUSTER),'r')
ourdickt = dict.fromkeys([])
st = f.read()
f.close()
print 'after metis'
num_list = st.split('\n')
cluster_list=[]
for i in range(NUM_CLUSTER):
	cluster_list.append(hcc.Hashtag_cluster_class(i))

linecount = 1
for num in num_list:
	if len(num)>0:
		cluster_list[int(num)].add_hashtag(vocab[linecount-1])
		linecount+=1

vectorizer = TfidfVectorizer(min_df=1,tokenizer=tokenizer_of_tweets, stop_words=None)
tweet_text_list = []
for tweet in tweet_list:
	tweet_text_list.append(tweet.text)
tweet_vector_list = vectorizer.fit_transform(tweet_text_list)
vocab_tweet = vectorizer.get_feature_names()

count = 0
for tweet in tweet_list:
	encountered_cluster = []
	for hashtag in tweet.hashtags:
		if hashtag in vocab:
			i = vocab.index(hashtag)
		cluster_id = int(num_list[i])
		if not cluster_id in encountered_cluster:
			cluster_list[cluster_id].tweet_list.append(count)
			encountered_cluster.append(cluster_id)
	count = count + 1
for cluster in cluster_list:
	print(cluster.cluster_id)
	print(cluster.hashtag_list)
	for tweet_index in cluster.tweet_list:
		print(tweet_list[tweet_index].hashtags)
	break




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

