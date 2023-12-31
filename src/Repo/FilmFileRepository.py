from Repo.FilmRepository import FilmRepo
from Domain.Film import Film

class FilmFileRepo(FilmRepo):
    def __init__(self, fisier):
        super().__init__()
        self.__fisier=fisier
        self.citesteFisier()

    def adauga(self, film):
        super().adauga(film)
        self.scrieFisier()

    def sterge(self, id):
        super().sterge(id)
        self.scrieFisier()

    def modifica(self, film):
        super().modifica(film)
        self.scrieFisier()

    def citesteFisier(self):
        f=open(self.__fisier, "r")
        line=f.readline().strip('\n')
        while line != '':
            list=line.split(' ')
            id=int(list[0])
            titlu=list[1]
            descriere=list[2]
            gen=list[3]
            nrInchirieri=int(list[4])
            film=Film(id, titlu, descriere, gen, nrInchirieri)
            line=f.readline().strip('\n')
            super().adauga(film)

    def scrieFisier(self):
        f=open(self.__fisier, "w")
        filme=super().getLista()
        for film in filme:
            id=film.id()
            titlu=film.titlu()
            descriere=film.descriere()
            gen=film.gen()
            nrInchirieri=film.getNrInchirieri()
            line=str(id) + ' ' + titlu + ' ' + descriere + ' ' + gen + ' ' +str(nrInchirieri) + '\n'
            f.write(line)
        f.close()