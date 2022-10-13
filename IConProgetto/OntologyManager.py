# GESTORE ONTOLOGIA
# Importa le librerie essenziali per l'ontologia
import owlready2 as owl


# Carica l'ontologia
def load():
    print("ONTOLOGIA\n")
    onto = owl.get_ontology("OntologiaProgetto.owl").load()

    return onto


# Restituisce il contenuto principale dell'ontologia
def query1(onto):
    print("Lista delle classi principali nell'ontologia: \n")
    print(list(onto.classes()), "\n")


# Restituisce la lista delle persone presenti nell'ontologia
def query2(onto):
    print("Lista Persone nella ontologia:\n")
    person = onto.search(is_a=onto.Person)
    print(person, "\n")


# Restituisce la lista dei tipi di BMI
def query3(onto):
    print("Lista tipologie BMI:\n")
    bmi = onto.search(is_a=onto.BodyMassCondition)
    print(bmi, "\n")


# Restituisce la lista delle tipologie di condizioni fisiche
def query4(onto):
    print("Lista tipologie condizioni fisiche:\n")
    obese = onto.search(is_a=onto.ObeseCondition)
    print(obese, "\n")


# Restituisce la lista delle tipologie di abitudini alimentari
def query5(onto):
    print("Lista tipologie abitudini alimentari:\n")
    ehabits = onto.search(is_a=onto.EatingHabits)
    print(ehabits, "\n")


# Restituisce la lista delle tipologie di condizioni di attività fisiche
def query6(onto):
    print("Lista tipologie condizioni di attività fisiche:\n")
    phycond = onto.search(is_a=onto.PhysicalActivityCondition)
    print(phycond, "\n")


# Esempio di query sull'ontologia
def query7(onto):
    print("Lista di persone che hanno le abitudini alimentari di tipo 2:\n")
    obesePerson = (onto.search(is_a=onto.Person, hasEatingHabits=onto.search(is_a=onto.eating_habits_2)))
    print(obesePerson, "\n")

