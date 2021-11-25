from Part2 import display_books


def add_reader():

    #Add the sign-in user infos

    #different available choices
    genders = ["", "man", "woman", "don't want to specify"]
    ages = ["", "18 or less", "between 18 and 25", "more than 25"]
    readstyles = ["", "Sci-fi", "Biography", "Horror", "Romance", "Fable", "History", "Comedy"]

    readersfile = open("./Ressources/readers.txt", "a")
    book = open("./Ressources/books.txt","r")
    booksread = open("./Ressources/booksread.txt","a")


    pseudo = str(input("What is your pseudonym ?\n"))

    #asking for the gender of the new user
    for g in range(1, len(genders)):
        print("Enter", g, "for :", genders[g])
    entier = False
    while not entier or gender > len(genders) - 1 or gender <= 0:
        entier = False
        try:
            gender = input("What is your gender ?\n")
            gender = int(gender)
            entier = True
        except:
            print("Please enter a number between 1 and " + str(len(genders) - 1) + ".")

    # asking for the age of the new user
    for a in range(1, len(ages)):
        print("Enter", a, "if you are", ages[a])
    entier = False
    while not entier or age > len(ages) - 1 or age <= 0:
        entier = False
        try:
            age = input("How old are you ?\n")
            age = int(age)
            entier = True
        except:
            print("Please enter a number between 1 and " + str(len(ages) - 1) + ".")

    # asking for the reading style of the new user
    for r in range(1, len(readstyles)):
        print(r, ":", readstyles[r])
    entier = False
    while not entier or readstyle > len(readstyles) - 1 or readstyle <= 0:
        entier = False
        try:
            readstyle = input("What reading style do you prefer (enter the corresponding number) ?\n")
            readstyle = int(readstyle)
            entier = True
        except:
            print("Please enter a number between 1 and " + str(len(readstyles) - 1) + ".")


    #Add the books the newby already read


    display_books()
    users_books = ""
    book_nb = 1

    while book_nb!=0:
        book_nb = int(input("Enter the number corresponding to a book you have read or 0 if you are done :\n"))
        while sum(1 for line in open("./Ressources/books.txt")) < book_nb or book_nb < 0:
            book_nb = int(input("Enter a valid answer :\n"))
        if book_nb!=0 and str(book_nb) not in users_books:
            users_books += (","+str(book_nb))
    booksread.write(pseudo + users_books + "\n")
    #writing in the readers.txt
    readersfile.write(pseudo + "," + str(gender) + "," + str(age) + "," + str(readstyle) + "\n")
    readersfile.close()

    return


def display_reader():
    return


def edit_reader():
    return


def delete_reader():
    return