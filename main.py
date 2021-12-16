from Part1 import *
from Part2 import *
from Part3 import *

if __name__ == "__main__":
    w = int(input("Hello, what do you want to do?\nEnter 1 to visit readers profile\nEnter 2 to visit the book depository\nEnter 3 to get reading recommandations\n"))
    while w<1 or w>3:
        # principal display with 2 main categories
        w=int(input("Please enter a number between 1 and 3 :\n"
                    "1/ Visit readers profile\n"
                    "2/ Visit the book depository\n"
                    "3/ Get reading recommandations\n"))

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

        if n == 1: #part1 loop
            print(add_reader())

        elif n==2: #showing all profiles
            n = DisplayAllReaders()
            print(n)
            print(display_reader(input('Which profile do you want to see ?\n')))

        elif n==3:
            n = DisplayAllReaders()
            print(n)
            print(edit_reader())

        elif n==4:
            n = DisplayAllReaders()
            print(n)
            print(delete_reader(input('Which profile do you want to delete ?\n')))

    #===================================================================================================================
    elif w==2:
            # display with 3 categories of part 2
        n=int(input("Press 1 if you want to display all listed books.\n"
              "Press 2 if you want to add a book.\n"
              "Press 3 if you want to modify a title.\n"
              "Press 4 if you want to delete a book.\n"))

        if n==1:
            display_books()
        elif n==2:
            print(add_book(input("Please type the name of the book you want to add : ")))
        elif n==3:
            display_books()
            print(modify_title(input("Please type the line of the book you want to update : ")))
        elif n==4:
            display_books()
            print(delete_book(input("Please type the line of the book you want to delete : ")))

    #===================================================================================================================
    elif w==3:
        #display with 2 categories of part 3
        print("We're late, we are not done yet")