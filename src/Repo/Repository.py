class Repo:
    def __init__(self):
        self.__repo=[]

    def getLista(self):
        return self.__repo

    def adauga(self, entitate):
        if self.cautaID(entitate.id) is False:
            self.getLista().append(entitate)
        else:
            raise KeyError('Exista deja')

    def sterge(self, id):
        if self.cautaID(id) is True:
            for entitate in self.getLista():
                if entitate.id==id:
                    self.getLista().remove(entitate)
        else:
            raise KeyError('Nu exista')

    def modifica(self, entitateNoua):
        for i in range (len(self.__repo)):
            if self.__repo[i].id==entitateNoua.id:
                nr=int(float(self.__repo[i].nrInchirieri()))
                entitateNoua.nrInchirieri=nr
                self.__repo[i]=entitateNoua

    def cautaID(self, id):
        for entitate in self.getLista():
            if entitate.id==id:
                return True
        return False

    def index(self, id):
        for entitate in self.getLista():
            if entitate.id==id:
                return entitate