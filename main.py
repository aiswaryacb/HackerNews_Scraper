
# This project uses the website 'Hacker News' - https://news.ycombinator.com/news
# We are using 'Beautiful Soup' tool for scraping the website

import requests
from bs4 import BeautifulSoup
import pprint #pretty print

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')  # when we click in more, we get this link
#print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
#print(soup)
#print(soup.title)
#print(soup.body)
#print(soup.contents)
#print(soup.find_all('div'))
#print(soup.find_all('a'))
#print(soup.select('.score')) # for selecting all items of class='score'
                            # dot is used for class, hash is used for id


links = soup.select('.titleline > a')
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline > a')
subtext2 = soup2.select('.subtext')

total_list = links + links2
total_subtexts = subtext + subtext2

#print(votes[0]) # to grab 1st item, index 0 is used

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True) # sorting a dictionary with key votes in the reverse order

def create_custom_hacker_news(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hacker_news(total_list, total_subtexts))

