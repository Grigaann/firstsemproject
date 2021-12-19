reader_file = "./Ressources/readers.txt"
books = open("./Ressources/books.txt",'r')
from Part1 import *
from Part2 import *

from useful_fonctions import *
'''
def rate_book():
    pseudonym=input("What's your pseudonym?\n")
    list1 = []
    with open(reader_file, 'r') as file:  # taking pseudos from readers and converting them into a list
        for line in file:
            p = line.split(',')
            list1.append(p[0])

        display_books()
    if pseudonym in list1:
        #showing all books to the user to choose from
        book_title=int(input("Which title of a book you want to rate?\n"
                         "Enter his Identification number"))
        display_books()
        if book_title in list2:
            matrix_creation(pseudonym,book_title)
        else:
            print("This book title isn't in our database, you could register it.")
    else:
         print("Your pseudonym isn't in our database, please register first.")
'''
def suggest_book():
    return

def matrix_creation():

    list3=[]
    for j in range(lenght_books()):
        list3.append([0]*list_readers()[1])

    return list3  #creating a matrix line=readers col=books


matrix= matrix_creation()

def matrix_update(matrix,readers_pseudonym, book_title,grade_book):
    matrix[book_title][readers_pseudonym] = grade_book
    return matrix
