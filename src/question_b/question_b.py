#write functions here, don't add input('') statements here!
class stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name
    
def get_stock_list():
    stock_list = [
        stock("AAPL", "Apple Inc"),
        stock("CAT", "Caterpillar"),
        stock("EK", "Eastman Kodak"),
        stock("GOOG", "Google"),
        stock("MSFT", "Microsoft")
    ]
    return stock_list