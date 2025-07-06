
from classes.studente import Studente
from func import conta, parla

studente_uno = Studente("Py", "Mike", 24, "Casa Dello Studente", "ragioneria")

def esegui():
    parla("napoli")
    conta(5, 65, "+")
    print(studente_uno.scheda_personale())
    studente_uno.modifica_scheda()
    print(studente_uno.scheda_personale())

def esegui2():
    parla("milano")
    conta(5, 35, "-")


if __name__ == "__main__":
    esegui()