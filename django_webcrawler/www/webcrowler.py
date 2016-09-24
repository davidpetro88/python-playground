import urllib.request

from bs4 import BeautifulSoup


class WebCrowlwer:

    def __init__(self):
        self.headers = {}
        self.link = 'http://www.themovieblog.com/category/features/reviews/'

    def getContent(self):
        soup = self.get_html()
        data = soup.findAll(attrs={'class': 'genaral-post-item'})
        content = []
        for index, post in enumerate(data):
            content.insert(index,{'header' : post.find(attrs={'class': 'genpost-entry-header', 'class': 'genpost-entry-title'}).text,
                                  'body': post.find(attrs={'class': 'genpost-entry-content'}).p.text,
                                  'moretag' : post.find(attrs={'class': 'genpost-entry-content'}).a['href']})
        return content

    def get_html(self):
        request = urllib.request.Request(self.link, headers=self.headers)
        return BeautifulSoup(urllib.request.urlopen(request), "html.parser")


#
#
# test = WebCrowlwer()
# a = test.getContent()
# print(a[0]['body'])
