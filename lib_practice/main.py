from kavlibrary import library

if __name__ == "__main__":
# Use library
    user_input = input("Enter a command (add, remove, search, list): ")
    if user_input == "add":
        library.add_book()
    elif user_input == "remove":
        library.remove_book()
    elif user_input == "search":
        library.search_book()
    elif user_input == "list":
        library.list_books()
    else:
        print("Invalid command")