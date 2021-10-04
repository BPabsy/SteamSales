from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq



#import and open URL
myUrl = 'https://store.steampowered.com/'
uClient = uReq(myUrl)
page_html = uClient.read()
uClient.close()
page_soup = BeautifulSoup(page_html, 'html.parser')



#body of webpage
page = page_soup.find('div', class_='home_tabs_content')

#sales section of webpage
sales = page.find('div', id='tab_specials_content')

#grab all item names
item_names = sales.findAll('div', {'class':'tab_item_name'})
item0_name = item_names[0].text
item1_name = item_names[1].text
item2_name = item_names[2].text
item3_name = item_names[3].text
item4_name = item_names[4].text
item5_name = item_names[5].text
item6_name = item_names[6].text
item7_name = item_names[7].text
item8_name = item_names[8].text
item9_name = item_names[9].text

#grab all original prices
original_prices = sales.findAll('div', {'class':'discount_original_price'})
item0_original_price = original_prices[0].text
item1_original_price = original_prices[1].text
item2_original_price = original_prices[2].text
item3_original_price = original_prices[3].text
item4_original_price = original_prices[4].text
item5_original_price = original_prices[5].text
item6_original_price = original_prices[6].text
item7_original_price = original_prices[7].text
item8_original_price = original_prices[8].text
item9_original_price = original_prices[9].text

#grab all sale prices
sale_prices = sales.findAll('div', {'class':'discount_final_price'})
item0_sale_price = sale_prices[0].text
item1_sale_price = sale_prices[1].text
item2_sale_price = sale_prices[2].text
item3_sale_price = sale_prices[3].text
item4_sale_price = sale_prices[4].text
item5_sale_price = sale_prices[5].text
item6_sale_price = sale_prices[6].text
item7_sale_price = sale_prices[7].text
item8_sale_price = sale_prices[8].text
item9_sale_price = sale_prices[9].text

#grab all sale percentages
sale_percent = sales.findAll('div', {'class':'discount_pct'})
item0_percent = sale_percent[0].text
item1_percent = sale_percent[1].text
item2_percent = sale_percent[2].text
item3_percent = sale_percent[3].text
item4_percent = sale_percent[4].text
item5_percent = sale_percent[5].text
item6_percent = sale_percent[6].text
item7_percent = sale_percent[7].text
item8_percent = sale_percent[8].text
item9_percent = sale_percent[9].text

#display data
item0 = '{name} {percent} off\nOriginal Price: {price}\nSale Price: {sale_price}'\
		.format(name=item0_name, percent=item0_percent, price=item0_original_price, sale_price=item0_sale_price)
item1 = '{name} {percent} off\nOriginal Price: {price}\nSale Price: {sale_price}'\
		.format(name=item1_name, percent=item1_percent, price=item1_original_price, sale_price=item1_sale_price)
item2 = '{name} {percent} off\nOriginal Price: {price}\nSale Price: {sale_price}'\
		.format(name=item2_name, percent=item2_percent, price=item2_original_price, sale_price=item2_sale_price)
item3 = '{name} {percent} off\nOriginal Price: {price}\nSale Price: {sale_price}'\
		.format(name=item3_name, percent=item3_percent, price=item3_original_price, sale_price=item3_sale_price)
item4 = '{name} {percent} off\nOriginal Price: {price}\nSale Price: {sale_price}'\
		.format(name=item4_name, percent=item4_percent, price=item4_original_price, sale_price=item4_sale_price)
item5 = '{name} {percent} off\nOriginal Price: {price}\nSale Price: {sale_price}'\
		.format(name=item5_name, percent=item5_percent, price=item5_original_price, sale_price=item5_sale_price)
item6 = '{name} {percent} off\nOriginal Price: {price}\nSale Price: {sale_price}'\
		.format(name=item6_name, percent=item6_percent, price=item6_original_price, sale_price=item6_sale_price)
item7 = '{name} {percent} off\nOriginal Price: {price}\nSale Price: {sale_price}'\
		.format(name=item7_name, percent=item7_percent, price=item7_original_price, sale_price=item7_sale_price)
item8 = '{name} {percent} off\nOriginal Price: {price}\nSale Price: {sale_price}'\
		.format(name=item8_name, percent=item8_percent, price=item8_original_price, sale_price=item8_sale_price)
item9 = '{name} {percent} off\nOriginal Price: {price}\nSale Price: {sale_price}'\
		.format(name=item9_name, percent=item9_percent, price=item9_original_price, sale_price=item9_sale_price)

item_list = '{a}\n\n{b}\n\n{c}\n\n{d}\n\n{e}\n\n{f}\n\n{g}\n\n{h}\n\n{i}\n\n{j}'\
			.format(a=item0, b=item1, c=item2, d=item3, e=item4, f=item5, g=item6, h=item7, i=item8, j=item9 )

print(item_list)
input()