

from bs4 import BeautifulSoup
import urllib2

tbi = "http://timesofindia.indiatimes.com/city/patna/topper-scam-samastipur-principal-3-others-held/articleshow/58990221.cms "

tbi = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

tbi = "http://www.thebetterindia.com/date/2017/05/"

page = urllib2.urlopen(tbi)

from bs4 import BeautifulSoup

soup = BeautifulSoup(page,"html.parser")

print soup.prettify()

soup.find_all('a',class_="g1-frame") # gets the links for the articles

k = soup.find_all('a',class_="g1-button g1-button-m g1-button-solid g1-load-more")



for item in k :
    print item.find_all('data-g1-next-page-url')

x = k[0]

print x.find('a')


print type(str(k[0]))


tbi = str(k[0]).split('=')[2].split(' ')[0][1:-1]


soup.select('div a')