# Create Library Class

# Methods
# 1. all book display
# 2. customer lending book (who owns the book if not present in library)
# 3. donate book (addbook function)
# 4. return book

# HarryLibrary= Library(listofbooks,library_name) init

# dict mentain (key books, value-nameof person)
# create main function and run an infinte while loop asking users for their input

class Library:

    def __init__(self,listofbooks,library_name):
        self.listofbooks=listofbooks
        self.library_name=library_name
        self.dict1={}

    def printdetails(self):
        return f"{self.library_name} has following books:\n {self.listofbooks}"

    def lending_book(self):
        bookname=''
        name=input("Please enter your name :")
        book = input("please enter book name which you want issue from library :").lower()
        bookname=bookname+book
        if bookname in [*self.dict1]:
            print(f"Sorry!!! this book issued already by {self.dict1[bookname]}\n It will available after 7 days")
        else:
            print("book issued successfully. please return it after 7 days")
            self.dict1.update({bookname:name})

    def donate_book(self):
        input2=input("Please enter book name which you want to donate :")
        self.listofbooks.append(input2)
        print("thanks for donation")

    def return_book(self):
        name = input("Please enter your name :")
        book = input("please enter book name which you want return:").lower()
        self.dict1.pop(book)
        print("return successful")

def main():

    books=["Ikigai","attitude is everything","alchemist","indian army","who will cry when you die","half girlfriend",
       "1 night at call center","2 states","five point someone"]
    lalbaug = Library(books, "lalbaug")
    print(f"Welocome to {lalbaug.library_name} library!!!!!!!!!!")

    quit1=False
    while (quit1!=True):
        option = int(input("kindly select options below:\n 1. Display Books\n 2.lending book\n 3.donate book\n 4.return book\n 5.exit\n"))
        if option==5:
            quit1=True
        elif option==3:
            lalbaug.donate_book()
        elif option==1:
            print(lalbaug.printdetails())
        elif option==2:
            lalbaug.lending_book()
        elif option==4:
            lalbaug.return_book()

if __name__=="__main__":
    main()