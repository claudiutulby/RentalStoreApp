from Domain.Client import Client
from dataclasses import dataclass

@dataclass
class ClientDTO:
    nume: str
    nrInchirieri: int

class DTOassembler:
    @staticmethod
    def createDTO(client):
        nume=client.nume
        nrInchirieri=client.nrInchirieri
        return ClientDTO(nume, nrInchirieri)

class ClientController:
    def __init__(self, repo):
        self.__repo=repo

    def getLista(self):
        return self.__repo.getLista()

    def adauga(self, id, nume, prenume):
        if self.__repo.cautaID(id) is False:
            client=Client(id, nume, prenume, 0)
            self.__repo.adauga(client)
        else:
            raise KeyError('Există deja un client cu acest ID!')

    def sterge(self, id):
        if self.__repo.cautaID(id) is True:
            self.__repo.sterge(id)
        else:
            raise KeyError('Nu există vreun film cu acest ID!')

    def modifica(self, id, nume, prenume):
        client=Client(id, nume, prenume, 0)
        self.__repo.modifica(client)

    def cautaNume(self, nume):
        return self.__repo.cautaNume(nume)

    def cautaPreume(self, prenume):
        return self.__repo.cautaPrenume(prenume)

    # def sortNume(self):
    #     clienti=self.getLista()
    #     clienti.sort(key=lambda x:x.nume)
    #     return clienti
    #
    # def sortNrInchirieri(self):
    #     clienti=self.getLista()
    #     clienti.sort(reverse=True, key=lambda x:x.nrInchirieri)
    #     return clienti
    #
    # def procente30(self):
    #     clientiLista=self.sortNrInchirieri()
    #     clienti={}
    #     lungime=3*len(clientiLista)//10
    #     for i in range (lungime):
    #         clienti.update({clientiLista[i].nume: clientiLista[i].nrInchirieri})
    #     return clienti

    def DTO(self, clienti):
        clientiDTO=[]
        for client in clienti:
            clientiDTO.append(DTOassembler.createDTO(client))
        return clientiDTO

    def sortNume(self):
        clienti=self.getLista()
        clienti.sort(key=lambda x:x.nume)
        return self.DTO(clienti)

    def sortNrInchirieri(self):
        clienti=self.getLista()
        clienti.sort(reverse=True, key=lambda x: x.nrInchirieri)
        return self.DTO(clienti)

    def procente30(self):
        clienti=self.getLista()
        clienti.sort(reverse=True, key=lambda x: x.nrInchirieri)
        nr=3*len(clienti)//10
        primii30=[]
        for i in range(nr):
            primii30.append(clienti[i])
        return self.DTO(primii30)