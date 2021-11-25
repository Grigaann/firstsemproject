reader_file = "./Ressources/readers.txt"
#Reader profiles interface

def add_reader():
#different available choices
    genders = ["", "man", "woman", "don't want to specify"]
    ages = ["", "18 or less", "between 18 and 25", "more than 25"]
    readstyles = ["", "Sci-fi", "Biography", "Horror", "Romance", "Fable", "History", "Comedy"]

    readersfile = open(reader_file, "a")


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

#writing in the readers.txt
    readersfile.write(pseudo + "," + str(gender) + "," + str(age) + "," + str(readstyle) + "\n")
    readersfile.close()
#later usage?
    return pseudo + "," + genders[gender] + "," + ages[age] + "," + readstyles[readstyle]+"\n"

def display_reader():
    return

def edit_reader():
    return

def delete_reader():
    return