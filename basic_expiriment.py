import json
from lib.primitives import Company
from lib.valuations import Valuations

# The core api is https://iextrading.com/developer/docs/
# based on open source library - https://addisonlynch.github.io/iexfinance/stable/stocks.html#formatting
def main():
	microsoft = Company('MSFT')
	valuations = Valuations(microsoft)
	valuations.freeCashFlow(2018)

if __name__ == "__main__":
	main()

