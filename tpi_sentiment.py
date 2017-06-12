

from bs4 import BeautifulSoup
import urllib2

tbi = "http://timesofindia.indiatimes.com/city/patna/topper-scam-samastipur-principal-3-others-held/articleshow/58990221.cms"

tbi = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page = urllib2.urlopen(tbi)

from bs4 import BeautifulSoup

soup = BeautifulSoup(page,"html.parser")

print soup.prettify()