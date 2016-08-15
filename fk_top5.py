# returns top 5 most reviewed

import csv
import requests
from bs4 import BeautifulSoup

# url_str = 'https://www.flipkart.com/search?q=televisions&otracker=start&as-show=off&as=off'
lolist = []

res_list = []
def get_res_spider():
	url_list = [url_str + '&page=2', url_str + '&page=3']
	#print(url_list)
	for url in url_list:
		src = requests.get(url)
		soup = BeautifulSoup(src.text, 'html.parser')
		print(soup.prettify())
		d = soup.findAll('div', {'class': 'pu-details lastUnit'})
		for i in d:
			dd = soup.findAll('div', {'class': 'pu-title fk-font-13'})
			for j in dd:
				a = soup.findAll('a', {'class': 'fk-display-block ssHashQuery'})
				for k in a:
					t = a.title
					res_list.append(t)
		print('\n\n\n\n\n\n\n\n\n\n')
	print('poop')
	print(res_list)

if __name__ == "__main__":
	url_str = input('Enter URL:\t\n')
	get_res_spider()
