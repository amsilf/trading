import json
from iexfinance import Stock
from lib.resource_reader import ResourceReader

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

# https://iextrading.com/developer/docs/#key-stats
class KeyStatistics:
	availableValues = ["companyName", "marketcap", "beta", "week52high", "week52low", "week52change",
		"shortInterest", "shortDate", "dividendRate", "dividendYield", "exDividendDate",
		"latestEPS", "latestEPSDate", "sharesOutstanding", "floatVal",
		"returnOnEquity", "consensusEPS", "numberOfEstimates", "symbol", "EBITDA",
		"revenue", "grossProfit", "cash", "debt", "ttmEPS", "revenuePerShare",
		"revenuePerEmployee","peRatioHigh","peRatioLow","EPSSurpriseDollar","EPSSurprisePercent",
		"returnOnAssets","returnOnCapital","profitMargin","priceToSales","priceToBook",
		"day200MovingAvg","day50MovingAvg","institutionPercent","insiderPercent","shortRatio",
		"year5ChangePercent","year2ChangePercent","year1ChangePercent","ytdChangePercent","month6ChangePercent",
		"month3ChangePercent","month1ChangePercent","day5ChangePercent"]

	keyStatisticsValus = {}

	def getKeyStatisticsByName(self, name):
		if name in self.keyStatisticsValus:
			return self.keyStatisticsValus.get(name)
		else:
			return ""

	def __init__(self, stock):
		self.keyStatisticsValus = stock.get_key_stats()


class SingleFinancialReport:

	ticker = ''

	# core financials
	reportDate = ''
	grossProfit = -1
	# The cost of revenue is the total cost of manufacturing and delivering a product or service
	costOwevenue = -1
	operatingRevenue = -1
	totalRevenue = -1
	operatingIncome = -1
	netIncome = -1
	researchAndDevelopment = 1
	operatingExpense = -1
	currentAssets = -1
	totalAssets = -1
	totalLiabilities = -1
	currentCash = -1
	currentLiabilities = -1
	# current portion of long term debt
	currentDebt = -1
	totalCash = -1
	totalDebt = -1
	shareholderEquity = -1
	cashChange = -1
	cashFlow = -1
	operatingGainsLosses = -1

	# ratio analysis
	currentRatio = -1

	def __init__(self, ticker, singleReport, liabilitityReader):
		self.ticker = ticker
		self.reportDate = singleReport['reportDate']
		self.grossProfit = singleReport['grossProfit']
		self.costOfRevenue = singleReport['costOfRevenue']
		self.operatingRevenue = singleReport['operatingRevenue']
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

		self.enrichDataQuality(liabilitityReader)

		self.calculateRatios()

	# TODO should we pass list of financials?
	def enrichDataQuality(self, resourceReader):
		if self.currentLiabilities == -1:
			 self.currentLiabilities = resourceReader.getFinancialByTicker(self.ticker, 'currentLiabilities', self.reportDate)

	def calculateRatios(self):
		self.currentRatio = self.currentAssets / self.currentLiabilities

class Financials:

	financials = []
	liabilitityReader = None

	def __init__(self, ticker, stock):
		liabilitityReader = ResourceReader('./resources/liabilities.csv')

		financials_response = stock.get_financials();
		for financial in financials_response:
			self.financials.append(SingleFinancialReport(ticker, financial, liabilitityReader))

class Company:
	stock = None

	dividends = None
	financials = None
	keyStatistics = None

	format = 'pandas'

	def __init__(self, ticker, data_format = 'json'):
		format = data_format
		self.stock = Stock(ticker, output_format = format)
		self.dividends = Dividends(self.stock)
		self.financials = Financials(ticker, self.stock)
		self.keyStatistics = KeyStatistics(self.stock)

