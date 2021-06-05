from bs4 import BeautifulSoup
import requests

class Melon(object):
    url = 'https://www.melon.com/chart/index.htm?'
    headers = {'User-Agent':'Mozilla/5.0'}
    class_name = []

    def set_url(self, detail):
        #detail 은 chartdate=20210605&charthour=14 부분으로 바뀌는 값
        self.url = requests.get(f'{self.url}{detail}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls1 = soup.find_all(name='div', attrs={"class":"ellipsis rank03"})
        for idx, title in enumerate(ls1):
            print(f'{idx+1}위 {title.find("a").text}')

    @staticmethod
    def main():
        melon = Melon()
        melon.set_url('dayTime=2021060515')
        melon.get_ranking()

Melon.main()