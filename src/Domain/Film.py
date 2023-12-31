from Domain.Entitate import Entitate
from dataclasses import dataclass

# class Film(Entitate):
#     def __init__(self, id, titlu, descriere, gen, nrInchirieri):
#         super().__init__(id, nrInchirieri)
#         self.__titlu=titlu
#         self.__descriere=descriere
#         self.__gen=gen
#
#     def getTitlu(self):
#         return self.__titlu
#
#     def getDescriere(self):
#         return self.__descriere
#
#     def getGen(self):
#         return self.__gen
#
#     def setTitlu(self, titluNou):
#         self.__titlu=titluNou
#
#     def setDescriere(self, descriereNoua):
#         self.__descriere=descriereNoua
#
#     def setGen(self, genNou):
#         self.__gen=genNou
#
#     def __str__(self):
#         return "Film: " + str(self.getID()) + ' ' + self.getTitlu() + ' ' + self.getDescriere() + ' ' + self.getGen() + ' ' + str(self.getNrInchirieri())

@dataclass
class Film(Entitate):
    titlu: str
    descriere: str
    gen: str
    nrInchirieri: int