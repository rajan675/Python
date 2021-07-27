class Library:
    def __init__(self, list, name):
        self.bookList = list
        self.name = name
        self.lendDict = {}
    def displayBook(self):
        print(f"We have following book in our Library : {self.name}")
        for book in self.bookList:
            print(book)
    def lendBook(self, user, book):
        if book  not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender Book Database has been updated. You can take the Book ")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")
    def addbook(self, book):
        self.bookList.append(book)
        print("The book has been added to the Booklist")
    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ =='__main__':
    rajan = Library(['Python', 'Rich Dad Poor Dad','Harry Potter','C++','Data Structure Using C','Discrete Math'], "Rajan's")

while (True):
    print(f"Welcome to the {rajan.name} Library ")
    print("Enter your choice to continue")
    print("1. Display Book")
    print("2. Lend Book")
    print("3. Add Book")
    print("4. Return Book")
    user_choice = input()
    if user_choice not in ['1','2','3','4']:
        print("Please enter a valid option")
        continue
    else:
        user_choice = int(user_choice)

    if user_choice == 1:
        rajan.displayBook()
    elif user_choice == 2:
        user = input("Enter your name ")
        book = input("Enter the name of Book you want to lend : ")
        rajan.lendBook(user, book)
    elif user_choice == 3:
        book = input("Enter the name of book you want to add : ")
        rajan.addbook(book)
    elif user_choice == 4:
        book = input("Enter the name of book you want to return : ")
        rajan.returnBook(book)
    else:
        print("Enter a valid option")
    print("Press q to quit and c to continue")
    user_choice2 = ""
    while user_choice2 != 'q' and user_choice2 != 'c':
        user_choice2 = input()
        if user_choice2 == 'q':
            exit()
        elif user_choice2 == 'c':
            continue