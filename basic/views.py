from django.shortcuts import render
import basic.codes.tweetDumper as td
import os


def searchPage(request):

	context = {}
	return render(request, 'searchPage.html', context)

def themes(request):

	context = {}
	return render(request, 'themes.html', context)

def findTweets(request):

	if request.method == 'POST':
		searchQuery = request.POST.get('search')

		# Retrieve Tweets
		td.get_all_tweets(str(searchQuery))

		# Run Turkish NLP
		# clean.main(str(searchQuery))

		# Run Spark
		location = 'data/' + searchQuery + '.txt'
		sparkPath = '/Users/k/Spark/bin/spark-submit'
		scriptPath = 'basic/codes/simpleApp.py'
		os.system(sparkPath + " --master local[4] " + scriptPath + " " + searchQuery + " > " + location)

		# Read Results
		# In this case, just Tweets
		results = str()
		count = 0
		with open(location, 'r') as f:
			for line in f:
				if count > 10:
					break
				else:
					results += line
					results += "\n"
					count += 1

		context = {"searchQuery":searchQuery, "results":results}
		return render(request, 'findTweets.html', context)
