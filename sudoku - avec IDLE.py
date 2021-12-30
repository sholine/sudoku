# Résolution de sudokus de niveaux 1 à 4

# Programmer avec Python Turtle Graphics

import numpy as np
import os  # module OS pour lire les noms des fichiers

# ..................................................
# 1 1 : Résolution de sudokus de niveau 1

grille=np.zeros((9,9)) # définition grille de 81 valeurs
# ..................................................

def RAZposs(): # RAZ des possibles
    for l in range(9):   
        for c in range(9):
            grilleVU[l,c]=0
            grillePU[l,c]=0  
    for i in range(81) :
        tabpos[i]=[1,2,3,4,5,6,7,8,9]
# ..................................................

def affiche_grille(grille) :
    
    print ("┌———————┬———————┬———————┐")
    ct=0
    for l in range(9) :
        print ("│ ",end="")
        for c in range(9):
            if grille[l,c]>0 :
                ct=ct+1
                v=int(grille[l,c])
                print (v,end=" ")
               
            else :
                print(" ",end=" ")  # n'affiche pas les 0
            if c==2 or c==5:
                print("│",end=" ")
        print ("│")
        if l==2 or l==5 :
            print ("├———————┼———————┼———————┤")
    print ("└———————┴———————┴———————┘")
    
# ..................................................
grillesauv=np.zeros((9,9))  # pour restituer la grille quand nécessaire

# ..................................................
def jouer(ch) :
    
    initjeu()
    MAJdd() # pour jouer niveau 3
    
    n = int(ch)
    lig = n // 100 
    col = (n- lig * 100) // 10
    val = (n- lig * 100) % 10
    l=lig-1
    c=col-1
    if grilleVU[l,c] == val or grillePU[l,c] == val: # niveaux 1 et 2 + niv 3 après MAJdd()
        grille[l,c] = val
        
    s=0 # si s==0 jouer un double pour niveau 4
    for lig in range(9):   
        for col in range(9):
            s=s+grilleVU[lig,col]+grillePU[lig,col]
            
    if s==0:
        # jeu-double
        w = grilleD[l,c]  # w valeur double
        v1 = w//10
        v2 = w%10
        if val == v1 or val == v2 :
            grille[l,c] = val  
        
    initjeu()
# ..................................................
def initjeu():
    # initialisations des possibles
    for l in range(9):   
        for c in range(9):
            grilleVU[l,c]=0
            grillePU[l,c]=0
            grilleD[l,c]=0
            grilleDD[l,c]=0
            
            grillepossibles[l,c]=0
                    
    for i in range(81) :
        tabpos[i]=[1,2,3,4,5,6,7,8,9]    
    MAJtabpos()       
    MAJgrilleVU()
    MAJgrillePU()

# ..................................................
# initialisation de la table des possibles (81 cellules, 9 valeurs possibles)
tabpos = np.zeros((81,9)) # définition
for i in range(81) :
    tabpos[i]=[1,2,3,4,5,6,7,8,9]
# ..................................................
def MAJtabpos() :
    for l in range(9) :
        for c in range(9) :
            lpos= l*9 + c
            val= int(grille[l,c])
            
            if val > 0 :   # si val >0 alors MAJ de tabpos
                # plus aucune valeur n'est possible pour la cellule (l,c)
                for i in range(9):
                    tabpos[lpos,i]=0
                # MAJ ligne l de la grille (valeur non possible pour toute la ligne)
                for k in range(9): # colonne k ligne l de la grille
                    tabpos[l*9 + k, val-1]=0
                # MAJ colonne c de la grille (valeur non possible pour toute la colonne)
                for h in range(9): # ligne h colonne c de la grille
                    tabpos[h*9 + c, val-1]=0
                # MAJ carré (l,c) de la grille, (l1,c1) 1ère cellule du carré
                l1 = l - l%3
                c1 = c - c%3
                for i in range(3) :
                    for j in range(3) :
                        tabpos[(l1 + i)* 9 + (c1  + j), val - 1]=0
# ..................................................
# initialisation de la grille de valeurs uniques possibles par cellule
grilleVU=np.zeros((9,9))
# ..................................................
def MAJgrilleVU() :
    for i in range(81):
        nv = 0 # initialisation du nombre de valeurs possibles ligne i 
        lp=tabpos[i]  # ligne lp = vecteur des 9 valeurs possibles pour une cellule (l,c)
        
        for j in range(9):
            if lp[j] > 0 :
                nv = nv + 1
                v=lp[j]
        if nv == 1 :    # si nv identique à 1
            l= i//9
            c= i%9
            grilleVU[l,c] = v
# ..................................................
grillesol=np.zeros((9,9))
# ..................................................
def solution1(sol):  # solution niveau 1
    initjeu()
    s=0 # si s>0 il y a des possibles uniques par cellules
    ct=0 # init ct (assignement)
    for l in range(9):   
        for c in range(9):
            s=s+grilleVU[l,c]
            
    while s>0 :  # tant qu'il y a des possibles uniques par cellules    
        # placer tous ces possibles (niveau 1)
        for l in range(9):   
            for c in range(9):            
                vu=grilleVU[l,c]           
                if vu>0 :
                    grille[l,c]=vu
                    initjeu()
        s=0  # maj de s et ct
        ct=0  # MAJ de ct
        for l in range(9):   
            for c in range(9):
                s=s+grilleVU[l,c]
                if grille[l,c]>0 :
                    ct=ct+1
    ct=0  # MAJ de ct sinon parfois erreur d'affichage
    for l in range(9):   
        for c in range(9):
            grillesol[l,c]=grille[l,c]  # mémorisation de la solution
            if grille[l,c]>0 :
                ct=ct+1   
    if sol>-1:
        if ct == 81 :        
            affiche_grille(grille)
            print()
        else :
            print("pas de soution de niveau 1 : ",ct,"réponses / 81")              
   
    # retour au jeu
    for l in range(9):   
        for c in range(9):
            grille[l,c]=grillesauv[l,c]
    initjeu()

def ajouter_valeurs() :
    for l in range(9):   
        for c in range(9):
            grillesauv[l,c]=grille[l,c]
    solution1(-1)
    
    lc=0
    while int(lc) < 11 or int(lc) > 99 :
        print("ajouter une valeur de la solution :")
        lc=input("saisir un nombre de 2 chiffres (lc) -->  ")
    
    n = int(lc)
    lig = n // 10 ; col= n - lig * 10
    l=lig-1 ; c=col-1
    v=grillesol[l,c] ; grille[l,c]=v

    initjeu()
    print()
# ..................................................
grilleinit=np.zeros((9,9)) # mémorisation de la grille en cours
grilleinitiale=np.zeros((9,9)) # mémorisation de la grille initale avant jouer

def lister_valàenlever():
    for l in range(9):   
        for c in range(9):
            grilleinit[l,c]=grille[l,c]
    
    for l in range(9):   
        for c in range(9):
            
            for lig in range(9):   
                for col in range(9):
                    grille[lig,col]=grilleinit[lig,col]
            v=grille[l,c]
            if v>0:                
                grille[l,c]=0
                initjeu()
                for lig in range(9):   
                    for col in range(9):
                        grillesauv[lig,col]=grille[lig,col]
                solution1(-1)
                ct=0
                for lig in range(9):   
                    for col in range(9):
                        if grillesol[l,c]>0 :
                            ct= ct+1
                if ct==81:
                    print("ligne",l+1,"colonne",c+1,"on peut enlever ",int(v),"  (solution de niveau 1)")
                
            for lig in range(9):   
                for col in range(9):
                    grille[l,c]=grilleinit[l,c]
                    grillesol[l,c]=0
                    grillesauv[l,c]=0
            initjeu()
    rep=input('évoulez-vous enlever une valeur ?  o/n   ')
    if rep=="o" :
        lcv=input("saisir un nombre de 3 chiffres (lcv) -->  ")
        n = int(lcv)
        lig = n // 100 
        col = (n- lig * 100) // 10
        v = (n- lig * 100) % 10
        l=lig-1
        c=col-1
        if grille[l,c]==v:
            grille[l,c]=0
            initjeu()
# ..................................................

# 1 2 : Propriétés des sudokus (1ère partie) et création de nouvelles grilles

# ..................................................
# pour permuter 9 indices
indicesinitiaux=[0,1,2,3,4,5,6,7,8] 
indicespermutés=[-1,-1,-1,-1,-1,-1,-1,-1,-1]

