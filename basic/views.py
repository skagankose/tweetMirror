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

		location = 'data/' + searchQuery + '_results.txt'

		try:

			# Read Results
			results = list()
			with open(location, 'r') as F:
				for line in F:
					results += [line.split()]

		except:

			# Retrieve Tweets
			td.get_all_tweets(str(searchQuery))

			# Run Turkish NLP
			# clean.main(str(searchQuery))

			# Run Spark
			sparkPath = '/Users/k/Spark/bin/spark-submit'
			scriptPath = 'basic/codes/simpleApp.py'
			os.system(sparkPath + " --master local[4] " + scriptPath + " " + searchQuery)

			# Read Results
			results = list()
			with open(location, 'r') as F:
				for line in F:
					results += [line.split()]

		# Get Words
		# t00= results[0][0];t01= results[0][1];t02= results[0][2];t03= results[0][3];t04= results[0][4];
		# t05= results[0][5];t06= results[0][6];
		# t00= results[0][0];t01= results[0][1];t02= results[0][2];t03= results[0][3];t04= results[0][4];
		# t05= results[0][5];t06= results[0][6];
		# t00= results[0][0];t01= results[0][1];t02= results[0][2];t03= results[0][3];t04= results[0][4];
		# t05= results[0][5];t06= results[0][6];


		context = {"searchQuery":searchQuery, "results": results}
		return render(request, 'findTweets.html', context)
