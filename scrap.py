from bs4 import BeautifulSoup
import requests
import re
import json
import random

cat_list = []
cat_dir = {
	"cat" : cat_list
}
page_list = [] 
quotes_list = []

def category():
	category_url = 'http://www.brainyquote.com/quotes/topics.html'
	html = requests.get(category_url) #requesting url
	soup = BeautifulSoup(html.text) #making soup for scrappig 
	category = soup.find_all('a',{"href" : re.compile("/quotes/topics/topic_")}) #to find tag "a" who contains category
	for name in category:
		cat_list.append(name.text)

	return json.dumps(cat_dir) 

def pages(category):
	url = "http://www.brainyquote.com/quotes/topics/topic_" + category + ".html"
	html = requests.get(url)
	soup = BeautifulSoup(html.text)
	div = soup.find('div',{"class":"quote-nav-msnry "})#to find total pages
	for li in div.find_all('li'):
		page_list.append(li) #we need second last li so appending to list
	total_pages = page_list[len(page_list) - 2].text #here we have total number of pages
	return total_pages

def quotes(category):
	p = int(pages(category))
	page = range(1,p+1)
	random_page = random.choice(page)
	url = "http://www.brainyquote.com/quotes/topics/topic_" + category + str(random_page) + ".html"
	html = requests.get(url)
	soup = BeautifulSoup(html.text)
	a_quotes =  soup.find_all('a',title='view quote')
	for each in a_quotes:
		quotes_list.append(each.text)
		random_quote = { "quote" : random.choice(quotes_list)}
	return random_quote


	




