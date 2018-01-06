from flask import Flask
from flask import jsonify
from flask import Flask
from pymongo import MongoClient
import json
import requests
import bs4
import urllib3
urllib3.disable_warnings()
# To disable SNImissing security warning
app = Flask(__name__)
@app.route('/<author>')
def crawl_quotes(author):
	client = MongoClient()
	db = client.test_database
	collection = db.test_collection
	lists = []
	jsonD = {}
	new_collection = collection.find({'author':author})
	if new_collection.count()>0:
		for obj in new_collection:
			del obj['_id']
			print obj
	else:
		url = 'https://www.goodreads.com/quotes/search?q='+author
		req = requests.get(url)
		soup = bs4.BeautifulSoup(req.text,"html.parser")
		for script in soup(["script", "style"]): # remove all javascript and stylesheet code
		        script.extract()
		next_element = soup.find('a',class_='next_page')
		last_page = 1
		if not next_element is None:
			last_page = next_element.find_previous_sibling('a').text
		for i in range(1,int(last_page)+1):
			print i
			url = 'https://www.goodreads.com/quotes/search?page='+str(i)+'&q=gandhi'
			req = requests.get(url)
			soup=bs4.BeautifulSoup(req.text,"html.parser")
			for script in soup(["script", "style"]):
				script.extract()
			links = soup.find_all('div',class_='quoteText')
			for link in links:
				lists.append(link.text)
	jsonD[author] = lists
	for listItem in lists:
		collection.insert({'author' : author, "quotes":listItem})
	return jsonify(jsonD)
app.run()