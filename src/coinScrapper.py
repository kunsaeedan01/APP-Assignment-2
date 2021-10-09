from bs4 import BeautifulSoup
import requests
import lxml



class Scrapper:
    def __init__(self):
        pass

    def scrap_articles(self, currency_name):
        self.currency_name = currency_name
        response = requests.get(f"https://coinmarketcap.com/currencies/{self.currency_name}/news")
        soup = BeautifulSoup(response.content, 'html.parser')
        article_paragraph = soup.find_all(name= "p")
        for paragraph in article_paragraph:
            print(paragraph.getText())
            print("-------------------------------------------------")







#"sc-1eb5slv-0 svowul-3 ddtKCV"
