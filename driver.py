import all_func as af
filename = 'Output.txt'
tweet_list = []
af.extract_hash(filename,tweet_list)
print('1')
af.duplicate_remove(tweet_list,0.95)
print('2')
vocab,co_hash_matrix = af.co_hashtags(tweet_list)
print('3')

for word in vocab:
	print(word)
print(co_hash_matrix['trump']['trump'])