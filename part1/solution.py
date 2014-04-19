import re
import sys
from pg_sample_texts import DIV_COMM, MAG_CART

documents = [DIV_COMM, MAG_CART]

title_search = re.compile(r'(title:\s*)(?P<title>(.*\S+\n)*)', re.IGNORECASE)
author_search = re.compile(r'(author:\s*)(?P<author>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:\s*)(?P<illustrator>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:\s*)(?P<translator>.*)', re.IGNORECASE)

# searches is a dictionary with key of 'search' and value of 'pattern'
# ??? how do you determine the use of a dictionary rather than a list?
searches = {}

# get user inputs for keyword searches
for kw in sys.argv[1:]:
	searches[kw] = re.compile(r'\b' + kw + r'\b', re.IGNORECASE)
# ??? why doesn't this work? >
# searches[kw] = re.compile(r'(?:.*\*\*\*\s*START.*)' + r'\b' + kw + r'\b' + r'(?:.*\*\*\*\s*END.*)', re.IGNORECASE)

for i, doc in enumerate(documents):
	title = re.search(title_search, doc).group('title')
	author = re.search(author_search, doc)
	illustrator = re.search(illustrator_search, doc)
	translator = re.search(translator_search, doc)

	if author:
		author = author.group('author')
	if illustrator:
		illustrator = illustrator.group('illustrator')
	if translator:
		translator = translator.group('translator')

	print '*' * 25
	print "Here's the info for file {:0>3d}".format(i)
	print "The title of the text is {}".format(title)
	if author:
		print "The author is {}".format(author)
	if illustrator:
		print "The illustrator is {}".format(illustrator)
	if translator:
		print "The translator is {}".format(translator)
	
	print "\n"
	
	print "Here's the counts for the keywords you searched for:"
	# iterating through all the searches user inputted
	for search in searches:
		print "\"{0}\" : {1}".format(search, len(re.findall(searches[search], doc)))
	print "\n"
