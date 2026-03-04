class voiture:
    def __init__(self, matricule,marque,couleur):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur
    def afficher_informations(self):
        print(f"la matricule de la voiture: {self.matricule},et ca marque: {self.marque},et couleur: {self.couleur}"
              )
