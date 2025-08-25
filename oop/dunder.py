class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def open(self):
        print(f"Opening {self.title} by {self.author}")
    def __len__(self):
        return self.pages
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __del__(self):
        print(f"Deleting {self.title} by {self.author}")


goodbye_garry_cooper = Book("Garry Cooper", "Garry Cooper", 10)

print(str(goodbye_garry_cooper))

del goodbye_garry_cooper