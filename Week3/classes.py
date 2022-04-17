
class Text():
    
    def __init__(self, author, title, text):
        self.author = author
        self.title = title
        self.text = text

    def __str__(self):
        return '{title} is written by {author}'.format(title=self.title, author=self.author)


if __name__ == '__main__':
    text1 = Text('Dennis','haveturen','De gik en lang tur i haven')
    tc = TextContainer(text1)
    print(tc)