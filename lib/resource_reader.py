import pandas

class ResourceReader:

	resourceLocation = ''
	headerFormat = None
	resourceData = None

	def __init__(self, resource, headerFormat=['id','ticker','date','financial','value']):
		self.resourceLocation = resource
		self.headerFormat = headerFormat

	def getFinancialByTicker(self, ticker, financial, date):
		resourceData = pandas.read_csv(self.resourceLocation)
		for index, row in resourceData.iterrows():
			if (row['financial'] == financial and row['date'] == date and row['ticker'] == ticker):
				return row['value']

		return -1