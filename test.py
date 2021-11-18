genders = ["man", "woman", "don't want to specify"]
ages = ["18 or less","between 18 and 25","more than 25"]
readstyles = ["Sci-fi","Biography","Horror","Romance","Fable","History","Comedy"]

for g in range(1, len(genders)):
    print("Enter", g, "for :", genders[g])
entier = False
while not entier or gender > len(genders) - 1 or gender <= 0:
    entier = False
    try:
        gender = input("What gender are you ?\n")
        gender = int(gender)
        entier = True
    except:
        print("Please enter a number between 1 and " + str(len(genders) - 1) + ".")

print(genders[gender])