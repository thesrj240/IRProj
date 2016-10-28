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
				hashtags.append(self.truncateHashtag(word[1:]))
		
		return sorted(hashtags)
