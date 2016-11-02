import csv
f = open('training_set_tweets.txt','r')
for line in csv.reader(f, dialect="excel-tab"):
	for l in line:
		print l
f.close()