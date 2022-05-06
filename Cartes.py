class Carte:
    def __init__(self,nom,coutmana,description):
        self.nom = nom
        self.coutmana = coutmana
        self.description = description
    def getName(self):
        return self.nom

Carte_1 = Carte ('Exemple', 20, 'Cette carte est un exemple.')
Carte_2 = Carte ('Cristal', 10, 'Cette carte permet d augmenter votre mana maximum de sa valeur')



class Mage:
    def __init__(self,nom,pv,mana,valeurmana,main):
        self.nom = nom
        self.pv = pv
        self.mana = mana
        self.valeurmana = valeurmana
        self.main = main
    def getMana(self) :
        return self.mana
    def getValeurMana(self) :
        return self.valeurmana

Joueur = Mage ('Joueur', 100, 5, 50, Carte_1)




class CarteAutre:
    def __init__(self,nom,pv,atk,coutmana,description):
        self.nom = nom
        self.pv = pv
        self.atk = atk
        self.coutmana = coutmana
        self.description = description
    def getName(self):
        return self.nom
    def getPV(self):
        return self.pv
    def getATK(self):
        return self.atk
    def getCoutMana(self):
        return self.coutmana

CarteCreature_1 = CarteAutre ('Créature', 45, 25, 25, 'Une créature')
CarteCreature_2 = CarteAutre ('Créature', 45, 25, 25, 'Cette créature est l ennemi de base à combattre pour l exemple')
CarteBlast_1 = CarteAutre ('Blast', 20, 40, 30, 'Ce Blast peut être lancé contre un mage ou une créature, mais est défaussé dès qu il est joué')


class Main:
    def __init__(self,main) :
        def getMain(self):
            Carte_1

class ZoneDeJeu:
    def __init__(self, zonedejeu) :
        self.zonedejeu = zonedejeu

class Defausse:
    def __init__(self, defausse) :
        self.defausse = defausse

class Play:
    def __init__(self):
        self.tour = 0



print ('Vous incarnez un mage et devez combattre les autres joueurs afin d acceder à la victoire !')
print ('Une première créature s oppose à vous.')
print ('Vous devez jouer une carte ! Laquelle choisissez-vous ?')
print (Carte_2.getName())
print (CarteCreature_1.getName())
print (CarteBlast_1.getName())



Choix1 = int(input('Choix : '))


if Choix1 == 'Cristal':
    + 30 (Joueur.getValeurMana)
    print ('Vous avez dépensé 10 mana pour jouer la carte Cristal.')
    print ('La valeur de votre mana à augmenté de 30 !')
    Carte_2 in Defausse

if Choix1 == 'Créature':
    - 25 (Joueur.getMana)
    print ('Votre créature attaque mais elle est également touchée par l ennemi !')
    CarteCreature_2.getPV - CarteCreature_1.getATK
    CarteCreature_1.getPV - CarteCreature_2.getATK
    print ('Votre créature possède désormais', CarteCreature_1.getPV, 'PV !')
    print ('La créature adverse possède elle', CarteCreature_2.getPV, 'PV !') 
    if (CarteCreature_1.getPV) < 0:
        CarteCreature_1 in Defausse
        print ('Votre créature est morte ! Elle est déplacée dans la défausse...')
    else : CarteCreature_1 in ZoneDeJeu

if Choix1 == 'Blast' :
    - 30 (Joueur.getMana)
    print ('Vous dépensez', CarteBlast_1.getCoutMana, 'mana pour la carte Blast ! Votre Blast attaque sans recevoir de coups en retour.')
    CarteCreature_2.getPV - CarteBlast_1.getATK
    print ('Votre Blast à toujours', CarteBlast_1.getPV, 'PV !')
    print ('La créature à', CarteCreature_2.getPV, 'PV !')
    if (CarteBlast_1.getPV) < 0:
        CarteBlast_1 in Defausse
        print ('Votre Blast est mort, il est déplacé dans la défausse...')
    else : CarteBlast_1 in ZoneDeJeu
