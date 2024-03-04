import random
import string
from datetime import date, timedelta
from Domain.Client import Client
from Repository.ClientRepo import ClientRepo


class ClientsService:

    def __init__(self, clientsRepo):
        self.__clientsRepo = clientsRepo
        """self.__moviesRepo = moviesRepo
        self.__rentalRepo = rentalRepo"""

    def addClient(self, clientId, clientName, nrInchiriate=0):
        """
        Adaugare client in dictionarul de clienti.
        :param clientId: Id-ul clientului - int
        :param clientName: Numele clientului - string
        :return:
        """
        client = Client(clientId, clientName, nrInchiriate)
        self.__clientsRepo.add(client)

    def RemoveClient(self, clientId):
        """
        Sterge un client din dictionar.
        :param clientId:
        :return:
        """
        self.__clientsRepo.delete(clientId)

    def updateClientName(self, clientId, clientName):
        """
        Modifica numele unui client existent in dictionar.
        :param clientId:
        :param clientName:
        :return:
        """
        client = self.__clientsRepo.searchById(clientId)
        client.SetName(clientName)
        self.__clientsRepo.update(client)

    def getIsDeleted(self, clientId):
        """
        Verfifica daca un client a fost sters.
        :param clientId: id-ul clientului - int
        :return: True/False
        """
        client = self.__clientsRepo.searchById(clientId)
        return self.self.__clientsRepo.searchById(clientId).isDeleted

    def getAllClients(self):
        """
        returneaza o lista cu toti clientii din dictionar
        :return:
        """
        return self.__clientsRepo.getAll()

    def generateClientsService(self, nrClients):
        """
        Genereaza un nr dat de la tastatura de clienti.
        :param nrClients: numarul de clienti pe care dorim sa ii generam - int
        :return:
        """
        n = 0
        for n in range(nrClients):
            clientId = random.randrange(0, 10000)
            length = 7
            letters = string.ascii_lowercase
            clientName = ''.join(random.choice(letters) for i in range(length))
            client = Client(clientId, clientName)
            while client in self.getAllClients():
                self.generateClientsService()
                return
            self.__clientsRepo.add(client)

    def searchById(self, clientId):
        """
        Cauta dupa id.
        :param clientId:
        :return:
        """
        return self.__clientsRepo.searchById(clientId)

    def ordonare_dupa_nume(self):
        """
        Ordoneaza cleintii care au inchiriat filme dupa nume.
        :return: client - lista
        """
        clients = [c for c in self.getAllClients() if c.getNrFilme() > 0]
        for i in range(0, len(clients) - 1):
            for j in range(i + 1, len(clients)):
                if clients[i].getClientName() > clients[j].getClientName():
                    clients[i], clients[j] = clients[j], clients[i]
        return clients

    def ordonare_dupa_nr(self):
        """
        Ordoneaza clientii dupa numarul de inchirieri.
        :return: clients - lista
        """
        clients = [c for c in self.getAllClients() if c.getNrFilme() > 0]
        for i in range(0, len(clients) - 1):
            for j in range(i + 1, len(clients)):
                if clients[i].getNrFilme() > clients[j].getNrFilme():
                    clients[i], clients[j] = clients[j], clients[i]
        return clients

    def primi_30_la_suta(self):
        """
        Returneaza primi 30% clienti dupa nr inchirieri
        :return: clients - lista
        """
        clients = self.ordonare_dupa_nr()
        return clients[int(0.7 * len(clients)):]


