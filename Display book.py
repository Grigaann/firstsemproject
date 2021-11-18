b = open("./Ressources/booksread.txt","r")
def display_books():
    for i in b.readlines():
        print(i)

print(display_books())
