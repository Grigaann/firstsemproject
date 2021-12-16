reader_file = "./Ressources/readers.txt"
from Part2 import display_books

#different available choices
genders = ["", "man", "woman", "don't want to specify"]
ages = ["", "18 or less", "between 18 and 25", "more than 25"]
readstyles = ["", "sci-fi", "biography", "horror", "romance", "fable", "history", "comedy"]


def add_reader():
    pseudo = ","
    while "," in pseudo:
        pseudo = str(input("What is your pseudonym ?\n"))

    display = ""
    for ligne in open(reader_file,"r").readlines():
        if pseudo == ligne.split(",")[0]:
            display = "This user is already registered."

    if display == "":
        #asking for the gender of the new user
        for g in range(1, len(genders)):
            print("Enter", g, "for :", genders[g])
        gender = -1
        while gender > len(genders) - 1 or gender <= 0:
            try:
                gender = int(input("What is your gender ?\n"))
            except:
                print("Please enter a number between 1 and " + str(len(genders) - 1) + ".")

        # asking for the age of the new user
        for a in range(1, len(ages)):
            print("Enter", a, "if you are", ages[a])
        age = -1
        while age > len(ages) - 1 or age <= 0:
            try:
                age = int(input("How old are you ?\n"))
            except:
                print("Please enter a number between 1 and " + str(len(ages) - 1) + ".")

        # asking for the reading style of the new user
        for r in range(1, len(readstyles)):
            print(r, ":", readstyles[r])
        readstyle = -1
        while readstyle > len(readstyles) - 1 or readstyle <= 0:
            try:
                readstyle = int(input("What reading style do you prefer (enter the corresponding number) ?\n"))
            except:
                print("Please enter a number between 1 and " + str(len(readstyles) - 1) + ".")

        nb_stored_books = display_books()
        books_lus = []
        deja_lu = -1
        while deja_lu != 0:
            deja_lu = int(input("Enter the number corresponding to a book you have read or 0 if you are done.\n"))
            while deja_lu < 0 or deja_lu > nb_stored_books:
                deja_lu = int(input("Please enter a valid number or 0 if you are done.\n"))
            if deja_lu != 0 and deja_lu not in books_lus:
                books_lus.append(str(deja_lu))
        print(books_lus)

        #writing in the readers.txt
        readersfile = open(reader_file, "a")
        readersfile.write(pseudo + "," + str(gender) + "," + str(age) + "," + str(readstyle) + "\n")
        readersfile.close()
        #writing in the booksread.txt
        booksreadfile = open("./Ressources/booksread.txt","a")
        booksreadfile.write(pseudo + "," + ",".join(books_lus)+"\n")
        booksreadfile.close()

        display = pseudo + "'s profile was successfully added."
    return display

#=======================================================================================================================

def display_reader(reader):
    Bool = False
    with open(reader_file) as file:
        for line in file:
            if reader in line:
                profile = line.split(',')[1::]
                Bool = True
    if Bool:
        if genders[int(profile[0])] == genders[3]:
            display = reader+" dosent want to share his/her gender, he/she is"+ages[int(profile[1])]+", and preferes the style "+readstyles[int(profile[2])]+"."
        else:
            display = reader+" is a "+genders[int(profile[0])] +", "+ages[int(profile[1])]+", who preferes the style "+readstyles[int(profile[2])]+"."
    else:
        display = "Error : this profile does not exist."
    return display

#=======================================================================================================================

