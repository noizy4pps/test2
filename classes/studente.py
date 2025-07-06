from classes.persona import Persona


class Studente(Persona):
    profilo = "Studente"

    def __init__(self, nome, cognome, età, residenza, corso_di_studio):
        super().__init__(nome, cognome, età, residenza)
        self.corso_di_studio = corso_di_studio

