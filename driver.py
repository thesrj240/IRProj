import all_func as af
import os
filename = 'Output.txt'
tweet_list = []
af.extract_hash(filename,tweet_list)
af.duplicate_remove(tweet_list,0.95)
vocab,co_hash_matrix = af.co_hashtags(tweet_list)


numbered_vocab = []
count =1

for word in vocab:
	numbered_vocab.append([word,count])
	count +=1

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

os.system('gpmetis graph2 50')
f = open('graph2.part.50','r')
ourdickt = dict.fromkeys([])
st = f.read()
f.close()

num_list = st.split('\n')

linecount = 1
for num in num_list:
	if len(num)>0:
		if ourdickt.has_key(num):
			ourdickt[num].append(vocab[linecount-1])
			linecount+=1
		else:
			ourdickt[num] =[]
			ourdickt[num].append(vocab[linecount-1])
			linecount+=1
count = 1
for key in ourdickt:
	goo = ''
	for hashtag in ourdickt[key]:
		goo = goo + hashtag + ' ' + str(co_hash_matrix[hashtag][hashtag]) + ' '
	print(goo)
	print('\n_________________ {}\n'.format(count))
	count += 1
