import json
from iexfinance import Stock

class SingleDividendPayment:
	exDate = ''
	paymentDate = ''
	recordDate = ''
	declaredDate = ''
	amount = -1
	flag = ''
	type = ''
	qualified = ''
	indicated = ''

	def __init__(self, dividend_json):
		self.exDate  = dividend_json['exDate']
		self.paymentDate = dividend_json['paymentDate']
		self.recordDate = dividend_json['recordDate']
		self.declaredDate = dividend_json['declaredDate']
		self.amount = dividend_json['amount']
		self.flag = dividend_json['flag']
		self.type = dividend_json['type']
		self.qualified = dividend_json['qualified']
		self.indicated = dividend_json['indicated']


# https://iextrading.com/developer/docs/#dividends
class Dividends:
	""" The class represents a compnay dividends and describes api resonse """

	payment_period = '5y'
	dividends = []

	def __init__(self, stock, period='5y'):
		self.payment_period = period
		dividends_response = stock.get_dividends(range='5y')
		for dividend in dividends_response:
			self.dividends.append(SingleDividendPayment(dividend))


class Company:
	stock = None
	company_dividends = None

	format = 'pandas'

	def __init__(self, ticker, data_format = 'pandas'):
		format = data_format
		stock = Stock(ticker, output_format = format)
		company_dividends = Dividends(stock)