# pour permuter 3 indices
indicesinit3val=[0,1,2]
indicesperm3val=[-1,-1,-1]

import random # pour choix aléatoire d'une valeur
# ..................................................
def mixer_valeurs():
    # 1 : permutation aléatoire des 9 valeurs
    permuter_indices()   # pour permuter 9 indices
    for l in range(9):   # mémorisation initiale de la grille de départ
        for c in range(9):
            grillesauv[l,c]=grille[l,c]

    for l in range(9):   
        for c in range(9):
            v=int(grillesauv[l,c])
            if v>0:
                # indicespermutés de 0 à 8, valeurs de 1 à 9
                v2=int(indicespermutés[v-1]+1)
                grille[l,c]=v2
    # grilleinit
    for l in range(9):   
        for c in range(9):
            grilleinit[l,c]=grille[l,c]
    
    # 2 : choix aléatoire d'une des 7 fonctons géométriques (fait 3 fois pour plus de hasard)

    for g in range(3):
        f=random.randint(0,7)
          
        # si f == 0 pas d'action
        if f == 1: 
            sd_dg()
        elif f == 2:
            sd_gd()
        elif f== 3:
            rg()
        elif f==4:
            rd()
        elif f==5 :
            sv()
        elif f==6 :
            sh()
        elif f==7 :
            f7()

    # 3 : permutations aléatoires
    perm3kcl()  # permutation des carrés alignés par colonnes
    perml_3k()  # permutation des 3 lignes de 3 carrés alignés
    permc_3k()  # permutation des 3 colonnes de 3 carrés superposés
    
    initjeu()  # initialisation du jeu
# ..................................................
def permuter_indices(): # permutation de 9 indices
    for ip in range(0,9):
        j=random.randint(0,8-ip) # recherche aléatoire dans un vecteur qui rétrécit
        indicespermutés[ip]=indicesinitiaux[j]
        for j in range(j,8-ip):
            indicesinitiaux[j]=indicesinitiaux[j+1] # rétrécissement du vecteur courant
    for i in range(8):
        indicesinitiaux[i]=i  # ré-init indices
# ..................................................
def permuter_indices3val():    # permutation de 3 indices
    for ip in range(3):   # de 0 à 2
        j=random.randint(0,2-ip) # recherche aléatoire dans un vecteur qui rétrécit
        indicesperm3val[ip]=indicesinit3val[j]
        for j in range(j,2-ip):
            indicesinit3val[j]=indicesinit3val[j+1] # rétrécissement du vecteur courant
    for i in range(3):
        indicesinit3val[i]=i  # ré-init indices
# ..................................................
# 7 fonctions géométriques :
def sd_dg():  # symétrie diagonale droite-gauche  fonction f6 = f1();f4()
    for l in range(9):   # mémorisation initiale de la grille de départ
        for c in range(9):
            grillesauv[l,c]=grille[l,c]
    for l in range(9):
        for c in range(9):
            grille[c,l]=grillesauv[l,c]
def sd_gd():   # symétrie diagonale gauche-droite  fonction f5 = f1();f3()
    for l in range(9):   # mémorisation initiale de la grille de départ
        for c in range(9):
            grillesauv[l,c]=grille[l,c]
    for l in range(9):
        for c in range(9):
            grille[c,l]=grillesauv[8-l,8-c]
def rg():    # rotation à gauche  fonction f2
    for l in range(9):   # mémorisation initiale de la grille de départ
        for c in range(9):
            grillesauv[l,c]=grille[l,c]
    for l in range(9):
        for c in range(9):
            grille[c,l]=grillesauv[l,8-c]
def rd():    # rotation à droite  fonction f1
    for l in range(9):   # mémorisation initiale de la grille de départ
        for c in range(9):
            grillesauv[l,c]=grille[l,c]
    for l in range(9):
        for c in range(9):
            grille[c,l]=grillesauv[8-l,c]
def sv() :    # symétrie verticale  fonction f4
    for l in range(9):   # mémorisation initiale de la grille de départ
        for c in range(9):
            grillesauv[l,c]=grille[l,c]
    for l in range(9):
        for c in range(9):
            grille[l,c]=grillesauv[l,8-c]
def sh():   # symétrie horizontale  fonction f3
    for l in range(9):   # mémorisation initiale de la grille de départ
        for c in range(9):
            grillesauv[l,c]=grille[l,c]
    for l in range(9):
        for c in range(9):
            grille[l,c]=grillesauv[8-l,c]
def f7():   # symétrie centrale (ou rotation 180°) f7 = f1();f1()
    rd();rd()
# ..................................................
def perml_3k():   # permutation des 3 lignes de 3 carrés alignés
    for l in range(9):   # mémorisation de la nouvelle grille en départ
        for c in range(9):
            grillesauv[l,c]=grille[l,c]
    # 3 séries de permutations (3 alignements de carrés)
    for j in range(3):
        permuter_indices3val()
        
        # transfert des valeurs de grillesauv vers grille
        for l in range(3):   
            for c in range(9):
                l2=indicesperm3val[l]
                grille[l2+3*j,c]=grillesauv[l+3*j,c]
# ..................................................
def permc_3k(): # permutation des 3 colonnes de 3 carrés superposés
    for l in range(9):   # mémorisation de la nouvelle grille en départ
        for c in range(9):
            grillesauv[l,c]=grille[l,c]
    # 3 séries de permutations (3 superpositions de carrés)
    for j in range(3):
        permuter_indices3val()
        
        # transfert des valeurs de grillesauv vers grille
        for c in range(3):   
            for l in range(9):
                c2=indicesperm3val[c]
                grille[l,c2+3*j]=grillesauv[l,c+3*j]
# ..................................................
def perm3kcl(): # permutation de  carrés 1 alignés et 2 superposés
    
    # 1 permutation des carrés alignés par colonnes
    permuter_indices3val()    
    for l in range(9):   # mémorisation initiale de la grille de départ
        for c in range(9):
            grillesauv[l,c]=grille[l,c]
    # transfert des valeurs de grillesauv vers grille
    for l in range(9):   
        for c in range(9):
            k=c//3
            c2=3*indicesperm3val[k]+c%3            
            grille[l,c2]=grillesauv[l,c]
    
    # 2 permutation des carrés alignés par lignes
    permuter_indices3val()
    for l in range(9):   # mémorisation de la nouvelle grille en départ
        for c in range(9):
            grillesauv[l,c]=grille[l,c]
    # transfert des valeurs de grillesauv vers grille
    for c in range(9):   
        for l in range(9):
            k=l//3
            l2=3*indicesperm3val[k]+l%3            
            grille[l2,c]=grillesauv[l,c]

# partie 4 : sudoku pendu niveaux 1 et 2
# ..................................................
# niveau 2

