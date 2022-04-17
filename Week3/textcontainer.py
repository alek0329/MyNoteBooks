from classes import Text

class TextContainer(Text):
    def __init__(self, author,title, text):
        self.author = author
        self.text = text
        self.title = title

    def __str__(self):
        return '{title} is written by {author} and contains: {text} characters.'.format(
            author=self.author, text=len(self.text), title=self.title)

    def word_count (self):
        print(len(self.text))
        return len(self.text)


