class book:
    def __init__(self, author, title,):
        self.author = author
        self.title = title
    def available1(self):
        print("book: ",self.title)
        print("author: ", self.author)


BforBook = book("Mortimer J. Adler", "How to Read a Book")
BforBook.available1()
        