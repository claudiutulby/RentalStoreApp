from dataclasses import dataclass

# class Entitate:
#     def __init__(self, id, nrInchirieri):
#         self.__id=id
#         self.__nrInchirieri=nrInchirieri
#
#     def getID(self):
#         return self.__id
#
#     def getNrInchirieri(self):
#         return self.__nrInchirieri
#
#     def setID(self, idNou):
#         self.__id=idNou
#
#     def setNrInchirieri(self, nrNou):
#         self.__nrInchirieri=nrNou
#
#     def __str__(self):
#         return 'ID: ' + str(self.getID()) + ' ' + str(self.getNrInchirieri())

@dataclass
class Entitate:
    __id: int

    @property
    def id(self):
        return self.__id