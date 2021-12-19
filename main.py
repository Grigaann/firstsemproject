from Part1 import *
from Part2 import *
from Part3 import *

z=True

if __name__ == "__main__":

    while z==True:
        w = 0
        while w < 1 or w > 3:
            try:
                w = int(input("Hello, what do you want to do?\nEnter 1 to visit readers profile\nEnter 2 to visit the book depository\nEnter 3 to get reading recommandations\n"))
            except:
                print('Please, enter a valid integer between 1 and 3\n')
                z = stop()


        #===================================================================================================================
        if w==1:
            n=0
            while n<1 or n>4:
                # display with 4 categories of part 1
                try:
                    n = int(input("Press 1 if you want to create an account.\n"
                                  "Press 2 if you want to view a reader's profile.\n"
                                  "Press 3 if you want to edit a reader's profile.\n"
                                  "Press 4 if you want to delete a reader's profile.\n"))
                except:
                    print('Enter a valid integer between 1 and 4')
                    z = stop()

            if n == 1: #part1 loop
                print(add_reader())
                z = stop()

            elif n==2: #showing all profiles
                n = DisplayAllReaders()
                print(n)
                print(display_reader(input('Which profile do you want to see ?\n')))
                z = stop()

            elif n==3:
                n = DisplayAllReaders()
                print(n)
                print(edit_reader())
                z=stop()


            elif n==4:
                n = DisplayAllReaders()
                print(n)
                print(delete_reader(input('Which profile do you want to delete ?\n')))
                z = stop()

        #========================================================================================================
        elif w==2:
            try:
                    # display with 3 categories of part 2
                n=int(input("Press 1 if you want to display all listed books.\n"
                  "Press 2 if you want to add a book.\n"
                  "Press 3 if you want to modify a title.\n"
                  "Press 4 if you want to delete a book.\n"))
            except:
                print('Enter a valid integer between 1 and 4')
                z = stop()

            if n==1:
                display_books()
            elif n==2:
                print(add_book(input("Please type the name of the book you want to add : ")))
                z = stop()
            elif n==3:
                display_books()
                print(modify_title(input("Please type the line of the book you want to update : ")))
                z = stop()
            elif n==4:
                display_books()
                print(delete_book(input("Please type the line of the book you want to delete : ")))
                z = stop()

        #===================================================================================================================
        elif w==3:
        #display with 2 categories of part 3
            n=0
            while not 0 < n <= 1:
                try:

                    n=int(input("Press 1 if you want to rate a book.\n"))

                except:
                    print('Please, enter 1, it is the only possible input.')
                    z = stop()
            if n==1:

                readers_pseudonym_str= 'bob'
                while not readers_pseudonym_str in list_readers()[0]: #asking user for pseudonym and verifying
                    try:
                        readers_pseudonym_str = str(input("What's your pseudonym?\n")) #rate a book, collecting pseudonym and title of the reader
                        readers_pseudonym_int= finding_id_reader(readers_pseudonym_str)+1

                    except:
                        print("This isn't a pseudonym.")
                        z = stop()

                if readers_pseudonym_str in list_readers()[0]:  #verif and showing books
                    # showing all books to the user to choose from
                    book_title_id = -1

                    while not book_title_id in range(len(list_books())+1): #verif book id is in range
                        try:
                            display_books()  #displaying all the books to choose from

                            book_title_id = int(input("Which title of a book you want to rate?\n" #verifying input
                                                   "Enter his title number\n"))
                        except:
                            print('Enter a value between 1 and ',lenght_books()-1,'.')

                    book_title_str = finding_title_book(book_title_id)   #converting the book number to his title
                    grade_book = -2
                    if book_title_str in list_books():  #getting ready with parameters for the matrix
                        while not -1<grade_book<6: #defining range for the grade and working
                            try:
                                grade_book = int(input('Which grade do you want to give to this book? between 0 and 5, 5 being the best grade.\n'))
                            except:
                                grade_book= int(input('Enter a value between 0 and 5, 5 being the best grade.\n'))
