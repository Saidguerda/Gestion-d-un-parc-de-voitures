class voiture:
    def __init__(self, matricule,marque,couleur):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur
    def afficher_informations(self):
        print(f"la matricule de la voiture: {self.matricule},et ca marque: {self.marque},et couleur: {self.couleur}")
class Parc:
    def __init__(self,id,adresse,capacite):
        self.id = id
        self.adresse = adresse
        self.capacite = capacite
        self.liste_voitures = []
