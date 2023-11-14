from joueurs import*
from EtatJeu import*
import sys

def partie(joueur1,joueur2):
    """Joue une partie d'échecs. 

    Args:
        joueur1 (_type_): Le joueur 1. Peut être humain ou IA
        joueur2 (_type_): Le joueur 2. Peut être humain ou IA 
    """
    
    save=None
    while save not in ("O","N"):
        
        save=input("Voulez vous charger une sauvegarde ? (O/N) \n")
    
    if save=="O":
        loop=True
        while loop:
            try :
                nom_save=input("Nom du fichier de sauvegarde : \n")
                partie = EtatJeu(sauvegarde = nom_save)
                loop=False
            except:
                print("Fichier introuvable \n")
        print("Sauvegarde chargée \n")
    
    else:
        partie= EtatJeu()        
    
    print("Bonne partie ! A tout moment, entrez 'save' pour sauvegarder et quitter.")
        
    joueurs=[joueur2,joueur1]


    print(partie)
    draw=False
    draw_votes=[]
    while partie.gagnant() is None and not draw:
        deplacement=joueurs[int(partie.trait)].jouer_coup(partie)
        
        #Vote de la nulle
        if deplacement=="nulle":
            draw_votes+=1
            if draw_votes==2:
                draw=True
        else:
            draw_votes=0
        
        if deplacement=="save" :
            partie.sauvegarder("save")
            print("Sauvegarde effectuée.") 
            return "N"
        
        partie.deplacer_piece(deplacement[0],deplacement[1])
        
        partie.trait = not partie.trait
        print(partie)
    
    if partie.pat():
        draw=True
    else:
        print(f"{joueurs[partie.gagnant()].nom} a gagné la partie ! \n")
    
    
    
def main():
    """Le jeu d'échec dans son intégralité. Initialise une partie, 
    la joue et répète tant que l'utilisateur veut rejouer."""
    
    while True:
        
        replay=None
        joueurs = []
        for i in (1,0):
            type_joueur=None
            if i==1: couleur="blanc"
            else: couleur="noir"
            
            while type_joueur not in ("1","2"):
                type_joueur=input(f"De quel type est le Joueur {couleur} ? \n 1: Humain \n 2: IA \n")
            
                
            if type_joueur=="1":
                nom=input(f"Quel est le nom du Joueur {couleur} ? \n")
                joueurs.append(Humain(nom,i))
            
            
            else:
                niveau=input(f"Quel est le niveau de l'IA {couleur} souhaité? \n")
                nom=f"IA {couleur}"
                if niveau == "9":
                    joueurs.append(Stockfish(nom, i))
                else :   
                    joueurs.append(IA(nom, i, int(niveau)))

        replay=partie(joueurs[0],joueurs[1])
            
        while replay not in ("O","N"):
            replay=input("Voulez vous rejouer ? (O/N) \n")
            
        if replay=="N":
            print("Merci d'avoir joué ! ")
            sys.exit()
    
    
        
if __name__== "__main__":
    main()