reader_file = "./Ressources/readers.txt"
bookss = open("./Ressources/books.txt",'r')


from Part2 import *

def list_readers():
    list1 = []
    cpt=0
    with open(reader_file, 'r') as file:  # taking pseudos from readers and converting them into a list
        for line in file:
            p = line.split(',')
            list1.append(p[0])
            cpt= cpt+1
    return list1,cpt

def finding_id_reader(pseudonym):
    listz= list_readers()[0]
    for j in range(len(listz)):
        if listz[j]== pseudonym:
            pseudonym_id = j
            return pseudonym_id  #returns id of a rider-1 in list composed of only pseudos [from list_reader()]


def list_books():
    list2=[] #taking books from books file and converting into a list and taking ONLY the title
    cpt=0
    delete_from=3
    bookss = open("./Ressources/books.txt", 'r')
    with bookss as file:
        for i in file:
            if cpt>8:       #deleting the part before title, there 3 char
                delete_from=5
                a=i[delete_from:].strip()
                list2.append(a)
            elif cpt <9:     #deleting the part before title, there 4 char
                a = i[delete_from:].strip()
                list2.append(a)

                cpt = cpt + 1
            else:
                print('Out of our stock, please delete some books.')
    bookss.close()
    return list2

def finding_title_book(book_id):
    listz= list_books()
    book_title= listz[book_id-1]
    return book_title
       #returns title of a books_id in list composed of only book_title [from list_books()]

def finding_id_book(title):
    listz= list_books()
    for j in range(len(listz)):
        if listz[j]== title:
            book_id = j
            return book_id

def lenght_books():
    line_cpt = 1
    booksfile = open(books_file, "r")
    for i in booksfile.readlines():
        line_cpt += 1
    booksfile.close()
    return line_cpt

lenght_of_books = lenght_books()

def stop():
    z = True
    try:
        z=int(input("If you want to stop the program press 9.\n"
                      "Otherwise, press any button.\n"))
        if z == 9:
            z = False
            print("Thank's for using this very nice program made with love.")
        else:
            z=True
    except:
            pass
    return z
