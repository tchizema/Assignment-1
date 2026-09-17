class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print()


# Create two Book objects
book1 = Book("Harry Potter", "J.K. Rowling", 25.99)
book2 = Book("The Alchemist", "Paulo Coelho", 19.99)

# Display book details
book1.display_details()
book2.display_details()