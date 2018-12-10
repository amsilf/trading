import pandas

class StaticResourceReader:

	resourceLocation = ''
	headerFormat = None
	resourceData = None

	def __init__(self, resource, headerFormat=['id', 'type', 'date', 'value']):
		self.resourceLocation = resource
		self.headerFormat = headerFormat

	def getFinancialByTicker(self, type, date):
		resourceData = pandas.read_csv(self.resourceLocation)
		for index, row in resourceData.iterrows():
			if (row['type'] == type and row['date'] == date):
				return row['value']

		return -1
