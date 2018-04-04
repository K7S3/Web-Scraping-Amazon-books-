from bs4 import BeautifulSoup
import requests
import os
import csv

file = open('in_book.csv' , 'w')
file.write('Name' + ";" + 'Author' + ";" + 'URL' + ";"  + 'Price' + ";" + 'Number of Ratings' + ";" + 'Average Rating' + "\n")

for i in range(1,6):
	source = requests.get('https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_{0}?ie=UTF8&pg={0}'.format(i)).text

	soup = BeautifulSoup(source , 'lxml')

	main = soup.find('div' , id = 'zg_centerListWrapper')

	for diff in main.find_all('div' , class_ = 'zg_itemWrapper'):
		try:
			name = diff.find('div' , class_ = 'p13n-sc-truncate p13n-sc-line-clamp-1').string.strip()
			name_val = name
	
		except Exception as e:
			name = diff.find('div' , class_ = 'p13n-sc-truncate p13n-sc-line-clamp-2').string.strip()
			name_val = name

		except Exception as e:
			name_val = "Not Available"

		file.write(str(name_val) + ";")
		print(name_val)


		try:
			 author = diff.find('div' , class_ = 'a-row a-size-small')
			 author_val = author.text
		

		except Exception as e :
			author_val = "Not Available"

		except Exception as AttributeError:
			author_val = "Not Available"

		file.write(str(author_val) + ";")
		print (author_val)



		try:
			url = diff.find('a' , class_ = 'a-link-normal')['href'].strip()
			url_val = 'https://www.amazon.in{0}'.format(url)

		except Exception as e:
			url_val = "Not Available"
		print(url_val)
		file.write(url_val + ";")



		try:
			price = diff.find('span' , class_ = 'p13n-sc-price').text.strip()
			price_val = price

		except Exception as e:
			price_val = "Not Available"
		print(price_val)
		file.write(price_val + ";")




		try:
			n_o_r = diff.find('a' , class_ = 'a-size-small a-link-normal').string.strip()
			n_o_r_val = n_o_r

		except Exception as e:
			n_o_r_val = "Not Available"
		print(n_o_r_val)		
		file.write(n_o_r_val + ";")


		try:
			avg_rat = diff.find('div' , class_ = 'a-icon-row a-spacing-none').find('a' , class_ = 'a-link-normal')['title'].strip()
			avg_rat_val = avg_rat

		except Exception as e:
			avg_rat_val  = "Not Available"
		print(avg_rat_val)
		file.write(avg_rat_val + "\n")
		

file.close()
		