grillePU=np.zeros((9,9))  # initialisation de la grille des possibles uniques par zones
# ..................................................
def MAJgrillePU() :  # et grillepossibles
    # 1 MAJ des possibles uniques par lignes
    for l in range(9) :  # l ligne de la grille
        for kval in range(9) : # pour chacune des 9 valeurs possibles
            nbv=0 # init calcul du nb de val pour toutes les colonnes (ligne l)
            for c in range(9) :
                if tabpos[l*9+c,kval]>0 :
                    nbv=nbv+1
                    col = c # mémorisation de l'indice c
            if nbv == 1 :
                val= kval+1 # valeur de 1 à 9
                lig=l
                grillePU[lig,col]=val
   
    # 2 MAJ des possibles uniques par colonnes
    for c in range(9) :  # l ligne de la grille
        for kval in range(9) : # pour chacune des 9 valeurs possibles
            nbv=0 # init calcul du nb de val pour toutes les lignes (colonne c)
            for l in range(9) :
                if tabpos[l*9+c,kval]>0 :
                    nbv=nbv+1
                    lig=l # mémorisation de l'indice l
            if nbv == 1 :
                val= kval+1 # valeur de 1 à 9
                col=c
                grillePU[lig,col]=val

    # 3 MAJ des possibles uniques par carrés
    # définition des 9 carrés
    carré=[[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
    for i in range(9) :  # i indices des carrés
        indices= carré[i]
        l1= indices[0]
        c1= indices[1]
        for kval in range(9) : # indice des 9 valeurs possibles
            nbv=0 # init calcul du nb de val pour toutes les carrés d'indice i
            for h in range(3) :  # h indice de ligne, k indice de colonne
                for k in range(3) :
                    if tabpos[(l1+h)*9+(c1+k),kval]>0 :
                        nbv=nbv+1
                        lig=l1+h # mémorisation de l'indice ligne
                        col=c1+k # mémorisation de l'indice colonne
            if nbv == 1 :
                val= kval+1 # valeur de 1 à 9
                grillePU[lig,col]=val
# ..................................................
def solution2(sol):  # solution niveau 2
    
    initjeu()
    s=0 # si s>0 il y a des possibles uniques par cellules
    ct=0 # init ct (assignement)
    for l in range(9):   
        for c in range(9):
            s=s+grilleVU[l,c]+grillePU[l,c]
            grillesol[l,c]=grille[l,c]
            
    while s>0 :  # tant qu'il y a des possibles uniques par cellules    
        # placer tous ces possibles (niveau 1)
        for l in range(9):   
            for c in range(9):            
                vu=grilleVU[l,c]
                if vu==0:
                    vu=grillePU[l,c]
                if vu>0 :
                    grille[l,c]=vu
                    initjeu()
        s=0  # maj de s et ct
        ct=0  # MAJ de ct
        for l in range(9):   
            for c in range(9):
                grillesol[l,c]=grille[l,c]  # mémorisation de la solution
                s=s+grilleVU[l,c]+grillePU[l,c]
                if grille[l,c]>0 :
                    ct=ct+1    
    ct=0  # MAJ de ct sinon parfois erreur d'affichage
    for l in range(9):   
        for c in range(9):
            if grillesol[l,c]>0 :
                ct=ct+1    
    if sol>-1:
        if ct==81 :
            affiche_grille(grillesol)
            print ("   ",ct,"/ 81  (niveau 2)")
        else :
            print("pas de soution de niveau 2 : ",ct,"réponses / 81")
            
    # retour au jeu
    for l in range(9):   
        for c in range(9):
            grille[l,c]=grillesauv[l,c]    

# ..................................................
# partie 6 : sudoku pendu niveau 3
# ..................................................
# niveau 3
# modif k23  affiche grille des possibles uniques et doubles
# ..................................................
# initialisation de la grille des doubles-doubles
grilleDD=np.zeros((9,9))
grilleD=np.zeros((9,9))

def MAJdoubles() :
    # réinitialisation de la grille des doubles
    for l in range(9) :
        for c in range(9) :
            grilleD[l,c]=0 
    # recherche des cellules où deux valeurs sont possibles (nb=2)
    for l in range(9) :
        for c in range(9) :  # pour chaque cellule (l,c)
            nb=0 # init
            v1 = 0 # init première valeur
            for i in range(9) : # i indice des valeurs possibles pour (l,c)
                if tabpos[(l*9+c),i]>0 :
                    nb=nb + 1
                    if v1 == 0 :
                        v1 = tabpos[(l*9+c),i]
                    else :
                        v2 = tabpos[(l*9+c),i]  # v2 peut recevoir plusieurs valeurs
                        
            if nb == 2 : # si deux possibles en (l,c)
                v=int(10 * v1 + v2)
                grilleD[l,c]=v
    for l in range(9) :
        for c in range(9) :
            if grilleVU[l,c] >0 or grillePU[l,c] > 0 :
                grilleD[l,c]=0 

def MAJdd() :  # recherche des doubles-doubles : remplit grilleDD
    # et fait la Mise à jour de la table des possibles si majtabpos2=1 (vrai)
    initjeu()
    MAJdoubles() # remplit la grille des doubles grilleD
    
    # 1 recherche de doubles-doubles par lignes de grilleD

    for l in range(9):
        for c in range(9):            
            if grilleD[l,c]>0 :
                w=grilleD[l,c]  # 1er double
                for k in range(c+1,9):
                    if grilleD[l,k] == w : # si double-double (sinon k suivant)
                        grilleDD[l,c]=w
                        grilleDD[l,k]=w
                        
                        # faire MAJ de tabpos ligne l
                        v1 = int(w//10 - 1)  # valeurs de 1 à 9 indices de 0 à 8
                        v2 =  int(w%10 - 1)
                        for col in range(9):
                            if col != c and col != k :
                                tabpos[l*9 + col,v1]=0
                                tabpos[l*9 + col,v2]=0                                               
    
    # 2 recherche de doubles-doubles par colonnes de grilleD

    for c in range(9):
        for l in range(9):
            if grilleD[l,c]>0 :
                w=grilleD[l,c]   # 1er double
                for h in range(l+1,9):
                    if grilleD[h,c] == w : # si double-double
                        grilleDD[l,c]=w
                        grilleDD[h,c]=w
                        # faire MAJ de tabpos colonne c
                        v1 = int(w//10 - 1)
                        v2 =  int(w%10 - 1)
                        for lig in range(9):
                            if lig != l and lig != h :
                                tabpos[lig*9 + c,v1]=0
                                tabpos[lig*9 + c,v2]=0
                                    
    # 3 recherche de doubles-doubles par carrés dans la grilleD
    
    carré=[[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]] # def (rappel)
    for i in range(9) :  # i indices des carrés
        indices= carré[i]
        l1= indices[0]
        c1= indices[1]
        valcarré=[]
        for h in range(3):            
            for k in range(3):            
                l=l1+h
                c=c1+k
                valcarré=valcarré+[grilleD[l,c]]
        
        # recherche de doubles-doubles dans les 9 vecteurs de valcarré)
        for j in range(9):
            valeur=valcarré[j] # valeur pour j (de 0 à 8) pour la cellule i du carré
            
            if valeur>0 :
                w=valeur  # 1er double
                lig1= l1 + j//3 
                col1= c1 + j%3

                for k in range(j+1,9):
                    if valcarré[k] == w : # si double-double                    
                        lig2= l1 + k//3 
                        col2= c1 + k%3
                        grilleDD[lig1,col1]=w
                        grilleDD[lig2,col2]=w
                        # faire MAJ de tabpos carré[i]
                        v1 = int(w//10 - 1)
                        v2 =  int(w%10 - 1)
                        for j2 in range(3):  # boucle double dans le carré[i]
                            for k2 in range(3):
                                l= l1 + j2%3 
                                c= c1 + k2%3
                                if grilleDD[l,c] != w :
                                    tabpos[l*9 + c,v1]=0
                                    tabpos[l*9 + c,v2]=0
    MAJgrilleVU();MAJgrillePU()  # MAJ à partir de la table des possibles modifiée

def solution3(sol):  # solution niveau 3
    
    initjeu();MAJdd()    
    s=0 # si s>0 il y a des possibles uniques par cellules
    ct=0 # init ct (assignement)
    for l in range(9):   
        for c in range(9):
            s=s+grilleVU[l,c]+grillePU[l,c]
            grillesol[l,c]=grille[l,c]
            
    while s>0 :  # tant qu'il y a des possibles uniques par cellules    
        # placer tous ces possibles (niveau 1)
        for l in range(9):   
            for c in range(9):            
                vu=grilleVU[l,c]
                if vu==0:
                    vu=grillePU[l,c]
                if vu>0 :
                    grille[l,c]=vu
                    grilleVU[l,c]=0
                    grillePU[l,c]=0
                    initjeu();MAJdd()        
                
        s=0  # maj de s et ct
        ct=0  # MAJ de ct
        for l in range(9):   
            for c in range(9):
                grillesol[l,c]=grille[l,c]  # mémorisation de la solution
                s=s+grilleVU[l,c]+grillePU[l,c]
                if grille[l,c]>0 :
                    ct=ct+1
    
    ct=0  # MAJ de ct sinon parfois erreur d'affichage
    for l in range(9):   
        for c in range(9):
            if grille[l,c]>0 :
                ct=ct+1
    if sol > -1 :
        if ct == 81:
            affiche_grille(grille)
            print ("   ",ct,"/ 81  (niveau 3)")
        else :        
            print("pas de soution de niveau 3 : ",ct,"réponses / 81")              
            print()
     
    # retour au jeu
    for l in range(9):   
        for c in range(9):
            grille[l,c]=grillesauv[l,c]
    initjeu()
# ..................................................
# partie 8 : sudoku solution niveau 4
# ..................................................
nbsolniv4=[0]  #  nb de solutions niveau 4
# ..................................................   
def jeuauto():
    # init remplir la grille niveau 3  (cf solution3)
    initjeu();MAJdd() # initialisations
    
    s=0 # si s>0 il y a des possibles uniques par cellules
    ct=0 # init ct (assignement)
    for l in range(9):   
        for c in range(9):
            s=s+grilleVU[l,c]+grillePU[l,c]
            
    while s>0 :  # tant qu'il y a des possibles uniques par cellules    
        # placer tous ces possibles (niveau 1)
        for l in range(9):   
            for c in range(9):            
                vu=grilleVU[l,c]
                if vu==0:
                    vu=grillePU[l,c]
                if vu>0 :
                    grille[l,c]=vu
                    initjeu();MAJdd()
        s=0  # maj de s et ct
        ct=0  # MAJ de ct
        for l in range(9):   
            for c in range(9):
                s=s+grilleVU[l,c]+grillePU[l,c]
                if grille[l,c]>0 :
                    ct=ct+1            
# ..................................................   
def solution4(sol):  # solution niveaux 1 à 4
    
    solution3(-1)
    
    ct=0  # MAJ de ct
    for l in range(9):   
        for c in range(9):
            if grillesol[l,c]>0 :
                ct=ct+1   
    if ct<81 :
        up();goto(35,190)
        #write("recherche de la solution",font=("Arial", 10, "normal"),align="center")
        nbsolniv4[0]=0  # init nb de sol
        suitesolution4(sol)
    #print(nbsolniv4[0])
    
def suitesolution4(sol):    
    finchoixval[0] = 0  # init
    jouer_double_auto(sol)    

    if sol!=-1: # n'affiche pas si =-1 affiche si =0
        if nbsolniv4[0]>1:
            print(" ",nbsolniv4[0]," solutions niveau 4")
            nivsol[0]=4
        else :
            print(" ",nbsolniv4[0]," solution niveau 4")      
    for l in range(9):   # retour au jeu
        for c in range(9):
            grille[l,c]=grillesauv[l,c] # restitution de la grille
    
    initjeu()
    
# .................................................. 
# pour jouerdoubleauto
indice=[0]

choixval1=np.zeros(28) # mémorise les 1ères valeurs
choixval2=np.zeros(28) # mémorise les 2èmes valeurs
choixval_index=np.zeros(28) # mémorises l'index de choix entre 2 valeurs
finchoixval=[0]

affichechoix=[0]
# ..................................................
def jouer_double_auto(sol) :
    while finchoixval[0] == 0 :
        #print("jouer double auto finchoi est faux")
        ct=0 # compteur de valeurs de la grille avant double auto
        for l in range(9) :
            for c in range(9) :
                if grille[l,c]>0:
                    ct=ct+1
        ct1=ct  # compteur de valeurs de la grille avant double auto
        double_auto(sol)
        ct=0 # compteur de valeurs de la grille
        for l in range(9) :
            for c in range(9) :
                if grille[l,c]>0:
                    ct=ct+1
        
        if ct1==ct:  # erreur de grille
            finchoixval[0]=1
            # print("     pas de solution ")               
# ..................................................    
def double_auto(sol):
    #print("double auto")
    jeuauto() # complète la grille (niveau 3)
    
    # choisir un double (par ordre croissant l,c dans la grille)
    lig=0
    while lig < 9 :
        col=0;l1=0;c1=0
        while col <9 :
            val =int(grilleD[lig,col])            
            if val >0 :
                l1=lig;c1=col
                col=8 ; lig=8
            col=col+1
        lig = lig + 1
        
    v1=int(val//10) ; v2=int(val%10)
    
    i=indice[0]
    choixval1[i]=v1 ; choixval2[i]=v2
        
    if choixval_index[i]==0:
        v=v1
    else :
        v=v2

        
    grille[l1,c1]=v
    initjeu()
    
    #solniv[0]=0 # initialise l'indicateur de solution oui=1 non=0
    
    jeuauto() # complète la grille (niveau 3)
    
    indice[0]=indice[0]+1  # indice de choix

    s=0  # maj de s et ct
    ct=0  # MAJ de ct
    for l in range(9):   
        for c in range(9):
            s=s+grilleVU[l,c]+grillePU[l,c]
            if grille[l,c]>0 :
                ct=ct+1
    
    if v1+v2==0 : # s'il n'ya plus de double

        # si on a obtenu une solution (ct = 81)
        #   mémoriser et afficher (ou pas) la solution
        if ct == 81:            
            for l in range(9):   # initialise la grille
                for c in range(9):
                    grillesol[l,c]=grille[l,c]  # mémorisation de la solution
            #solniv[2]=solniv[2]+1  # 1 solution en +
            nbsolniv4[0]=nbsolniv4[0]+1   # 1 solution niv 4 en +

            # pour visualiser le nombre de solutions pour les pb à multiples solutions
            #if sol == -1:    
            #    print(nbsolniv4[0],end=" ")
            
            if sol!=-1 : # on n'affiche pas si sol == -1            
                #print("       solution ",solniv[2])
                print()
                affiche_grille(grille)
       
        # poursuivre la recherche d'autres solutions
        
        # modifier l'index de choix de double
        if choixval_index[i-1]==0 :
            choixval_index[i-1]=1
        else :
            index1=choixval_index[0] # mémorisation initiale du 1er index
            j=1
            while choixval_index[i-j]==1:                
                choixval_index[i-j]=0
                choixval_index[i-j+1]=0                               
                j=j+1
            choixval_index[i-j]=1
            
            # test d'arrêt : si le 1er index prend passe de 1 à 0 tous les choix possibles ont été faits
            if choixval_index[0] ==0 and index1 ==1 :  
                finchoixval[0]=1  # alors arrêt des choix

        # initialisations pour une nouvelle série de choix
        indice[0]=0 # initialise l'index 
        for l in range(9):   # initialise la grille
            for c in range(9):
                grille[l,c]=grillesauv[l,c]
        initjeu()    # initialise les possibles
    # si v1+v2 > 0 : alors il reste des doubles, faire d'autres choix
    # on quitte cette procédure double_auto(sol)
    # de retour dans jouer_double_auto(sol),
    #     1 on test s'il n'y a pas d'erreur dans la grille (donc si le compteru n'a pas bougé)
    #     2 si d'autre choix sont possibles (si finchoix est faux) la boucle reprend
    #     3 si finchoix est vrai ( == 1 ) retour à solution4(sol)
    #       on affiche le nbde solution et réinitiale la grille et le jeu pour retourner au menu.

    # pour visualiser les choix effectués et les solutions
    if affichechoix[0]==1:
        if v1+v2 > 0 :  
            if i==0:
                print()
            print(v, " en (",l1+1,",",c1+1,")",end="  ")
            
            if ct==81 :
                print ("solution ",nbsolniv4[0]+1)
                affiche_grille(grille)
# ..................................................
    

# ..................................................
#  Partie 2 :

# programmer pour jouer avec la tortue (au clavier et avec la souris)

# ..................................................

def dessine_grille():
    tracer(0)
    color("blue")
    x0=-122;y0=173  # emplacement du point en haut, à gauche de la grille
    for i in range(10):
        if i%3==0:
            pensize(3)  # taille du trait
        else:
            pensize(1)
        up();goto (x0,y0-i*35)
        down();goto (x0+9*35,y0-i*35)  # ligne horizontale
        up();goto (x0+i*35,y0)
        down();goto (x0+i*35,-142)  # ligne verticale
    color("black")
    
def remplir_grille_sudo(grille):
    
    if color() == ('green', 'green'): # affiche grille des possibles
        couleur="green"
        up();goto(35,190)
        
        write("Grille des possibles",font=("Arial", 13, "normal"),align="center")
    
    else :
        couleur="black"
        # pour niveau 4
        MAJdd()
        s1=0;s=0
        for l in range(9):   
            for c in range(9):
                s1=s1+grille[l,c] # si s1 == 0 la grille est vide
                s=s+grilleVU[l,c]+grillePU[l,c]  # si s == 0 il n'y a plus de possible unique
        if s1>0 and nouv_sudo[0]==0  :  # pas pendant saisie d'une grille
            if s == 0 :  
                up();goto (-110,200);color("white") # pour effacer message au dessus de la grille
                pensize(30); down(); goto (180,200)
    
                up();goto (35,195);color("black")
                write("jouer (ou tester) une case avec deux valeurs possibles",font=("Arial", 9, "normal"),align="center")
            else :
                up();goto (-110,200);color("white") # pour effacer message au dessus de la grille
                pensize(30); down(); goto (180,200);up();color("red")
    
    
    for lig in range (0,9):
        for col in range (0,9):
            tracer(0) 
            x=35*(col-3)-3;y=35*(4-lig)
            up()
            goto(x+5,y+15)
            down()
            color("white") # couleur de la ligne pour effacer
            pensize(28)  
            goto (x+5,y+15)
            if grille[lig][col]!=0:
                up()
                
                color(couleur)
                goto(x,y)
                if couleur=="green" or couleur=="blue": # pour les possibles et la solution
                    goto(x+4,y+4)
                    write(int(grille[lig,col]), font=("Arial", 12),align="center")
                else :
                    if couleur=="black": # pour afficher la grille
                        if grilleinitiale[lig,col] == 0 and mémo[0]>0 :
                            color("blue")
                       
                        write(int(grille[lig,col]), font=("Arial", 14))
    
    affich_compteur() 
    
    c=num_colonne[0] ; l=num_ligne[0]
    x=35*(c-4);y=35*(5-l)
    up(); goto(x,y);color("red")
    
def messages():  # commandes clavier du menu
    
    up();goto (-200,200);color("red")
    write('Sudoku',font=("Arial", 16, "normal"),align="center")
    
    goto (-119,265);color("black")
    write("charger une grille  : ",font=("Arial", 9, "normal"))
    goto (-10,265);color("black")
    write(" Facile Moyen Difficile Expert Diabolique",font=("Arial", 9, "normal"))
    
    goto (35,250);color("blue")
    write("    F    M    D    E    D   -   afficher la grille   -   mixer les valeurs",font=("Arial", 9, "normal"),align="center")
    goto (35,225);color("red")
    write("   afficher les possibles     -     afficher la solution     -     quitter",font=("Arial", 9, "normal"),align="center")

    goto (-200,225);color("black")
    write("   afficher toutes les aides",font=("Arial", 9, "normal"),align="center")
    
    goto (-50,-200);color("blue")
    write("saisir une nouvelle grille   O",font=("Arial", 9, "normal"),align="right")
    goto (50,-200);color("blue")
    write("+  :  pour ajouter une valeur de la solution",font=("Arial", 9, "normal"),align="left")

    goto (-50,-220);color("blue")
    write("mémorise le jeu en cours   O",font=("Arial", 9, "normal"),align="right")
    goto (-50,-240);color("blue")
    if mémo[0]>0 :
        write("jouer avec le jeu mémorisé   O",font=("Arial", 9, "normal"),align="right")
    
    goto (90,-220);color("blue")
    write("(pour enlever une valeur :  0)",font=("Arial", 9, "normal"),align="left")

    
    color("red")
    up;goto(35*(num_colonne[0]-4)+2,35*(5-num_ligne[0])) # retour du pointeur en (5,5)

def action(x, y):    # commande à partir des coordonnées du pointeur/souris
    plt.close() # ferme la fenêtre matplotlib
    tracer(0)  # pour ne pas afficher le déplacement du pointeur
     
    if x//17 > -19 and x//17 < -14 and y //17==14 : # fin saisie nouvelle grille
        
        nouv_sudo[0]=0
        mémo[0]=0 # jeu non mémorisé
        resetscreen();left(90) # efface et pointe vers le haut
        dessine_grille()
        messages()
        remplir_grille_sudo(grille)
        color("red");tracer(1) # fait apparaître le pointeur
        initjeu()  # initialisation du jeu
        for l in range(9):   # recherche solution et mémo grille initiale
            for c in range(9):
                grillesauv[l,c]=grille[l,c]
        
        solution4(-1)  # solution non affichée
        
    if x>-120 and x<190 and y>-140 and y<170 : # limites de la grille
        goto(x-10,y) # place le pointeur dans la bonne case
        tracer(1)
        
        num_colonne[0]=int((x+10)//35 +4)   # mémorisation indice colonne
        num_ligne[0]=int(5-y//35)           # mémorisation indice ligne

    # commandes avec la souris dans menu au dessus de la grille
    
    if nouv_sudo[0] == 0 : # hors la saisie d'une nouvelle grille
        if y>245 and y<265 :
            if x>-122 and x<-20: # charger une grille
                k0=x//20 +7 # niveau 1 à 5
                j=int(random.randint(1,10)) # boucle pour optimiser le hasard
                for i in range(j):
                    k=int(random.randint(0,5)+ (k0-1)*6) # choix aléatoire 
                choixgrille[0]=k
                k22() # charger une grille       
            if x>0 and x<70:
                k24() # afficher grille
            if x>100 and x<190: 
                k26() # mixer
        
        if y>225 and y<245 :
            if x>-120 and x<-20:
                k23() # possibles
            if x>20 and x<120:                
                k25() # solution
            if x>160 and x<190:
                k21() # quitter
            if x>-260 and x<-130:
                k20() # toutes les grilles

        if x>-62 and x<-46:
            if y>-200 and y<-188:
                k27() # saisir
            if y>-220 and y<-208:                
                k28() # mémoriser jeu
            if y>-240 and y<-228:
                k29() # afficher jeu mémorisé
        
                
    color("red")
    
# définitions des commandes (à partir du clavier ou avec la souris)

def k0(): # efface valeur 
    if nouv_sudo[0]==1: # pendant la saisie d'une nouvelle grille
        tracer(0)
        c=num_colonne[0]
        l=num_ligne[0]
        x=35*(c-4);y=35*(5-l)
        tracer(0)
        # efface case
        up(); goto(x,y+15)
        down(); color("white") # couleur de la ligne pour effacer
        pensize(28);goto (x,y+15);up();goto(x,y)
        
        grille[l-1,c-1]=0        
        initjeu()
    else:  #   pendant le jeu
        tracer(0)
        col=num_colonne[0]-1 ; lig=num_ligne[0]-1
        grille[lig,col]=0
    
        remplir_grille_sudo(grille)
        color("red");goto(35,0); tracer(1) # place le pointeur case centrale 
        initjeu()
        
def k1():
    num_valeur[0]=1
    valide_lcv()
        
def k2():
    num_valeur[0]=2
    valide_lcv()
    
def k3():
    num_valeur[0]=3
    valide_lcv()
    
def k4():
    num_valeur[0]=4
    valide_lcv()
    
def k5():
    num_valeur[0]=5
    valide_lcv()
    
def k6():
    num_valeur[0]=6
    valide_lcv()
            
def k7():
    num_valeur[0]=7
    valide_lcv()
    
def k8():
    num_valeur[0]=8
    valide_lcv()
    
def k9():
    num_valeur[0]=9
    valide_lcv()


def k21():
    exit()

def k22():  # charger une grille
    mémo[0]=0 # jeu non mémorisé
    # efface fenêtre
    resetscreen();left(90) # efface et pointe vers le haut
    penduindice[0]=0 # RAZ pendu
    choixgrillesudo()
    affniv()   # pour afficher le niveau
    
    initjeu()  # initialisation du jeu
    for l in range(9):   # recherche solution
        for c in range(9):
            grillesauv[l,c]=grille[l,c] # mémoristion avant procédure solution
            grilleinitiale[l,c]=grille[l,c] # mémoristion avant de jouer
            
    solution4(-1)  # solution non affichée
        
    tracer(0) # tracé instantané    
    up();goto (-40,200);color("white") # pour effacer message au dessus de la grille
    pensize(30); down(); goto (100,200)
    dessine_grille() 
    messages()
    
    remplir_grille_sudo(grille)
    color("red");tracer(1) # fait apparaître le pointeur
    

def affniv() :
    i=choixgrille[0] # pour afficher le niveau
    
    ct=0  # maj du compteur
    for l in range(9):
        for c in range(9):
            if grille[l,c]>0:
                ct=ct+1
    if i == -1:
        niveau="" # niveau non défini pour une grille saisie
    elif i < 6 :
        niveau="facile"
    elif i <12 :
        niveau = "moyen"
    elif i <18 :
        niveau = "difficile"
    elif i <24 :
        niveau = "expert"
    elif i <30 :
        niveau = "diabolique"
        
    tracer(0) # tracé instantané    
    up();goto (200,-160);color("white") # pour effacer niveau
    down();goto (280,-160)
    up();goto(240,-175)
    color("red")
    write(niveau,font=("Arial", 14, "normal"),align="center")
        

grillepossibles=np.zeros((9,9)) # mémorisation de grilleVU + grillePU  pour afficher tous les possibles


def k23(): # grille des possibles
    resetscreen();left(90) # efface et pointe vers le haut
    dessine_grille()
    messages()
    tracer(0) # tracé instantané
    color("red")
    up();goto(35,190)
    write("Grille des possibles",font=("Arial", 13, "normal"),align="center")
    
    initjeu()
    MAJdd()  # pour niveau 3
    for l in range(9):
        for c in range(9):
            grillepossibles[l,c]=0   # init
            if grilleVU[l,c]>0:
                grillepossibles[l,c]=grilleVU[l,c]
            if grillePU[l,c]>0:
                grillepossibles[l,c]=grillePU[l,c]
            if grilleD[l,c]>0:
                grillepossibles[l,c]=grilleD[l,c]
    for lig in range (0,9):
        for col in range (0,9):
            x=35*(col-3)-3;y=35*(4-lig)
            goto(x+4,y+4)
            if grillepossibles[lig,col]>0:
                if grillepossibles[lig,col]<10:
                    color("red")
                    write(int(grillepossibles[lig,col]), font=("Arial", 14),align="center")
                else :
                    if grilleDD[lig,col]>0:
                        color("black")
                        write(int(grillepossibles[lig,col]), font=("Arial", 12),align="center")
                    else :
                        color("blue")
                        write(int(grillepossibles[lig,col]), font=("Arial", 8),align="center")

    penduindice[0]=penduindice[0]+1
    choixpendu() 
    
    up();goto(35,0);color("red")

def k24():    # affiche grille
    resetscreen();left(90) # efface et pointe vers le haut
    dessine_grille()
    messages()
    
    tracer(0) # tracé instantané   
    color("black")
    for lig in range (0,9):
        for col in range (0,9):
            x=35*(col-3)-3;y=35*(4-lig)
            goto(x+4,y+4)
            if grilleinitiale[lig,col]>0:
                color("black")
            else :
                color("blue")
            if grille[lig,col]>0:
                write(int(grille[lig,col]), font=("Arial", 14),align="center")
          
    affniv()
    choixpendu() 
    up();goto(35,0)
    color("red")
  
def k25():   # affiche solution
    resetscreen();left(90) # efface et pointe vers le haut
    dessine_grille()
    messages()
    
    tracer(0) # tracé instantané
    color="green"
    up();goto(35,190)
    write("Grille solution",font=("Arial", 13, "normal"),align="center")
    
    for lig in range (0,9):
        for col in range (0,9):
            x=35*(col-3)-3;y=35*(4-lig)
            goto(x+4,y+4)
            if grillesol[lig,col]>0:
                write(int(grillesol[lig,col]), font=("Arial", 12),align="center")
    goto(35,0)
   
def k26():  # mixer valeurs
    mémo[0]=0 # jeu non mémorisé
    # efface fenêtre
    resetscreen();left(90) # efface et pointe vers le haut
    tracer(0)
    up();goto (-40,200);color("white") # pour effacer message au dessus de la grille
    pensize(30); down(); goto (100,200)
    up();goto(0,190);color("red")    
    write("mixer valeurs",font=("Arial", 14, "normal"),align="center")
    up();goto(35,0)
    for l in range(9):   
        for c in range(9):
            grillesol[l,c]=0
    mixer_valeurs()
    initjeu()
    for l in range(9):   
        for c in range(9):
            grillesauv[l,c]=grille[l,c]
            grilleinitiale[l,c]=grille[l,c]
                
    solution4(-1)  # solution non affichée
    dessine_grille() # affiche grille
    
    remplir_grille_sudo(grille)
    messages()
    choixpendu() # affiche pendu
    color("red");goto(35,0); tracer(1) # place le pointeur case centrale

nouv_sudo=[0]  # def 
def k27(): # . nouveau jeu nouvelle grille    partie 5
    nouv_sudo[0]=1 # vrai
    choixgrille[0]=-1 # niveau non défini
    
    penduindice[0]=0
    
    # efface fenêtre
    resetscreen();left(90) # efface et pointe vers le haut
    color("red")
    up();goto(35,190)        
    write("Nouvelle Grille (0 pour effacer une valeur)",font=("Arial", 10, "normal"),align="center")
    up();goto(35,0) 
    tracer(0)
    for l in range(9):   
        for c in range(9):
            grille[l,c]=0
            grillesol[l,c]=0
            grilleinitiale[l,c]=0
            
    dessine_grille() # affiche grille vide
    
    up();goto(-270,240)
    write('fin de saisie ici  ',font=("Arial", 9, "normal"),align="center")    

    # saisie des valeurs dans valide lcv
    # arrêt dans procédure get mouse

grillemémo=np.zeros((9,9))  # définition de la grille mémorisée
mémo=[0]

def k28(): # mémorise le jeu en cours
    mémo[0]=1 # jeu mémorisé
    for l in range(9):
        for c in range(9):
            grillemémo[l,c]=grille[l,c]
    goto (90,-240);color("red")
    write("jeu mémorisé",font=("Arial", 12, "normal"),align="left")


def k29() : # affiche jeu mémorisé
    if mémo[0]==1 :    
        suite_k29()

def suite_k29():
        
    RAZposs()
    for l in range(9):
        for c in range(9):
            grille[l,c]=grillemémo[l,c]
    resetscreen();left(90) # efface et pointe vers le haut
    dessine_grille()
    messages()
    for lig in range (0,9):
        for col in range (0,9):
            grilleinitiale[lig,col]=0
    remplir_grille_sudo(grille)
    color("red");goto(35,0); tracer(1) # place le pointeur case centrale 
    initjeu() 
    
def k30():  #   + ajouter valeur de la solution
    tracer(0)
    
    # ... pénalité pendu
    penduindice[0]=penduindice[0]+1
    choixpendu()
    color("red");up();goto(35,0)
    # ...
    if grillesol[1,1]==0: # si solution non déjà cherchée
        # maj sol
        for l in range(9):   
            for c in range(9):
                grillesauv[l,c]=grille[l,c]
        solution4(-1)  # solution non affichée niveaux 1 à 4
    
    col=num_colonne[0]-1 ; lig=num_ligne[0]-1
    v= grillesol[lig,col]

    if v>0 :    
        grille[lig,col]=v
        affich_compteur()
        
        x=35*(col-3)-3;y=35*(4-lig) # position du pointeur pour écrire
        color("red")
        goto(x,y)          
        write(int(grille[lig,col]), font=("Arial", 18))
        goto(35,0); tracer(1) # place le pointeur case centrale        
    
    initjeu()

def valide_lcv():
    if nouv_sudo[0]==1 :# saisie nouvelle grille  = vrai
        c=num_colonne[0]
        l=num_ligne[0]
        x=35*(c-4);y=35*(5-l)
             
        v=num_valeur[0]
        grille[l-1,c-1]=v
        # affichage valeur
        tracer(0)
        # efface case
        up(); goto(x,y+15)
        down(); color("white") # couleur de la ligne pour effacer
        pensize(28);goto (x,y+15);up();goto(x,y)
        
        up();color("green");goto(x,y); write(v, font=("Arial", 16),align="center")
    else :
        suite_valide_lcv()

def suite_valide_lcv() :
    tracer(0);up()
    MAJdd() # pour jouer niveau 3
    
    
    c=num_colonne[0]
    l=num_ligne[0]
    x=35*(c-4);y=35*(5-l)
    
    v=num_valeur[0]

    ch=str(l*100+c*10+v)

    initjeu()
    MAJdd() # partie 6 (pour niveau de résolution 3) 
    jouer(ch)

    # ......
    # partie 3 : sudoku pendu
    if grille[l-1,c-1]!=v : # si non validé
        penduindice[0]=penduindice[0]+1
        choixpendu()
        color("red");up();goto(35,0)
    # ......
    
    if nouv_sudo[0]==1 : # pendant la saisie d'une nouvelle grille
        # partie 5 : saisie nouvellegrille
        penduindice[0]=0 # init pendu pas de pénalité
        grille[l-1,c-1]=v  # choix validé en cours de saisie
        x=35*(c-4)-3;y=35*(5-l) # position du caractère à écrire
        up(); goto(x+5,y+15);color("white")
        down();pensize(28);goto(x+5,y+15);up() # efface avant d'écrire
        up(); goto(x,y);color("black")    
        write(int(grille[l-1,c-1]),font=("Arial", 16)) # écrit la valeur validée
        
   
    elif grille[l-1,c-1]==v : #si validé par le programme
        # complète la grille : v en (l,c)
        
        up(); goto(x-3,y);color("green")
    
        write(int(grille[l-1,c-1]),font=("Arial", 16)) # écrit la valeur validée
    affich_compteur()
    
    up();goto (-110,200);color("white") # pour effacer message au dessus de la grille
    pensize(30); down(); goto (180,200);up();color("red")
    goto(x,y) # positionne le pointeur
    
def affich_compteur():  # et numéro du problème
    ct=0  # maj du compteur affiché
    for l in range(9):
        for c in range(9):
            if grille[l,c]>0:
                ct=ct+1
    
    up();goto (-40,-165);color("white") # pour effacer le compteur
    pensize(20)
    down(); goto (90,-165)
    
    up();goto (25,-170);color("black")    
    write(str(ct)+' / 81',font=("Arial", 10, 'normal', 'bold', 'italic', 'underline'))
    
    color("red") # couleur du pointeur
    goto(35*(num_colonne[0]-4)+6,35*(5-num_ligne[0])) # replacer le pointeur

    
    up();goto (-220,185);color("white") # pour effacer le numéro du pb
    pensize(30)
    down(); goto (-180,185)
    
    up()
# ..................................................
# ..................................................
# partie 3 : sudoku pendu
# ..................................................
penduindice=[0]
def choixpendu():
    i=penduindice[0]+1
    if i<15:
        for j in range(i):
            
            dessine_pendu(j)
            

def dessine_pendu(i): 
    if i== 1:
        pendu1()
    elif i==2:
        pendu2()
    elif i==3:
        pendu3()
    elif i==4:
        pendu4()
    elif i==5:
        pendu5()
    elif i==6:
        pendu6()
    elif i==7:
        pendu7()
    elif i==8:
        pendu8()
    elif i==9:
        pendu9()
    elif i==10:
        pendu10()
    elif i==11:
        pendu11()
    elif i==12:
        pendu12()
    elif i==13:
        pendu13()
def  pendu1() : # soleil
    if nouv_sudo[0]!=1 : # pendant la saisie d'une nouvelle grille
        up();goto(-290,200);color("yellow")  
        write(chr(9788),font=("Arial", 60, "normal"),align="center")

def  pendu2() :
    x=-210;y=-35  # banc
    pensize(4)  # taille de la ligne
    up();goto (x,y);color("black");down(); goto(x+55,y);up()
def  pendu3() :   
    up();goto(-180,68)  # tête gaie
    color("black")
    write(chr(9786),font=("Arial", 40, "normal"),align="center")
def  pendu4() :    
    goto(-180,10);color("black")  # tronc haut
    write(chr(8898),font=("Arial", 55, "normal",'bold'),align="center")
    goto(-180,-13)   # tronc bas    
    write(chr(8899),font=("Arial", 55, "normal",'bold'),align="center")
def  pendu5() : 
    x=-198;y=+62 # bras gauche
    pensize(5)  # taille de la ligne
    up();goto (x,y);color("black");down(); goto(x-10,y-22);up()
def  pendu6() :     
    x=-166;y=+62  # bras droit
    pensize(5)  # taille de la ligne
    up();goto (x,y);color("black");down(); goto(x+11,y-22);up() 
def  pendu7() : 
    x=-190;y=10 # pied gauche
    pensize(5)  # taille de la ligne
    up();goto (x,y);color("black");down(); goto(x-10,y-40);up()
def  pendu8() : 
    x=-174;y=10  # pied droit
    pensize(5)  # taille de la ligne
    up();goto (x,y);color("black");down(); goto(x+8,y-40);up() 
def  pendu9() : 
    x=-260;y=-60  # sol
    pensize(4)  # taille de la ligne
    up();goto (x,y);color("grey");down(); goto(x+130,y);up() 
def  pendu10() : 
    x=-250;y=-60  # potence verticale
    pensize(4)  # taille de la ligne
    up();goto (x,y);color("black");down(); goto(x,y+210);up() 
def  pendu11() : 
    x=-250;y=149  # potence horizontale
    pensize(4)  # taille de la ligne
    up();goto (x,y);color("black");down(); goto(x+80,y);up() 
def  pendu12() : 
    x=-250;y=130  # potence angle
    pensize(4)  # taille de la ligne
    up();goto (x,y);color("black");down(); goto(x+19,y+19);up() 

def  pendu13() : # fin
    x=-180;y=149  # corde - banc
    pensize(2)  # taille de la ligne
    up();goto (x,y);color("grey");down(); goto(x,y-42);up()
    x=-210;y=-35  # banc
    pensize(4)  # taille de la ligne    
    up();goto (x,y);color("white");down(); goto(x+55,y);up()

    up();goto(-180,68)  # tête gaie
    color("white")   # pour effacer la tête gaie
    write(chr(9786),font=("Arial", 40, "normal"),align="center")
    color("black")
    up();goto(-180,50)  # tête triste
    write(chr(9785),font=("Arial", 55, "normal"),align="center")
    
    up()
    goto(-260,-180) # tête échec
    color("black")
    write(chr(9760),font=("Arial", 70, "normal"),align="center")

    up();goto(-160,-160);color("black") # cercueil
    write(chr(9904),font=("Arial", 40, "normal"),align="center")

# charger() est remplacé par choixgrillesudo()
# ..................................................
# choisir une grille sudoku de facile à diabolique
choixgrille=[-1]
grillesudo=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''] # 30 grilles
def choixgrillesudo():
    # grilles faciles de 0 à 5 (puis mixées)
    grillesudo[0]=['007000004083000060000704500010087000004250600095000000109003040600400000300106207']  # pb 1282
    grillesudo[1]=['856000073301070008009060500000400820000530409010020000003012000000604000025000100']  # pb 1291
    grillesudo[2]=['004060738008000010300005400090570020503000000001009050040196005000002000170403090']  # pb 1301
    grillesudo[3]=['504008300000009001700350008053460870040000000002100040020000537080000900905020180']  # pb 1311
    grillesudo[4]=['072800059580200000000007000000052948040009015060140230000406020006000100830021000']  # pb 1321
    grillesudo[5]=['009107005470050312006800090650000289000400506900000000002600708807010900390720000']  # pb 1341
    # grilles moyennes de 6 à 11 (puis mixées)
    grillesudo[6]=['002900807403020000000008004005000000090000000030001500010002409600080070700004005']  # pb 1242
    grillesudo[7]=['000000270400279036030080100000040000000006000900100002028300604009050007001000000']  # pb 1251
    grillesudo[8]=['010064000080000036000502010002083000706000509000750200070405000150000090000370060']  # pb 1281
    grillesudo[9]=['790000000003076020028100090036200001052609800004001006000800700000090010010005400']  # pb 2291
    grillesudo[10]=['000008100003200005908070060705403200040120000000706054050047000090000730037610008']  # pb 2321
    grillesudo[11]=['048700000602080009037400580379000004026549700400073060080050000004637001001020000']  # pb 2351
    # grilles difficiles de 12 à 17 (puis mixées)
    grillesudo[12]=['600200008007000050800040700040000030005400060010025009070090000000000005000080041']  # pb 2231
    grillesudo[13]=['090000000003076020028000090030200000052609800004001006000800700000000010010005400']  # pb 2241
    grillesudo[14]=['790000000003006020028100090030200001052609000004001006000800700000090000010005400']  # pb 2251
    grillesudo[15]=['501000080200940000000000902020009008000080450010007006000000309900150000306000040']  # pb 3251
    grillesudo[16]=['000040000000002010692800040030000900700000081000580006400035090063900400000004007']  # pb 3261
    grillesudo[17]=['000040000000002010692800043030000900700000081000580006400035090063900400000004007']  # pb 3271
    # grilles expert  de 18 à 23 (puis mixées)
    grillesudo[18]=['000020094010080003600000200308070000470000030000200010002800007030000000057006900']  # pb 4241
    grillesudo[19]=['012000000000401080000000340903050002104000000806020007000000610000608050087000000']  # pb 4242
    grillesudo[20]=['380027050006800032009500800600010000000300060004200009120008005090000003000050004']  # pb 4271
    grillesudo[21]=['080020094010080003600000200308070000470060030000200010062800007030000800057006900']  # pb 4281
    grillesudo[22]=['000800300000000058308052000080000073400000260007640900000003820050094000603020514']  # pb 4301
    grillesudo[23]=['500870060700265004600094080060000250975100006120056900000002500051000000400009000']  # pb 4321
    # grilles diaboliques de 24 à 29 (puis mixées)
    grillesudo[24]=['930000200000002000600470000002000400000357000006000300000080005000100000054000017']  # pb 4211
    grillesudo[25]=['000107000030000050002000100020070080097000420000605000400050002601000809000080000']  # pb 4231
    grillesudo[26]=['000510007000000492400800000007000100802600050000000000100070008006008205000040030']  # pb 4232
    grillesudo[27]=['000514007000000492400800500007000100802600050000000000100070008006008205000040030']  # pb 4251
    grillesudo[28]=['000306700800500020400700000090000073000003009305000100080060040902000007057009000']  # pb 4253
    grillesudo[29]=['000000040002400500000287000025000008900800050080001060700000801200063005050000730']  # pb 4261

    k=choixgrille[0]    
    grsudo=str(grillesudo[k])  # chaine de 85 caractères 2+81+2
    
    # grille sudoku
    for l in range(9):
        for c in range(9):
            i=l*9+c;v=grsudo[i+2]
            grille[l,c]=v
    
    mixer_valeurs()   # pour obtenir de nouvelles grilles
    initjeu()  # initialisation du jeu
# ..................................................
# pour afficher toutes les grilles
import matplotlib.pyplot as plt
mat = [[1,1,1,9,9,9,1,1,1],[1,1,1,9,9,9,1,1,1],[1,1,1,9,9,9,1,1,1],
    [9,9,9,1,1,1,9,9,9],[9,9,9,1,1,1,9,9,9],[9,9,9,1,1,1,9,9,9],
    [1,1,1,9,9,9,1,1,1],[1,1,1,9,9,9,1,1,1],[1,1,1,9,9,9,1,1,1]]
# *******************************************************
         
def k20(): # affiche toute les grilles avec matplotlib
    ct=0 
    for l in range(9):   
        for c in range(9):
            if grille[l,c]>0 :
                ct=ct+1
    compt=str(ct)
    initjeu()
    MAJgrilleVU()
    MAJgrillePU()
    MAJdoubles()
    
    figure = plt.figure()

    axes = figure.add_subplot(2,2,1)
    axes.matshow(mat, cmap='Pastel1')
    
    # affiche la grille
    axes.set_xticks(range(9))
    axes.set_xticklabels(['1','2','3','4','5','6','7','8','9'],fontsize=7)
    axes.set_yticks(range(9))
    axes.set_yticklabels(['1','2','3','4','5','6','7','8','9'],fontsize=7)
    axes.set_title('sudoku ',color="r",fontsize=8)
    axes.text(4,10, compt+"/81", fontsize=8,ha="center", va="center", color="b")

    s=0
    for l in range(9) :
        for c in range(9):
            s=s+ grilleVU[l,c] + grillePU[l,c]
            if grille[l,c]>0:
                axes.text(c,l, int(grille[l,c]), fontsize=8,ha="center", va="center", color="b")

    if s==0 :  # (ni VU ni PU sans majdd)
        s2=0
        MAJdd()
        for l in range(9) :
            for c in range(9):
                s2=s2+ grilleVU[l,c] + grillePU[l,c]
        
        if s2 >0 :            
            axes.text(7,21, "après MAJ-doubles-doubles des possibles", fontsize=9,ha="center", va="center", color="b")
        else :
            axes.text(20.5,21,"jouer un double", fontsize=9,ha="center", va="center", color="r")
    
    # valeurs uniques
    axes = figure.add_subplot(3,3,7)
    axes.matshow(mat, cmap='cool')
    axes.set_xticks(range(9))
    axes.set_xticklabels(['','','','','','','','',''])
    axes.set_yticks(range(9))
    axes.set_yticklabels(['','','','','','','','',''])
    axes.set_title('possibles uniques par cellules',fontsize=8,color="m")
    
    for l in range(9) :
        for c in range(9):
            if grilleVU[l,c]>0 :
                axes.text(c,l, int(grilleVU[l,c]), fontsize=8,ha="center", va="center", color="b")
        
    # possibles uniques
    
    axes = figure.add_subplot(3,3,8)

    axes.matshow(mat, cmap='cool_r')

    axes.set_xticks(range(9))
    axes.set_xticklabels(['','','','','','','','',''])
    axes.set_yticks(range(9))
    axes.set_yticklabels(['','','','','','','','',''])
    axes.set_title('possibles uniques par zones',fontsize=8,color="k")
    for l in range(9) :
        for c in range(9):
            if grillePU[l,c]>0 :
                axes.text(c,l, int(grillePU[l,c]), fontsize=8,ha="center", va="center", color="b")
    
    # doubles
    
    axes = figure.add_subplot(3,3,9)

    axes.matshow(mat, cmap='Set3')
    #axes.matshow(mat, cmap='Wistia')

    axes.set_xticks(range(9))
    axes.set_xticklabels(['','','','','','','','',''])
    axes.set_yticks(range(9))
    axes.set_yticklabels(['','','','','','','','',''])
    axes.set_title('deux possibles par cellules',color="b",fontsize=8)
    for l in range(9) :
        for c in range(9):
            if grilleD[l,c]>0 :
                if grilleDD[l,c]>0 :
                    axes.text(c,l, int(grilleD[l,c]), fontsize=8,ha="center", va="center", color="r")
                else :
                    axes.text(c,l, int(grilleD[l,c]), fontsize=7,ha="center", va="center", color="b")

    # solution
    
    ct=0
    for l in range(9) :
        for c in range(9):
            if grillesol[l,c]>0 :
                ct=ct+1
    if ct==81:            
        axes = figure.add_subplot(2,2,2)
        axes.matshow(mat, cmap='Wistia')
        #axes.matshow(mat, cmap='Set3')
        #axes.matshow(mat, cmap='spring')
        #axes.matshow(mat, cmap='autumn')
        
        #axes.matshow(mat, cmap='Purples')
        #axes.matshow(mat, cmap='Paired')
        #axes.matshow(mat, cmap = plt.cm.gist_rainbow)

        axes.set_xticks(range(9))
        axes.set_xticklabels(['','','','','','','','',''])
        axes.set_yticks(range(9))
        axes.set_yticklabels(['','','','','','','','',''])
        axes.set_title('solution',color="b",fontsize=8)
        for l in range(9) :
            for c in range(9):
                axes.text(c,l, int(grillesol[l,c]), fontsize=7,ha="center", va="center", color="k")
  
    #plt.savefig('aide.png',bbox_inches='tight', dpi =200)
    
    plt.show()  
# ..................................................
# ..................................................
# définitions des variables utilisées et initialisation en (l,c) = (5,5)
num_ligne=[0] ; num_ligne[0]=5
num_colonne=[0] ; num_colonne[0]=5
num_valeur=[0] # mémorisation de la valeur jouée (de 1 à 9)

# ..................................................
#programme principal    (pour jouer avec le clavier et la souris)
import turtle  
from turtle import *  # importer les fonctions du module turtle
tracer(0) # fonction
# valeur 0 : pointeur et déplacement (rapide) non visibles
# valeur 1 : pointeur et déplacement (lent) visibles
# ..................................................
# commande à partir de la souris :
turtle.onscreenclick(action) # action à partir des coordonnées (x,y) pointées par la souris

# ..................................................
wn = turtle.Screen()  # pour utiliser le clavier
# ..................................................
# définitions des commandes à partir du clavier

wn.onkey(k0, "0") # pour enlever une valeur dans la case pointée
wn.onkey(k1, "1") # pour jouer 1
wn.onkey(k2, "2")
wn.onkey(k3, "3")
wn.onkey(k4, "4")
wn.onkey(k5, "5")
wn.onkey(k6, "6")
wn.onkey(k7, "7")
wn.onkey(k8, "8")
wn.onkey(k9, "9")

# autre commande à partir du clavier
wn.onkey(k30, "+") # pour ajouter une valeur de la solution

wn.listen() # en mode 'tortue' le programme 'écoute' le clavier et suit les instructions
# ..................................................      
# initialisations :

nouv_sudo[0]=0 # saisir grille est faux
messages() # affiche le menu

# ..................................................
#n=input()    # ajouter # pour jouer avec IDLE
