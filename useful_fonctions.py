reader_file = "./Ressources/readers.txt"
books = open("./Ressources/books.txt",'r')

def lenght_readers():
    list1 = []
    with open(reader_file, 'r') as file:  # taking pseudos from readers and converting them into a list
        for line in file:
            p = line.split(',')
            list1.append(p[0])
