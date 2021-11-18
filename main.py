reader_file = "./Ressources/readers.txt"


def add_reader():
    genders = ["", "man", "woman", "don't want to specify"]
    ages = ["", "18 or less", "between 18 and 25", "more than 25"]
    readstyles = ["", "Sci-fi", "Biography", "Horror", "Romance", "Fable", "History", "Comedy"]

    readersfile = open(reader_file, "a")
    pseudo = str(input("What is your pseudonym ?\n"))

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

    readersfile.write(pseudo + "," + str(gender) + "," + str(age) + "," + str(readstyle) + "\n")
    readersfile.close()
    return pseudo + "," + genders[gender] + "," + ages[age] + "," + readstyles[readstyle]


print(add_reader())
