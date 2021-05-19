class Persoana:
    def __init__(self, nume_familie, prenume, varsta):
        self.nume_famile = nume_familie
        self.prenume = prenume
        self.varsta = varsta
    def numeFamilie(self):
        print(f'Numele meu este {self.nume_famile}.')
    def prenumele(self):
        print(f'Prenumele meu este {self.prenume}.')
    def numeComplet(self):
        print(f'Numele meu este {self.nume_famile} {self.prenume}.')
    def ani(self):
        print(f'Varsta mea este de {self.varsta} de ani.')
    def numeVarsta(self):
        print(f'Numele meu este {self.nume_famile} si am {self.varsta} de ani.')
    def prenumeVarsta(self):
        print(f'Prenumele meu este {self.prenume} si am {self.varsta} de ani.')
    def numePrenumeVarsta(self):
        print(f'Numele meu este {self.nume_famile} {self.prenume} si am {self.varsta} de ani.')
    def cinesunt(self):
        print(f'Numele meu este {self.nume_famile} {self.prenume} si am {self.varsta} de ani sau pe scurt, Subiectul6.')
Subiectul1 = Persoana('Belmond', 'Tiberiu', 33)
Subiectul1.ani()
print('#' * 50)
Subiectul2 = Persoana('Bella', 'Kon', 21)
Subiectul2.numeVarsta()
print('#' * 50)
Subiectul3 = Persoana('Kevin', 'Llons', 72)
Subiectul3.numeComplet()
print('#' * 50)
Subiectul4 = Persoana('Kassir', 'Ted', 63)
Subiectul4.prenumeVarsta()
print('#' * 50)
Subiectul5 = Persoana('Klipps', 'Ivy', 22)
Subiectul5.numeFamilie()
print('#' * 50)
Subiectul6 = Persoana('Kalips', 'Leo', 20)
Subiectul6.cinesunt()