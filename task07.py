class Book:
    def __init__(self, title, author, year):
        self.title=title
        self.author=author
        self.year=year
book1=Book("Otkan kunlar", "Abdulla Qoodiriy", 1994)
book2=Book("Jimjitlik", "Said Ahmad", 2023)
print(f"Title: {book1.title}, Author: {book1.author}, Year: {book1.year}")
print(f"Title: {book2.title}, Author: {book2.author}, Year: {book2.year}")