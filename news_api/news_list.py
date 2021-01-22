# My own modules.
from .news_api import NewsApi
from .news import News
from .keys import Keys


class NewsList:
    def __init__(self):
        controller = NewsApi()
        articles = controller.articles

        self.newses = NewsList.create_newses(articles)

    def to_contents(self):
        contents = ""
        for news in self.newses:
            contents += news.to_content()
            contents += "\n"
        return contents

    @staticmethod
    def create_newses(articles):
        newses = []
        for article in articles:
            data = NewsList.get_data(article)
            news = News(
                source_name=data[0],
                title=data[1],
                url=data[2],
            )
            newses.append(news)
        return newses

    @staticmethod
    def get_data(article):
        title = str(article.get(Keys.title_key))
        url = str(article.get(Keys.url_key))
        source = article.get(Keys.source_key)
        source_name = source.get(Keys.source_name_key)
        return source_name, title, url
