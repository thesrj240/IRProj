import sets
class Tweet:
	def __init__(self,tweet):
		self.text = tweet
		self.hashtags = self.extractHashtag(tweet)


	def truncateHashtag(self,hashtag):
		hashtag2 = ""
		for ch in hashtag:
			if (ch.isalnum()):
				hashtag2 = hashtag2+ch
			else:
				break
				
		return hashtag2.lower()


	def extractHashtag(self,tweet):
		hashtags = []
		words = tweet.split(' ')
		for word in words:
			if len(word)>1 and word[0]=='#':
				hashtag = self.truncateHashtag(word[1:])
				if(len(hashtag)>0): #To void avoids hashtags like ''
					hashtags.append(hashtag)
		
		return list(set(hashtags)) #this is to remove duplicates and sort the hashtags
	def createBagOfWords(self):
		keywords = self.text.split(' ')
		for keyword in keywords:
			if keyword.startswith('https://'):
				keywords.remove(keyword)
		self.bagOfWords = sets.Set(keywords)




