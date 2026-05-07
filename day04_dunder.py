class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book(Title: {self.title}, Author: {self.author}, Pages: {self.pages})"

    def __len__(self):
        return len(self.pages)

b = Book("The absolute scammer LLOYD", "Puddong", ["First", "Second", "Third", "Fourth"])

print(str(b))
print(repr(b))
print(len(b))
