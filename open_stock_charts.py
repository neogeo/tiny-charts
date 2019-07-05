import argparse
import csv
import time
import webbrowser
from urllib import parse

'''A program to display tiny stockcharts
Set up with 
	python3.6 -m venv .env
	. .env/bin/activate

Run by giving it a space separated list of symbols
	python open_stock_charts [-s] list of symbols
	
	Or with no argument, which will open a file 'results.csv' (with one column "results") and open all symbols
	python open_stock_charts 
'''

URL = 'https://stockcharts.com/freecharts/candleglance.html?{}|B|Q3,10|1'
#  12 is max stockcharts will open at one time
BATCH_SIZE = 12


def open_stock_charts(symbols):
	# if no symbols were passed in
	if (symbols == None or len(symbols) == 0):
		symbols = read_csv()

	# open new tabs in batches
	for i in range(0, len(symbols), BATCH_SIZE):
		batch = symbols[i:i+BATCH_SIZE]
		url_list = ','.join(batch)
		# open browser with url
		chart_url = URL.format(url_list)
		print(chart_url)
		
		# use Safari, becuase it does not double-encode the URL like Chrome
		safari = webbrowser.get('safari')
		safari.open_new_tab(chart_url)

		# be nice, done hammber the site
		time.sleep(5)


	print("done")

def read_csv():
	symbols = []

	file = 'results.csv'
	with open(file) as csvfile:
		reader = csv.DictReader(csvfile)
		
		for row in reader:
			symbol = None

			# add each non empty value
			# support TD Scan results and my spreadsheet restuls
			if 'results' in row:
				symbol = row['results']
			elif '\ufeffWatchlist Scanner' in row:
				# thinkorswim excel
				symbol = row['\ufeffWatchlist Scanner']
			elif 'Watchlist Scanner' in row:
				# thinkorswim excel
				symbol = row['Watchlist Scanner']

			# if we found something and we are not on the wierd row in a TD CSV
			if(symbol and symbol != 'Results'):
				symbols.append(symbol)
				print(symbol)

	return symbols				


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	# a list of stock symbols
	parser.add_argument('-s', '--symbols', nargs='+')

	args = parser.parse_args()
	open_stock_charts(args.symbols)
