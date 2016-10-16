import urllib.request

from bs4 import BeautifulSoup


class WebCrowlwer(object):
    def __init__(self):
        self.headers = {}
        self.link = 'http://www.themovieblog.com/category/features/reviews/'

    def get_content(self):
        soup = self.get_html()
        data = soup.findAll(attrs={'class': 'genaral-post-item'})
        content = []
        for index, post in enumerate(data):
            content.insert(index,
                 {'header': post.find(attrs={'class': 'genpost-entry-header','class': 'genpost-entry-title'}).text,
                  'content': post.find(attrs={'class': 'genpost-entry-content'}).p.text,
                  'moretag': post.find(attrs={'class': 'genpost-entry-content'}).a['href']})
        return content

    def get_content_v2(self):
        return list(map((lambda x: self.body_html(x)), self.get_html().findAll(attrs={'class': 'genaral-post-item'})))

    def body_html(self, html_general_post):
        return {'header': html_general_post.find(attrs={'class': 'genpost-entry-header','class': 'genpost-entry-title'}).text,
                'content': html_general_post.find(attrs={'class': 'genpost-entry-content'}).p.text,
                'moretag': html_general_post.find(attrs={'class': 'genpost-entry-content'}).a['href']}

    def get_html(self):
        request = urllib.request.Request(self.link, headers=self.headers)
        return BeautifulSoup(urllib.request.urlopen(request), "html.parser")