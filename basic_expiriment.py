import json
from lib.primitives import Company



# based on open source library - https://addisonlynch.github.io/iexfinance/stable/stocks.html#formatting
def main():
	company = Company('MSFT')
	# tsla = Stock('TSLA', output_format = 'pandas')

	# print(tsla.get_open())
	# financials = tsla.get_financials()
	# print(financials.iloc[2].get_values())

	# msft = Stock('MSFT')
	# print(msft.get_dividends())


if __name__ == "__main__":
	main()

