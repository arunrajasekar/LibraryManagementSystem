import sys

books = []
borrowed = 0
notBorrowed = 0
class Lms:
    
    def displayBooks():
        """        if books[0] == 'None':
            print('There are no books in the library')
        """ 
        if books: 
            for i in range(len(books)):
                if books[i][0] != '*':
                    a=print('\t', i+1, '\t', books[i])
                else:
                    a=print('\t', i+1, '\t', books[i], '- Borrowed')
        else:
            print('There are no books in the library. Please donate some books.')


    def borrowBooks(index):
        ind = index-1
        if books:
            if books[ind][0] == '*':
                print(books[ind][1:], ' has already been borrowed. Please select another book.')
                return 0
            else:
                print('You have borrowed', books[ind],'\n\t Happy reading!')
                books[ind] = '*' + books[ind]
                return 1
        else:
            print('\nThere are no books in the library. Please donate some books.\n')

    def returnBooks(rBook):
        a = 0
        for i in range(len(books)):
            if books[i][0] == '*' and (books[i][1:] == rBook):
                books[i] = books[i][1:]
                print(rBook, 'has been successfully returned')
                return 1
            else:
                a += 1
        if a == len(books):
            print('\nEnter the correct book name')
            return 0

    def addBook(book):
        books.append(book)
        return 1
print('Welcome!!!')
while(1):
    print('\n============\nEnter option\n============\n1\tDisplay the books\n2\tBorrow a book\n3\tReturn a book\n4\tAdd books\n5\tExit\n')
    option =  int(input())
    if  option == 1:
        Lms.displayBooks()
    elif option == 2:
        print('Enter the number of the book')
        index = int(input())
        Lms.borrowBooks(index)
    elif option == 3:
        rBook = input()
        Lms.returnBooks(rBook)
    elif option == 4:
        print('Enter the no. of books to add followed the name of the books')
        n = int(input())
        for _ in range(n):
            book = input()
            Lms.addBook(book)
    elif option == 5:
        print('\n\t\tThank you! Come again!')
        break
