books_file = "./Ressources/books.txt"



def display_books():
    booksfile = open(books_file, "r")
    for i in booksfile.readlines():
        print(i.rstrip('\n'))
    booksfile.close()
    return

#=======================================================================================================================

def add_book(book):
    booksfile = open(books_file, "r")
    lignes = booksfile.readlines()
    final_line_nb = int(lignes[-1][:lignes[-1].find(" "):]) + 1
    display = ""
    for ligne in lignes:
        if book == ligne[ligne.find("- ")+2:-1:]:
            display = "This book is already registered."
    booksfile.close()
    if display == "":
        verif = ""
        while verif != "yes" and verif != "no":
            verif = str(input("Are you sure you want to add '" + book + "' ? Type 'Yes' or 'No'.\n")).lower()
        if verif == "yes":
            booksfile = open(books_file, "a")
            booksfile.write(str(final_line_nb) + " - " + book+"\n")
            booksfile.close()
            display = "Book successfully added."
        else:
            display = book + " has not been added."
    return display

#=======================================================================================================================

def modify_title(book):
    verif = ""
    txt = ""
    line_nb = 1
    with open(books_file) as file:
        for line in file:
            if book == line[:line.find('-')-1:]:
                selected_book = line[line.find("- ")+2:-1:]
                txt += str(line_nb) + " - " + input("Please enter the new title for '"+selected_book+"' : ") + "\n"
                while verif != "yes" and verif != "no":
                    verif = str(input("Are you sure you want to save your changes ? Type 'yes' or 'no'.\n")).lower()
            else:
                txt += str(line_nb)+line[line.find(" - ")::]
            line_nb+=1
    if verif == "yes":
        booksfile = open(books_file, "w")
        booksfile.write(txt)
        booksfile.close()
        display = "Book successfully updated."
    elif verif == "no":
        display = selected_book+" has not been modified."
    else:
        display = "This number is not related to a book."
    return display

#=======================================================================================================================

def delete_book(book):
    verif = ""
    txt = ""
    line_nb = 1
    with open(books_file) as file:
        for line in file:
            if book == line[:line.find('-')-1:]:
                selected_book = line[line.find("- ")+2:-1:]
                while verif != "yes" and verif != "no":
                    verif = str(input("Are you sure you want to permanently remove '" + selected_book + "' ? Type 'yes' or 'no'.\nBe careful : This operation can NOT be undone.\n")).lower()
            else:
                txt += str(line_nb)+line[line.find(" - ")::]
                line_nb+=1
    if verif == "yes":
        booksfile = open(books_file, "w")
        booksfile.write(txt)
        booksfile.close()
        display = "Book successfully deleted."
    elif verif == "no":
        display = selected_book+" has not been deleted."
    else:
        display = "This number is not related to a book. Please try again later. :)"
    return display
