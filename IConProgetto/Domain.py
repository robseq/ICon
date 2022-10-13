# DOMINIO
# importa le librerie necessarie
import Domain as dm
import OntologyManager as om
import KBManager as gkb


# Stampa il menu della scelta dominio
def menu():
    print(" --------------------------------------- MENU' DOMINIO ----------------------------------------------\n"
          "|  Qui puoi selezionare come visualizzare il dominio di interesse:                                   |\n"
          "|  1. Knowledge Base in Prolog                                                                       |\n"
          "|  2. Ontologia con owlready2                                                                        |\n"
          "|  3. Esci                                                                                           |\n"
          " ---------------------------------------------------------------------------------------------------- \n")

    commands = input()
    if commands == 'help':
        dm.menu()
    elif commands == '1':
        dm.menuKB()
    elif commands == '2':
        dm.menuOWL()
    elif commands == '3':
        print("A presto!")
        return 0
    else:
        print("Non riesco a trovare questo comando! Consulta la lista dei comandi e riprova.")
        dm.menu()


# Stampa il menù delle query in prolog
def menuKB():
    print(" --------------------------------------- MENU' PROLOG -----------------------------------------------\n"
          "|  Qui puoi selezionare le informazioni da visualizzare tramite query prolog:                        |\n"
          "|  1. Visualizza le persone obese                                                                    |\n"
          "|  2. Visualizza le persone non obese                                                                |\n"
          "|  3. Cerca una persona in base al suo livello di BMI                                                |\n"
          "|  4. Cerca il livello di bmi di una persona                                                         |\n"
          "|  5. Cerca una persona in base ad un'informazione                                                   |\n"
          "|  6. Cerca un'informazione relativa ad una persona                                                  |\n"
          "|  7. Torna al menu' dominio                                                                         |\n"
          "|  8. Esci                                                                                           |\n"
          " ---------------------------------------------------------------------------------------------------- \n")

    commands2 = input()
    if commands2 == 'help':
        om.menu()
    elif commands2 == '1':
        gkb.query1()
        dm.menuKB()
    elif commands2 == '2':
        gkb.query2()
        dm.menuKB()
    elif commands2 == '3':
        print("Scegli un BMI tra: 1. Insufficient_Weight, 2. Normal_Weight, 3. Overweight, "
              "4. Obesity_Type_1, 5. Obesity_Type_2, 6. Obesity_Type_3\n")
        commands3 = input()
        if commands3 == '1':
            gkb.query3()
            dm.menuKB()
        elif commands3 == '2':
            gkb.query4()
            dm.menuKB()
        elif commands3 == '3':
            gkb.query5()
            dm.menuKB()
        elif commands3 == '4':
            gkb.query6()
            dm.menuKB()
        elif commands3 == '5':
            gkb.query7()
            dm.menuKB()
        elif commands3 == '6':
            gkb.query8()
            dm.menuKB()
        else:
            print("Non riesco a trovare questo comando! Consulta la lista dei comandi e riprova.")
            dm.menuKB()
    elif commands2 == '4':
        gkb.query9()
        dm.menuKB()
    elif commands2 == '5':
        gkb.query11()
        dm.menuKB()
    elif commands2 == '6':
        gkb.query12()
        dm.menuKB()
    elif commands2 == '7':
        dm.menu()
    elif commands2 == '8':
        print("A presto!")
        return 0
    else:
        print("Non riesco a trovare questo comando! Consulta la lista dei comandi e riprova.")
        dm.menuKB()


# Stampa il menu delle query in owlready2
def menuOWL():
    print(" --------------------------------------- MENU' ONTOLOGIA --------------------------------------------\n"
          "|  Qui puoi selezionare le informazioni da visualizzare tramite query owlready2:                     |\n"
          "|  1. Mostra il contenuto principale dell'ontologia                                                  |\n"
          "|  2. Mostra le persone presenti nell'ontologia                                                      |\n"
          "|  3. Mostra le tipologie di BMI nell'ontologia                                                      |\n"
          "|  4. Mostra le tipologie di condizioni fisiche                                                      |\n"
          "|  5. Mostra le tipologie di abitudini alimentari                                                    |\n"
          "|  6. Mostra le tipologie di condizioni di attività fisiche                                          |\n"
          "|  7. Esempio di query                                                                               |\n"
          "|  8. Torna al menu' dominio                                                                         |\n"
          "|  9. Esci                                                                                           |\n"
          " ---------------------------------------------------------------------------------------------------- \n")

    commands1 = input()
    if commands1 == 'help':
        om.menu()
    elif commands1 == '1':
        onto = om.load()
        om.query1(onto)
        dm.menuOWL()
    elif commands1 == '2':
        onto = om.load()
        om.query2(onto)
        dm.menuOWL()
    elif commands1 == '3':
        onto = om.load()
        om.query3(onto)
        dm.menuOWL()
    elif commands1 == '4':
        onto = om.load()
        om.query4(onto)
        dm.menuOWL()
    elif commands1 == '5':
        onto = om.load()
        om.query5(onto)
        dm.menuOWL()
    elif commands1 == '6':
        onto = om.load()
        om.query6(onto)
        dm.menuOWL()
    elif commands1 == '7':
        onto = om.load()
        om.query7(onto)
        dm.menuOWL()
    elif commands1 == '8':
        dm.menu()
    elif commands1 == '9':
        print("A presto!")
        return 0
    else:
        print("Non riesco a trovare questo comando! Consulta la lista dei comandi e riprova.")
        om.menu()


# Inizio
dm.menu()
