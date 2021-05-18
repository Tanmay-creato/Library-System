
class Library:
    def __init__(self,listofbooks):
        self.books = listofbooks

    print("Please enter your details --> ")
    name = input("Enter your name --> ")
    Class = int(input("Enter your class --> "))
    if Class <=12 or Class <=1:
        print("Valid Class")
    else:
        exit()
    def DisplayListOfBooks(self,):
        print("Books present")
        for book in self.books:
            print(" * " + book)

    def BorrowBook(self,bookName):
        if bookName in self.books:
            print(f"Your Book {bookName} has been issued to you , you have to return it in 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry ! Your book is not available now . Please try again")
            return False
    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Your book is successfully returned")
class student:
    def borrowBook(self):
        self.book = input("Enter which book do you want --> ")
        return self.book
    def returnBook(self):
        self.book = int(input("Enter the number of book -->  "))
        return self.book
if __name__ == "__main__":
    library = Library(["Flask", "Python", "Django", "Java", "Javascript", "HTML", "CSS", "C++", "C#"])
    Student = student()

while True:
    welcomeMsg = """ ************************** WELCOME TO TANMAY'S CENTRAL LIBRARY **************************
    ||Choose The Options||
    1.List all the books 
    2.Borrow Book
    3.Return Book
    4. Exit
    """
    print(welcomeMsg)

    a = int(input("Enter a choice --> "))
    if a == 1:
        library.DisplayListOfBooks()
    elif a == 2:
        library.BorrowBook(Student.borrowBook())
    elif a == 3:
        library.returnBook(Student.returnBook())
    elif a == 4:
        print("Thanks for coming to my library. Please visit again.")
        exit()
