from Repo.Repository import Repo

class ClientRepo(Repo):
    def __init__(self):
        super().__init__()

    def cautaNume(self, nume):
        for client in self.getLista():
            if client.nume()==nume:
                return client

    def cautaPrenume(self, prenume):
        for client in self.getLista():
            if client.prenume()==prenume:
                return client