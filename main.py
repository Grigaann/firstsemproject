from Part1 import *
response=3
books= open("./Ressources/books.txt", "r")

if __name__ == "__main__":
    while response <0 or response>2:
        response=int(input('Welcome user.\n'   #beginning interface
          'If you want to watch the riders profiles, press 0.\n'
          'If you want to visit the book depository, press 1.\n'
          'If you want to watch our recommendations, press 2.\n'))
    #add_reader()

    if response == 0: #shows reader profiles
        pass
        #reader_profile()
    elif response == 1:  #shows all the books avaible
        print(books.read())
    else:    #recommends a book
        pass

    books.close()