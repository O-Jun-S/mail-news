class News:
    def __init__(self, source_name, title, url):
        self.source_name = source_name
        self.title = title
        self.url = url

    def to_content(self):
        return f"{self.source_name} : {self.title} : {self.url}"
