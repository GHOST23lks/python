
class Livre:
    def __init__(self, id, titre, auteur, genre, disponible=True):
        self.id = id
        self.titre = titre
        self.auteur = auteur
        self.genre = genre
        self.disponible = disponible
