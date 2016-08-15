import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.flipkart.com/search?q=televisions&otracker=start&as-show=off&as=off'
#url = 'https://www.flipkart.com/search?q=shoes&sid=osp/cil/e1f&as=on&as-show=on&otracker=start&as-pos=1_1_ic_s'
pattern = re.compile("(.* ratings)")

info = []
res_list = []
ratings = []

def get_res_spider():
	src = requests.get(url)
	soup = BeautifulSoup(src.text, 'html.parser')
	#print(soup.prettify())
	d = soup.findAll('div', {'class': 'pu-details lastUnit'})
	for x in d:
		info.append(x.get('title'))
		info.append(x.get('href'))
		s = x.text
		rat = pattern.findall(s)
		info.append(rat)
		#s = s.replace(" ", "").replace("\n", "").replace("ratings", "").replace("(", "'").replace(")", "").replace(",", '').replace("'", "").replace("Rs.", "")
		#info.append(s)
		res_list.append(info)

	print('poop')
	
	for i in range(len(res_list)):
		print(res_list[i])
		print('\n')

if __name__ == "__main__":
	get_res_spider()