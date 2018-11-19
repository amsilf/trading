from iexfinance import Stock

# https://iextrading.com/developer/docs/#dividends
class Dividends:
	""" The class represents a compnay dividends and describes api resonse """

	d5y = -1
	d2y = -1
	d1y = -1
	# year to date - https://www.investopedia.com/terms/y/ytd.asp
	ytd = -1
	d6m = -1
	d3m = -1
	d1m = -1

	def __init__(self, stock):
		dividends_response = stock.get_dividends()

class Company:
	stock = None
	format = 'pandas'

	def __init__(self, ticker, data_format = 'pandas'):
		format = data_format
		stock = Stock('TSLA', output_format = format)