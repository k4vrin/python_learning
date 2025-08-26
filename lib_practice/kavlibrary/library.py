
def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    pages = input("Enter the number of pages in the book: ")
    with open("books.txt", "a") as f:
        f.write(f"{title},{author},{pages}\n")

def remove_book():
    title = input("Enter the title of the book to remove: ")
    with open("books.txt", "r") as f:
        lines = f.readlines()

def search_book():
    title = input("Enter the title of the book to search for: ")
    with open("books.txt", "r") as f:
        for line in f:
            if title in line:
                print(line)
                break
        else:
            print("Book not found")

def list_books():
    with open("books.txt", "r") as f:
        for line in f:
            print(line)

