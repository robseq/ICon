# GESTORE KB
# importa le librerie necessarie
from pyswip import Prolog

# Carica la KB
pl = Prolog()
pl.consult("myKB2.pl")


# Restituisce le persone obese
def query1():
    myQuery = "prop(X, is, obese)."
    project = list(pl.query(myQuery))
    for elem in project:
        query = "- "+elem["X"]+""
        print(query)


# Restituisce le persone non obese
def query2():
    myQuery = "prop(X, is, not_obese)."
    project = list(pl.query(myQuery))
    for elem in project:
        query = "- "+elem["X"]+""
        print(query)


# Restituisce le persone con peso insufficiente
def query3():
    myQuery = "prop(X, type, insufficient_weight)."
    project = list(pl.query(myQuery))
    for elem in project:
        query = "- "+elem["X"]+""
        print(query)


# Restituisce le persone con peso normale
def query4():
    myQuery = "prop(X, type, normal_weight)."
    project = list(pl.query(myQuery))
    for elem in project:
        query = "- "+elem["X"]+""
        print(query)


# Restituisce le persone sovrappese
def query5():
    myQuery = "prop(X, type, overweight)."
    project = list(pl.query(myQuery))
    for elem in project:
        query = "- "+elem["X"]+""
        print(query)


# Restituisce le persone obese di tipo 1
def query6():
    myQuery = "prop(X, type, obesity_type_1)."
    project = list(pl.query(myQuery))
    for elem in project:
        query = "- "+elem["X"]+""
        print(query)


# Restituisce le persone obese di tipo 2
def query7():
    myQuery = "prop(X, type, obesity_type_2)."
    project = list(pl.query(myQuery))
    for elem in project:
        query = "- "+elem["X"]+""
        print(query)


# Restituisce le persone obese di tipo 3
def query8():
    myQuery = "prop(X, type, obesity_type_3)."
    project = list(pl.query(myQuery))
    for elem in project:
        query = "- "+elem["X"]+""
        print(query)


# Restituisce il BMI in base alla persona
def query9():
    person = input("Inserisci la persona per trovare il suo BMI :\n")
    query = "prop(" + person + ", type, X)"
    myList = list(pl.query(query))
    for elem in myList:
        print("- " + elem["X"])


# Restituisce una persona in base ad una sua proprietà
def query11():
    commands = input("Inserisci un elemento per trovare la persona associata"
                     "1. Age, 2.Gender, 3. Height, 4. Weight, 5. Family_Overweight\n")
    if commands == '1':
        age = input("Inserisci l'età per trovare una persona: ")
        query = "prop(X, has_age, " + age + ")"
        myList = list(pl.query(query))
        for elem in myList:
            print("- " + elem["X"])
    elif commands == '2':
        gender = input("Inserisci il sesso per trovare una persona: ")
        query = "prop(X, has_gender, " + gender + ")"
        myList = list(pl.query(query))
        for elem in myList:
            print("- " + elem["X"])
    elif commands == '3':
        height = input("Inserisci un'altezza per trovare una persona: ")
        query = "prop(X, has_height, " + height + ")"
        myList = list(pl.query(query))
        for elem in myList:
            print("- " + elem["X"])
    elif commands == '4':
        weight = input("Inserisci un peso per trovare una persona: ")
        query = "prop(X, has_weight, " + weight + ")"
        myList = list(pl.query(query))
        for elem in myList:
            print("- " + elem["X"])
    elif commands == '5':
        fwo = input("Inserisci se una persona ha/avuto familiari obesi per trovarla: ")
        query = "prop(X, has_fwo, " + fwo + ")"
        myList = list(pl.query(query))
        for elem in myList:
            print("- " + elem["X"])


# Restituisce un'informazione di una persona
def query12():
    commands = input("Inserisci un elemento da cercare tra "
                     "1. Age, 2.Gender, 3. Height, 4. Weight, 5. Family_Overweight\n")
    if commands == '1':
        person = input("Inserisci la persona per sapere l'età: ")
        query = "prop(" + person + ", has_age, A)"
        myList = list(pl.query(query))
        for elem in myList:
            print(elem["A"])
    elif commands == '2':
        person = input("Inserisci la persona per sapere il suo sesso: ")
        query = "prop(" + person + ", has_gender, G)"
        myList = list(pl.query(query))
        for elem in myList:
            print("- " + elem["G"])
    elif commands == '3':
        person = input("Inserisci la persona per sapere la sua altezza: ")
        query = "prop(" + person + ", has_height, H)"
        myList = list(pl.query(query))
        for elem in myList:
            print(elem["H"])
    elif commands == '4':
        person = input("Inserisci la persona per sapere il suo peso: ")
        query = "prop(" + person + ", has_weight, W)"
        myList = list(pl.query(query))
        for elem in myList:
            print(elem["W"])
    elif commands == '5':
        person = input("Inserisci la persona per sapere se ha/avuto familiari obesi: ")
        query = "prop(" + person + ", has_fwo, F)"
        myList = list(pl.query(query))
        for elem in myList:
            print("- " + elem["F"])
