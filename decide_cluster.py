import pickle
from sklearn.metrics.pairwise import cosine_similarity
import re
import all_func as af
def tokenizer_of_tweets(tweet_text):	################change this function in both places for '@'
	tweet_text = tweet_text.replace('\n',' ') 
	temp_list = tweet_text.split(' ')
	useful_list = []
	for ele in temp_list:
	    
	    if len(ele)<2 or ele.startswith('https://'):
	        continue
	    if ele.startswith('@') or ele.startswith('#'):
	    	ele = ele[1:]
	    useful_list.append(ele)
	    
	useful_text = " ".join(useful_list)
	tokens = re.split('[,.;?! ]',useful_text)
	real_tokens = []
	for token in tokens:
	    if len(token)>0:
	        real_tokens.append(token)
	return real_tokens

f = open('cluster_info_for_classification','r')
(cluster_list,vocab_tweet,vectorizer) = pickle.load(f)
f.close()
tweet = 'finally done with the project could not be happier'
#print(tokenizer_of_tweets(tweet))
#print(vectorizer.get_feature_names())
tweet_vector = vectorizer.transform([tweet])
#print(tweet_vector)

centroid_list = []
for cluster in cluster_list:
	centroid_list.append(cluster.centroid)
#print(centroid_list[0])
cosine_sim = []
for centroid in centroid_list:
	cosine_sim.append(cosine_similarity(tweet_vector,centroid)[0][0])
#print(cosine_sim)
max_cosine = max(cosine_sim)
max_cosine_index = cosine_sim.index(max_cosine)
for hashtag in cluster_list[max_cosine_index].hashtag_list:
	print(hashtag)


# print(len(tweet_vector.toarray()))
# print(vectorizer.vocabulary_.get('world'))

# print(len(tweet_vector_list[0].toarray()))
