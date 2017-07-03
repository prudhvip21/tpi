

from bs4 import BeautifulSoup
import urllib2

#tbi = "http://timesofindia.indiatimes.com/city/patna/topper-scam-samastipur-principal-3-others-held/articleshow/58990221.cms "
# tbi = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

tbi = "http://www.thebetterindia.com/date/2017/05/"
page = urllib2.urlopen(tbi)
soup = BeautifulSoup(page,"html.parser")

print soup.prettify()
pages = soup.find_all('a',class_="g1-frame") # gets the links for the articles

k = soup.find_all('a',class_="g1-button g1-button-m g1-button-solid g1-load-more")
x = k[0]
k[0].get('data-g1-next-page-url')

# tbi = str(k[0]).split('=')[2].split(' ')[0][1:-1] # going to next page from load more
# soup.select('div a')

""" Reading the text from the page """

page = urllib2.urlopen("http://www.thebetterindia.com/102639/fight-right-to-education-anurag-kundu/")
soup = BeautifulSoup(page,"html.parser")
print soup.prettify()

soup.find_all('h2')[0].get_text()


h2 class ="entry-subtitle g1-gamma g1-gamma-3rd"




"""reading archives of entire month"""
tbi = "http://www.thebetterindia.com/date/2017/05/"
page = urllib2.urlopen(tbi)
soup = BeautifulSoup(page,"html.parser")
content = []
heading = []

for i in range(1,50) :
    page = urllib2.urlopen(tbi)
    soup = BeautifulSoup(page, "html.parser")
    links = soup.find_all('a', class_="g1-frame") # all links in that page
    links = [item.get('href') for item in links]
    try :
        pp = soup.find_all('a', class_="g1-button g1-button-m g1-button-solid g1-load-more") #next page
        tbi = pp[0].get('data-g1-next-page-url')
        print i, tbi
    except :
        break

    for k in links :
        link_page = urllib2.urlopen(k)
        soup_page = BeautifulSoup(link_page, "html.parser")
        article = []
        for para in soup_page.find_all('p'):
            if len(para.get_text()) > 50 :
                article.append(para.get_text())
        content.append(article)
        h = []
        h.append(soup_page.find_all('h2')[0].get_text())
        h.append(soup_page.find_all('h1')[0].get_text())
        heading.append(h)



""" Times of India archives page news links extractor """

page = "http://timesofindia.indiatimes.com/2008/1/17/archivelist/year-2008,month-1,starttime-39464.cms"
page = urllib2.urlopen(page)
soup = BeautifulSoup(page,"html.parser")

print soup.prettify()

for item in soup.find_all('a') :
    #print type(item.get('href'))
    l = str(item.get('href')).split('/')
    if 'articleshow' in l :
        print item.get('href')

