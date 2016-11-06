class Hashtag_cluster_class:
	def __init__(self,cluster_id):
		self.cluster_id = cluster_id
		self.hashtag_list = []
		self.tweet_list = []
		self.centroid = 0

	def add_hashtag(self,hashtag):
		self.hashtag_list.append(hashtag)

	def add_tweet(self,tweet):
		self.tweet_list.append(tweet)
		self.recompute_centroid()
	
	def recompute_centroid():
		return

