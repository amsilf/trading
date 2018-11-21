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

class SingleFinancialReport:

	# basic financials
	reportDate = ''
	grossProfit = -1
	costOfRevenue = -1
	costOfRevenue = -1
	totalRevenue = -1
	operatingIncome = -1
	netIncome = -1
	researchAndDevelopment = 1
	operatingExpense = -1
	currentAssets = -1
	totalAssets = -1
	totalLiabilities = -1
	currentCash = -1
	# current portion of long term debt
	currentDebt = -1
	totalCash = -1
	totalDebt = -1
	shareholderEquity = -1
	cashChange = -1
	cashFlow = -1
	operatingGainsLosses = -1

	# ratio analysis

	def __init__(self, singleReport):
		self.reportDate = singleReport['reportDate']
		self.grossProfit = singleReport['grossProfit']
		self.costOfRevenue = singleReport['costOfRevenue']
		self.totalRevenue = singleReport['totalRevenue']
		self.operatingIncome = singleReport['operatingIncome']
		self.netIncome = singleReport['netIncome']
		self.researchAndDevelopment = singleReport['researchAndDevelopment']
		self.operatingExpense = singleReport['operatingExpense']
		self.currentAssets = singleReport['currentAssets']
		self.totalAssets = singleReport['totalAssets']
		self.totalLiabilities = singleReport['totalLiabilities']
		self.currentCash = singleReport['currentCash']
		self.currentDebt = singleReport['currentDebt']
		self.totalCash = singleReport['totalCash']
		self.totalDebt = singleReport['totalDebt']
		self.shareholderEquity = singleReport['shareholderEquity']
		self.cashChange = singleReport['cashChange']
		self.cashFlow = singleReport['cashFlow']
		self.operatingGainsLosses = singleReport['operatingGainsLosses']
		#self.calculateRatios()

	# def calculateRatios(self):


class Financials:

	financials = []

	def __init__(self, stock):
		financials_response = stock.get_financials();
		for financial in financials_response:
			self.financials.append(SingleFinancialReport(financial))

class Company:
	stock = None

	dividends = None
	financials = None

	format = 'pandas'

	def __init__(self, ticker, data_format = 'json'):
		format = data_format
		self.stock = Stock(ticker, output_format = format)
		self.dividends = Dividends(self.stock)
		self.financials = Financials(self.stock)