def edit_reader():
    profile = input('Which profile do you want to edit ?\n')
    while profile not in DisplayAllReaders().split(", "):
        profile = input('Which profile do you want to edit ?\n')
    choice = int(input("You are going to edit "+profile+"'s profile.\n"
                       "Which part do you want to modify?\n"
                       "Enter : 1 for the pseudonym,\n"
                       "        2 for the gender,\n"
                       "        3 for the age,\n"
                       "        4 for the reading style.\n"))
    while choice > 5 or choice < 0:
        choice = int(input("Please enter a number between 1 and 4 to modify the corresponding category.\n"
                           "1) the pseudonym\n"
                           "2) the gender\n"
                           "3) the age\n"
                           "4) the reading style.\n"))

    with open(reader_file,'r') as file:
        txt = ""
        readerfile = file.readlines()
        Bool = False
        for lignes in readerfile:
            readerparameters = lignes.split(",")
            if profile == readerparameters[0]:
                Bool = True
                if choice == 1:
                    current_param = profile
                    print("The current pseudonym is : "+current_param)
                    pseudo = ","
                    while "," in pseudo:
                        pseudo = str(input("Please enter "+profile+"'s new pseudonym : "))
                    not_verified_txt = pseudo + lignes[lignes.find(",")::]
                    new_param = pseudo
                if choice == 2:
                    current_param = ages[int(readerparameters[1])]
                    print(profile + "'s current age is : " + current_param)
                    for g in range(1, len(genders)):
                        print("Enter", g, "for :", genders[g])
                    gender = -1
                    while gender > len(genders) - 1 or gender <= 0:
                        gender = int(input("Please enter the modified gender : "))
                    not_verified_txt = readerparameters[0] + "," + str(gender) + "," + readerparameters[2] + "," + readerparameters[3]
                    new_param = genders[gender]
                if choice == 3:
                    current_param = ages[int(readerparameters[2])]
                    print(profile+"'s current age is : " + current_param)
                    for a in range(1, len(ages)):
                        print("Enter", a, "if "+profile+" is", ages[a])
                    age = -1
                    while age > len(ages) - 1 or age <= 0:
                        age = int(input("How old is "+profile+" ?\n"))
                    not_verified_txt = readerparameters[0] + "," + readerparameters[1] + "," + str(age) + "," + readerparameters[3]
                    new_param = ages[age]
                if choice == 4:
                    current_param = readstyles[int(readerparameters[3])]
                    print(profile + "'s current prefered reading style is : " + current_param)
                    for r in range(1, len(readstyles)):
                        print(r, ":", readstyles[r])
                    readstyle = -1
                    while readstyle > len(readstyles) - 1 or readstyle <= 0:
                        readstyle = int(input("Please enter " + profile + "'s new reading style : "))
                    not_verified_txt = readerparameters[0] + "," + readerparameters[1] + "," + readerparameters[2] + "," + str(readstyle)
                    new_param = readstyles[readstyle]
                verif = ""
                while verif != "yes" and verif != "no":
                    verif = str(input("Are you sure you want to change " + profile + "'s parameter ?\n"
                                      "The current information is '" + current_param + "' and you want to set it to '"+new_param+"'.\n"
                                      "Type Yes or No : ")).lower()
                if verif == "yes":
                    txt += not_verified_txt + "\n"
                    display = profile + "'s profile successfully updated."
                else:
                    txt += lignes
                    display = profile + "'s profile has not been modified."
            else:
                txt+=lignes
    if Bool:
        readersfile = open(reader_file, "w")
        readersfile.write(txt)
        readersfile.close()
    else:
        display = "Error : this profile does not exist."
    return display

#=======================================================================================================================

def delete_reader(reader):
    txt = ""
    Bool = False
    with open(reader_file) as file:
        for line in file:
            if reader == line[:line.find(",")]:
                Bool = True
            else:
                txt += line
    if Bool:
        verif = ""
        while verif != "yes" and verif != "no":
            verif = str(input("Are you sure you want to permanently remove "+reader+" ?\n"
                              "Be careful : This operation can NOT be undone.\nType Yes or No : ")).lower()
        if verif == "yes":
            readersfile = open(reader_file, "w")
            readersfile.write(txt)
            readersfile.close()
            display = "Profile successfully deleted."
        else:
            display = reader+" has not been deleted."
    else:
        display = "Error : this profile does not exist."
    return display

#=======================================================================================================================

def DisplayAllReaders():
    with open(reader_file) as file:
        p = ''
        for line in file:
            p += line.split(',')[0] + ', '
    return p.rstrip(', ')