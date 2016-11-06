import pickle
import os
import hashtag_cluster_class as hcc
import tweet_class as tc
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import all_func as af
NUM_CLUSTER = 103
#Transfer
def tokenizer_of_tweets(tweet_text):
	tweet_text = tweet_text.replace('\n',' ') 
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


g = open('copickle','r')
(vocab,numbered_vocab,co_hash_matrix,tweet_list) = pickle.load(g)
#print(vocab)
g.close()



f = open('graph2.part.{}'.format(NUM_CLUSTER),'r')
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
tweet_vector_list = vectorizer.fit_transform(tweet_text_list) #tweet vectors
vocab_tweet = vectorizer.get_feature_names() #vocabalary  for tweet classfication

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
	cluster.centroid = 0
	for tweet_id in cluster.tweet_list:
		cluster.centroid = cluster.centroid + tweet_vector_list[tweet_id]
	cluster.centroid = cluster.centroid/float(len(cluster.tweet_list))



f = open('cluster_info_for_classification','w')
pickle.dump([cluster_list,vocab_tweet,vectorizer],f)
f.close()
