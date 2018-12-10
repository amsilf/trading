import lib
from lib.static_resource_reader import StaticResourceReader

class Valuations:

	company = None

	# advanced financials
	# https://www.investopedia.com/terms/w/wacc.asp
	wacc = -1
	costOfEquity = -1
	riskFreeRate = -1
	marketRateOfReturn = -1

	def __init__(self, company):
		self.company = company
		self.marketDataReader = StaticResourceReader('./resources/market_data.csv')

	# WACC - weighted average cost of capital, required by CAMP model
	# https://www.investopedia.com/ask/answers/063014/what-formula-calculating-weighted-average-cost-capital-wacc.asp
	def calculateWacc(self):
		exit(0)

	# Cost of equity = Risk-Free Rate + Beta * (Market Rate of Return - Risk Free Rate), according to CAMP model
	# Risk-Free Rate - yield of 30 year T-bills
	# Market Rate of Return - S&P 500 rate of return
	# https://www.investopedia.com/terms/c/costofequity.asp
	def calculateCostOfEquity(self, year):
		riskFreeRate = float(self.marketDataReader.getFinancialByTicker('risk_free_rate', year))
		marketRateOfReturn = float(self.marketDataReader.getFinancialByTicker('snp_500_market_return', year))
		beta = self.company.keyStatistics.getKeyStatisticsByName('beta')
		return riskFreeRate + beta * (marketRateOfReturn - riskFreeRate)

	# FCF model - https://www.investopedia.com/articles/fundamental-analysis/11/present-value-free-cash-flow.asp
	# Calcualtion example - https://www.stock-analysis-on.net/NASDAQ/Company/Microsoft-Corp/DCF/Present-Value-of-FCFF
	def freeCashFlow(self, year):
		costOfEquity = self.calculateCostOfEquity(year)
		print('cost of equity = ', costOfEquity)
		exit(0)

	# DCF model - https://www.investopedia.com/university/dcf/dcf4.asp
	def discountedCashFlow(self):
		exit(0)

	# DDM - https://www.investopedia.com/terms/d/ddm.asp
	def dividendDiscountedModel(self):
		exit(0)