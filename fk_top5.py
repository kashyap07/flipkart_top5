# returns top 5 most reviewed

import csv
import requests
from bs4 import BeautifulSoup

url_str = 'https://www.flipkart.com/search?q=televisions&otracker=start&as-show=off&as=off'
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
		#lolist.append(i)

	#print(lolist)


	'''
	for in soup.findAll('a', {'class': 'font18'}):
			href = str('http://www.carwale.com' + link.get('href'))
			# us str() to convert to regular string
			car_name = str(link.string)
			# print(car_name)
			# print(href)
			# get_individual_car_data(href)
			
			detail_list = []
			detail_list.append(car_name)
			detail_list.append(href)
			detail_list.append(get_individual_car_data(href))
			# print(detail_list)
			giga_list.append(detail_list)
	# print(giga_list)

def get_individual_car_data(car_url):
	src = requests.get(car_url)
	soup = BeautifulSoup(src.text, 'html.parser')
	for car in soup.findAll('span', {'class': 'font24 text-black margin-right5'}):
		car_str = str(car.text)
		return car_str
		# use 'text' instead of string'''

if __name__ == "__main__":
	#url_str = input('Enter URL:\t\n')
	#print(url_str + "\n")
	get_res_spider()
'''
	all_car_spider()
	outfile = open('./car_list.csv', 'wb')
	writer = csv.writer(outfile)
	writer.writerow(['CAR NAME', 'URL', 'EX-SHOWROOM PRICE'])
	writer.writerows(giga_list)'''