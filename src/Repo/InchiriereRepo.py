from Repo.Repository import Repo

class InchiriereRepo(Repo):
    def __init__(self, clientRepo, filmRepo):
        super().__init__()
        self.__clientRepo=clientRepo
        self.__filmRepo=filmRepo

    def inchiriere(self, inchiriere):
        super().adauga(inchiriere)
        filmID=int(inchiriere.filmID())
        film=self.__filmRepo.index(filmID)
        clientID=int(inchiriere.clientID())
        client=self.__clientRepo.index(clientID)
        nr=film.nrInchirieri()+1
        film.nrInchirieri=nr
        nr=client.nrInchirieri()+1
        client.nrInchirieri=nr

    def returnare(self, inchiriere):
        super().sterge(inchiriere.id())
        filmID=int(inchiriere.filmID())
        film=self.__filmRepo.index(filmID)
        clientID=int(inchiriere.clientID())
        client=self.__clientRepo.index(clientID)
        nr=film.nrInchirieri()-1
        film.nrInchirieri=nr
        nr=client.nrInchirieri()-1
        client.nrInchirieri=nr