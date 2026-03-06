class Voiture:
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
    def entrer_voiture(self,voiture):
        if voiture in self.liste_voitures:
            print("voiture existe dans le parc")
        elif len(self.liste_voitures) >= self.capacite:
            print("le parc est plein on peux pas ajouter des voitures")
        else:
            self.liste_voitures.append(voiture)
            print(f"places libres {self.calculerNbrPlacesLibres()}")
    def sortir_voiture(self,voiture):
        if voiture in self.liste_voitures:
            self.liste_voitures.remove(voiture)
            print("la voiture est sortira dans le parc")
            print(f"places libres {self.calculerNbrPlacesLibres()}")
        else:
            print("voiture non existe")
    def calculerNbrPlacesLibres(self):
        return self.capacite - len(self.liste_voitures)
parc = Parc(2,"29 Clarion Road",3)
v1 = Voiture("A123","Toyota","Rouge")
v2 = Voiture("B199","Honda","Blue")
v3 = Voiture("C144","Bmw","vert")


