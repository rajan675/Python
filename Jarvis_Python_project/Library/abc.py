 class Library:
    def __init__(self, list, name):
        self.bookList = list
        self.name = name
        self.lenDict = {}

    def displayBook(self):
        print(f"We have following books in {self.name}s  Library ")
        for book in self.bookList:
            print(book)
    def lendBook(self, user, book):
        if book not in self.lenDict.keys():
            self.lenDict.update({book:user})
            print("You can take the Book")
        else:
            print(f"Sorry! The book is already taken by {self.lendDict[book]} ")
    def addBook(self, book):
        self.bookList.append(book)
        print("The book has been added")
    def returnBook(self, book):
        self.lenDict.pop(book)

if name == '__main__':
    while(True):
        print(f"     Welcome to the {self.name}s Library  ")
        print("Enter your choice ")
        print("1. Display Book")
        print("2. Lend Book")
        print("3. Add Book")
        print("4. Return Book")
        user_Choice = input()
        if user_Choice != ['1','2','3','4']:
            print("Enter a valild option")
            continue
        else:
            user_Choice = int(user_Choice)
        if user_Choice == 1:
            rajan.displayBook()
        elif user_Choice == 2:
            print("Enter your name ")
            print("Enter the name of book you want to lend ")
            rajan.lendBook(user, book)
        elif user_Choice == 3:
            print("Enter the name of book you want to  add ")
            rajan.addBook(book)
        elif user_Choice == 4:
            print("Enter the name of book you want to return ")
            rajan.returnBook(book)
        else:
            print("Enter a valid option")
        user_Choice2 = input("Enter q to Quit and c to Continue")
        user_Choice2 = ""
        if user_Choice2 !='q' and user_Choice2 != 'c':
            print("Enter a valid option")
            user_Choice2 = input()

        if user_Choice2 == 'q':
            exit()
        else:
            continue