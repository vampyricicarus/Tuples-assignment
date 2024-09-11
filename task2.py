# task 1

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

newBook = ("Harry Potter and the Sorcerer's Stone", "JK Rowling")

def addBooks():
    userBook = (input("Book title: "), input("Author: "))
    library.append(newBook)
    if userBook not in library:
        library.append(userBook)
    else: 
        print("Book already exists")
    print(library)
    return
addBooks()
    