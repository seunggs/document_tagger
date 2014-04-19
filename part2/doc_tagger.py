import sys
import os
import re

searches = {}	# key: keyword, value: matching object for finding keyword
documents = {}	# key: file name, value: full text 

directory = sys.argv[1]

for kw in sys.argv[2:]:
	searches[kw] = re.compile(r'\b' + kw + r'\b', re.IGNORECASE)
# or: searches = {kw: re.compile(r'\b' + kw + r'\b', re.IGNORECASE) for kw in sys.argv[2:]}

title_search = re.compile(r'(title:\s*)(?P<title>(\S+\s)*\n*)', re.IGNORECASE)
author_search = re.compile(r'(author:\s*)(?P<author>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:\s*)(?P<illustrator>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:\s*)(?P<translator>.*)', re.IGNORECASE)

for fl in os.listdir(directory):
	if fl.endswith(".txt"):
		fl_path = os.path.join(directory, fl)
		with open(fl_path, "r") as f:
			full_text = f.read()

		title = re.search(title_search, full_text).group('title')
		author = re.search(author_search, full_text)
		illustrator = re.search(illustrator_search, full_text)
		translator = re.search(translator_search, full_text)

		if author:
			author = author.group('author')
		if illustrator:
			illustrator = illustrator.group('illustrator')
		if translator:
			translator = translator.group('translator')

		print "*" * 25
		print "Here's the info for file {}".format(fl)
		print "The title of the text is {}".format(title)
		print "The author is {}".format(author)
		print "The illustrator is {}".format(illustrator)
		print "The translator is {}".format(translator)
		print "\n"
		print "Here's the counts for the keywords you searched for:"

		for search in searches:
			print "\"{0}\" : {1}".format(search, len(re.findall(searches[search], full_text)))

		print "\n"
