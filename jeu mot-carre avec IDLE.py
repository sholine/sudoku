# jeu mot-carré avec Résolution de sudokus de niveau 1 et 2

import numpy as np
grille=np.zeros((9,9))
# ..................................................
grillesauv=np.zeros((9,9))  # pour restituer la grille si nécessaire

# ..................................................
def initjeu():
    # initialisations des possibles
    for l in range(9):   
        for c in range(9):
            grilleVU[l,c]=0
            grillePU[l,c]=0
    for i in range(81) :
        tabpos[i]=[1,2,3,4,5,6,7,8,9]    
    MAJtabpos()       
    MAJgrilleVU()  # pour résolution niveau 1
    MAJgrillePU()  # pour résolution niveau 2
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
# niveau 1
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
            grillesol[l,c]=grille[l,c]
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
                grillesol[l,c]=grille[l,c]
                if grille[l,c]>0 :
                    ct=ct+1
        
    ct=0 
    for l in range(9):   
        for c in range(9):
            if grille[l,c]>0 :
                ct=ct+1    
    if sol>-1:
        if ct == 81 :
            affiche_grille(grille)
            print ("   ",ct,"/ 81  (niveau 1)")
        else :
            print("pas de soution de niveau 1 : ",ct,"réponses / 81")
          
    # retour au jeu
    for l in range(9):   
        for c in range(9):
            grille[l,c]=grillesauv[l,c]
    initjeu()    
# ..................................................
# niveau 2
# ..................................................
grillePU=np.zeros((9,9))  # initialisation de la grille des possibles uniques par zones
# ..................................................
def MAJgrillePU() :
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
# mixer permuter valeurs

indicesinitiaux=[0,1,2,3,4,5,6,7,8]
indicespermutés=[-1,-1,-1,-1,-1,-1,-1,-1,-1]
grilleinit=np.zeros((9,9))
# choix aléatoire d'une valeur
import random

def permuter_indices():
    
    for ip in range(0,9):
        j=random.randint(0,8-ip) # recherche aléatoire dans un vecteur qui rétrécit
        indicespermutés[ip]=indicesinitiaux[j]
        for j in range(j,8-ip):
            indicesinitiaux[j]=indicesinitiaux[j+1] # rétrécissement du vecteur courant
    for i in range(8):
        indicesinitiaux[i]=i  # ré-init indices
    #for i in range(8):
    #    print(indicesinitiaux[i]+1, "->",indicespermutés[i]+1,end ="  ")
    #print()
# ..................................................
def mixer_valeurs():
    #print("permutation des valeurs")  
    permuter_indices()
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
    
    j=random.randint(0,20)
    f=random.randint(1,7) # f indice fonction sur matrice
    
    #print("fonction",f,end="  ")

    if f == 1: # si f ==0 pas d'action
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
        
    #affiche_grille(grille)
    perm3kcl()  # permutation des carrés alignés par colonnes
    perml_3k()  # permutation des 3 lignes de 3 carrés alignés
    permc_3k()  # permutation des 3 colonnes de 3 carrés superposés

    initjeu()  # initialisation du jeu
    
# ..................................................
indicesinit3val=[0,1,2]
indicesperm3val=[-1,-1,-1]
# ..................................................
def permuter_indices3val():
    
    for ip in range(3):   # de 0 à 2
        j=random.randint(0,2-ip) # recherche aléatoire dans un vecteur qui rétrécit
        indicesperm3val[ip]=indicesinit3val[j]
        for j in range(j,2-ip):
            indicesinit3val[j]=indicesinit3val[j+1] # rétrécissement du vecteur courant
    for i in range(3):
        indicesinit3val[i]=i  # ré-init indices
            
def perm3kcl():
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
            
def sd_dg():    # symétrie diagonale droite-gauche
    for l in range(9):   # mémorisation initiale de la grille de départ
        for c in range(9):
            grillesauv[l,c]=grille[l,c]
    for l in range(9):
        for c in range(9):
            grille[c,l]=grillesauv[l,c]
def sd_gd():  # symétrie diagonale gauche-droite
    for l in range(9):   # mémorisation initiale de la grille de départ
        for c in range(9):
            grillesauv[l,c]=grille[l,c]
    for l in range(9):
        for c in range(9):
            grille[c,l]=grillesauv[8-l,8-c]
def rg():    # rotation à gauche
    for l in range(9):   # mémorisation initiale de la grille de départ
        for c in range(9):
            grillesauv[l,c]=grille[l,c]
    for l in range(9):
        for c in range(9):
            grille[c,l]=grillesauv[l,8-c]
def rd():    # rotation à droite
    for l in range(9):   # mémorisation initiale de la grille de départ
        for c in range(9):
            grillesauv[l,c]=grille[l,c]
    for l in range(9):
        for c in range(9):
            grille[c,l]=grillesauv[8-l,c]
def sv() :    # symétrie verticale
    for l in range(9):   # mémorisation initiale de la grille de départ
        for c in range(9):
            grillesauv[l,c]=grille[l,c]
    for l in range(9):
        for c in range(9):
            grille[l,c]=grillesauv[l,8-c]
def sh():   # symétrie horizontale
    for l in range(9):   # mémorisation initiale de la grille de départ
        for c in range(9):
            grillesauv[l,c]=grille[l,c]
    for l in range(9):
        for c in range(9):
            grille[l,c]=grillesauv[8-l,c]
def f7():   # symétrie axiale (ou rotation 180°)
    rd();rd()

def perml_3k():   # permutation des lignes successives dans alignements de 3 carrés
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

def permc_3k():
    #print("permutation des colonnes successives dans superpositions de 3 carrés")
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
def affiche_grille(grille) :
    print()
    
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
    print ("└———————┴———————┴———————┘  ")
    
# ..................................................
import turtle as turtle # pour afficher le jeu avec turtle

from turtle import *  # pour importer les fonctions du module turtle
   
num_ligne=[0]
num_ligne[0]=5
num_colonne=[0]
num_colonne[0]=5
num_valeur=[0]
x0=-210  # emplacement dessin du pendu
# ..................................................
penduindice=[0]
def choixpendu():
    
    tracer(0) # dessin instantané
    i=penduindice[0]
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
    tracer(1) # pour re-voir le pointeur
# ..................................................
    
def  pendu1() : # soleil
    color("white")
    up();goto(x0+140,190);color("black")  
    write(chr(9788),font=("Arial", 60, "normal"),align="center")

def  pendu2() :
    x=x0-30;y=-35  # banc
    color("white")
    pensize(4)  # taille de la ligne
    up();goto (x,y);color("black");down(); goto(x+55,y);up()
def  pendu3() :   
    up();goto(x0,68)  # tête gaie
    color("white")
    color("black")
    write(chr(9786),font=("Arial", 40, "normal"),align="center")
def  pendu4() :    
    color("white")
    up();goto(x0,10);color("black")  # tronc haut
    write(chr(8898),font=("Arial", 55, "normal",'bold'),align="center")
    goto(x0,-13)   # tronc bas    
    write(chr(8899),font=("Arial", 55, "normal",'bold'),align="center")
def  pendu5() : 
    color("white")
    x=x0-18;y=+62 # bras gauche
    pensize(5)  # taille de la ligne
    up();goto (x,y);color("black");down(); goto(x-10,y-22);up()
def  pendu6() :     
    color("white")
    x=x0+14;y=+62  # bras droit
    pensize(5)  # taille de la ligne
    up();goto (x,y);color("black");down(); goto(x+11,y-22);up() 
def  pendu7() : 
    x=x0-10;y=10 # pied gauche
    pensize(5)  # taille de la ligne
    up();goto (x,y);color("black");down(); goto(x-10,y-40);up()
def  pendu8() : 
    x=x0+6;y=10  # pied droit
    pensize(5)  # taille de la ligne
    up();goto (x,y);color("black");down(); goto(x+8,y-40);up() 
def  pendu9() : 
    color("white")
    x=x0-80;y=-60  # sol
    pensize(4)  # taille de la ligne
    up();goto (x,y);color("grey");down(); goto(x+130,y);up() 
def  pendu10() : 
    color("white")
    x=x0-70;y=-60  # potence verticale
    pensize(4)  # taille de la ligne
    up();goto (x,y);color("black");down(); goto(x,y+210);up() 
def  pendu11() : 
    color("white")
    x=x0-70;y=149  # potence horizontale
    pensize(4)  # taille de la ligne
    up();goto (x,y);color("black");down(); goto(x+80,y);up() 
def  pendu12() : 
    color("white")
    x=x0-70;y=130  # potence angle
    pensize(4)  # taille de la ligne
    up();goto (x,y);color("black");down(); goto(x+19,y+19);up() 

def  pendu13() : # fin
    color("white")
    x=x0;y=149  # corde - banc
    pensize(2)  # taille de la ligne
    up();goto (x,y);color("grey");down(); goto(x,y-42);up()
    x=x0-30;y=-35  # banc
    pensize(4)  # taille de la ligne    
    up();goto (x,y);color("white");down(); goto(x+55,y);up()

    up();goto(x0,68)  # tête gaie
    color("white")   # pour effacer la tête gaie
    write(chr(9786),font=("Arial", 40, "normal"),align="center")
    color("black")
    up();goto(x0,50)  # tête triste
    write(chr(9785),font=("Arial", 55, "normal"),align="center")
    color("white")    
    up()
    goto(x0-60,-180) # tête échec
    color("black")
    write(chr(9760),font=("Arial", 70, "normal"),align="center")
    color("white")
    up();goto(x0+20,-160);color("black") # cercueil
    write(chr(9904),font=("Arial", 40, "normal"),align="center")
    for i in range(9):
        up()
        goto(-107+i*35,-170) # tête échec
        color("red")
        write(motcaré[i],font=("Arial", 12))
# ..................................................  
def  dessiner_grille() : # et remplir la grille avec Turtle
    left(90)
    color("blue")
    x0=-122;y0=173  # emplacement du point en haut, à gauche de la grille
    for i in range(10):
        if i%3==0:
            pensize(3)  # taille du trait
        else:
            pensize(1)
        color("white");up();goto (x0,y0-i*35)
        down();color("blue");goto (x0+9*35,y0-i*35)  # ligne horizontale
        color("white");up();goto (x0+i*35,y0)
        down();color("blue");goto (x0+i*35,-142)  # ligne verticale
        
# ..................................................  
        
def k21():
    exit()

def k22(): # . nouveau jeu nouvelle grille
    #plt.close() # ferme la fenêtre d'aide si elle est ouverte
    # efface fenêtre
    resetscreen()
    penduindice[0]=0
    num_colonne[0]=5;num_ligne[0]=5
    mots_carrés() # nouveau jeu : choix de grille et de mot à trouver 
    
        
def k30() : # ! affiche définition
    
    # efface message
    tracer(0)
    up();color ("yellow");goto(-120,-190);down();pensize(30);goto(200,-190)
    # affiche définition
    up();goto(35,-200);color("black")    
    write(defmot[0], font=("Arial", 12),align="center")
    color("white")
    l=num_ligne[0]-1;c=num_colonne[0]-1
    x=35*(c-3);y=35*(4-l)+5 # position du caractère à écrire
    up(); goto(x,y);color("red")
    for j in range (8):
        penduindice[0]=penduindice[0]+1;choixpendu()  # 8 pénalités
    
    up();color ("red")
    goto(35*(num_colonne[0]-4)+4,35*(5-num_ligne[0])) # replacer le pointeur
    tracer(1) # pour voir le pointeur
    
def k31():
    letr='a'
    valid_lettr(letr)
def k32():
    letr='b'
    valid_lettr(letr)
def k33():
    letr='c'
    valid_lettr(letr)
def k34():
    letr='d'
    valid_lettr(letr)
def k35():
    letr='e'
    valid_lettr(letr)
def k36():
    letr='f'
    valid_lettr(letr)
def k37():
    letr='g'
    valid_lettr(letr)
def k38():
    letr='h'
    valid_lettr(letr)
def k39():
    letr='i'
    valid_lettr(letr)
def k40():
    letr='j'
    valid_lettr(letr)
def k41():
    letr='k'
    valid_lettr(letr)
def k42():
    letr='l'
    valid_lettr(letr)
def k43():
    letr='m'
    valid_lettr(letr)
def k44():
    letr='n'
    valid_lettr(letr)
def k45():
    letr='o'
    valid_lettr(letr)
def k46():
    letr='p'
    valid_lettr(letr)
def k47():
    letr='q'
    valid_lettr(letr)
def k48():
    letr='r'
    valid_lettr(letr)
def k49():
    letr='s'
    valid_lettr(letr)
def k50():
    letr='t'
    valid_lettr(letr)
def k51():
    letr='u'
    valid_lettr(letr)
def k52():
    letr='v'
    valid_lettr(letr)
def k53():
    letr='w'
    valid_lettr(letr)
def k54():
    letr='x'
    valid_lettr(letr)
def k55():
    letr='y'
    valid_lettr(letr)
def k56():
    letr='z'
    valid_lettr(letr)
# ..................................................

def get_mouse_click_coor(x, y):  # programme principal avec tortue
    # à partir des coordonnées x et y pointées par la souris
    color("red")
    numcol=int((x+10)//35 +4)
    numlig=int(5-y//35)
    if (numlig <10 and numcol<10) and (numlig >0 and numcol>0):
        num_colonne[0]=int((x+10)//35 +4)
        num_ligne[0]=int(5-y//35)
        
    up();color ("white")
    goto(35*(num_colonne[0]-4)+4,35*(5-num_ligne[0])) # replacer le pointeur
    color("red")
# ..................................................

# commandes clavier
wn = turtle.Screen()  # commande nécessaire pour utiliser onkey

wn.onkey(k21, "/") # quitter
wn.onkey(k22, "*") # nouveau jeu nouvelle grille
wn.onkey(k30, "!") # affiche définition

wn.onkey(k31, "a")
wn.onkey(k32, "b")
wn.onkey(k33, "c")
wn.onkey(k34, "d")
wn.onkey(k35, "e")
wn.onkey(k36, "f")
wn.onkey(k37, "g")
wn.onkey(k38, "h")
wn.onkey(k39, "i")
wn.onkey(k40, "j")
wn.onkey(k41, "k")
wn.onkey(k42, "l")
wn.onkey(k43, "m")
wn.onkey(k44, "n")
wn.onkey(k45, "o")
wn.onkey(k46, "p")
wn.onkey(k47, "q")
wn.onkey(k48, "r")
wn.onkey(k49, "s")
wn.onkey(k50, "t")
wn.onkey(k51, "u")
wn.onkey(k52, "v")
wn.onkey(k53, "w")
wn.onkey(k54, "x")
wn.onkey(k55, "y")
wn.onkey(k56, "z")
# ..................................................
# mot carré
# ..................................................
valeur_lettre=[0,0,0,0,0,0,0,0,0] # 9 valeurs pour les 9 mettres du motcarré

grillemot=['','','','','','']
grmot=['']
defmot=['']
motcaré=['','','','','','','','','']
motcarré = []
defmotcarré =  ['','','','','','','','','','','','','','','','','','','','',
             '','','','','','','','','','','','','','','','','','','','',
             '','','','','','','','','','','','','','','','','','','','','']
             
motcarré.append('COURTISAN')
defmotcarré[0] = 'attaché à la cour'
motcarré.append('ERUPTIONS')
defmotcarré[1] = 'surgissements'
motcarré.append('POINTURES')
defmotcarré[2] = 'qui excellent'
motcarré.append('ALTRUISME')
defmotcarré[3] = 'valeur morale'
motcarré.append('SALICORNE')
defmotcarré[4] = 'sur le bord de la mer'
motcarré.append('RELUISANT')
defmotcarré[5] = 'brillant'
motcarré.append('RELATIONS')
defmotcarré[6] = 'rapports de dépendance'
motcarré.append('SCOLARITE')
defmotcarré[7] = 'durée de plusieurs années'
motcarré.append('MONITEURS')
defmotcarré[8] = "chargés d'encadrer"
motcarré.append('CHERUBINS')
defmotcarré[9] = 'esprit céleste de second rang'
motcarré.append('BISCORNUE')
defmotcarré[10] = 'bizarre'
motcarré.append('SIGNATURE')
defmotcarré[11] = 'marque qui identifie'
motcarré.append('NOSTALGIE')
defmotcarré[12] = 'mal du pays'
motcarré.append('NATURISME')
defmotcarré[13] = 'style de vie'
motcarré.append('SOURIANTE')
defmotcarré[14] = 'de bonne humeur'
motcarré.append('ARCHIPELS')
defmotcarré[15] = 'groupes formant une unité géographique'
motcarré.append('FOCALISER')
defmotcarré[16] = 'concentrer'
motcarré.append('TOURNEVIS')
defmotcarré[17] = 'gendarme'
motcarré.append('BUCHERONS')
defmotcarré[18] = 'travaillent dans le bois'
motcarré.append('CONFISEUR')
defmotcarré[19] = 'fait ou vend des produits comestibles'
motcarré.append('OBSCURITE')
defmotcarré[20] = "défaut d'intelligibilité"
motcarré.append('CONFITURE')
defmotcarré[21] = 'mélange gélifié'
motcarré.append('URBANISTE')
defmotcarré[22] = 'spécialiste de plans'
motcarré.append('VOCALISER')
defmotcarré[23] = 'parcourir une échelle'
motcarré.append('TOURAINES')
defmotcarré[24] = 'qui habitent une commune du Vaucluse'
motcarré.append('SOBRIQUET')
defmotcarré[25] = 'surnom'
motcarré.append('BRAIMENTS')
defmotcarré[26] = "cris d'ânes"
motcarré.append('PATINEURS')
defmotcarré[27] = 'peuvent être sur roulettes'
motcarré.append('DINOSAURE')
defmotcarré[28] = 'personne de grande influence'
motcarré.append('DOUANIERS')
defmotcarré[29] = 'vérifient les marchandises'
motcarré.append('NOIRAUDES')
defmotcarré[30] = 'ont le teint brun'
motcarré.append('REDUCTION')
defmotcarré[31] = 'diminution'
motcarré.append('BRUTALISE')
defmotcarré[32] = 'violenté'
motcarré.append('URBANISME')
defmotcarré[33] = "art de l'aménagement"
motcarré.append('ROUMAINES')
defmotcarré[34] = 'habitent en Europe orientale'
motcarré.append('AUMONIERS')
defmotcarré[35] = 'écclésiastique'
motcarré.append('ORGANISME')
defmotcarré[36] = 'être vivant'
motcarré.append('PARTICULE')
defmotcarré[37] = 'partie infime'
motcarré.append('ANTICORPS')
defmotcarré[38] = 'protéine'
motcarré.append('PYROMANIE')
defmotcarré[39] = 'impulsion obsédante'
motcarré.append('PLASTIQUE')
defmotcarré[40] = 'malléable'
motcarré.append('EXCLUSION')
defmotcarré[41] = 'relation logique'
motcarré.append('COMPTABLE')
defmotcarré[42] = 'responsable'
motcarré.append('SOUHAITER')
defmotcarré[43] = 'désirer'
motcarré.append('CONSULTER')
defmotcarré[44] = 'délibérer'
motcarré.append('SOULIGNER')
defmotcarré[45] = 'faire ressortir'
motcarré.append('INCOMPLET')
defmotcarré[46] = 'partiel'
motcarré.append('OBLIGEANT')
defmotcarré[47] = 'rend service'
motcarré.append('COMPLIQUE')
defmotcarré[48] = 'alambiqué'
motcarré.append('CONJUGALE')
defmotcarré[49] = "propre à l'union"
motcarré.append('CLIGNOTER')
defmotcarré[50] = 'par intermittence'
motcarré.append('CHALOUPER')
defmotcarré[51] = 'se balancer'
motcarré.append('IMPORTUNE')
defmotcarré[52] = 'incommodé'
motcarré.append('CENSORIAL')
defmotcarré[53] = 'pour une juridiction'
motcarré.append('CARBONYLE')
defmotcarré[54] = "mélange d'huiles"
motcarré.append('FORMALITE')
defmotcarré[55] = 'procédure'
motcarré.append('PATCHOULI')
defmotcarré[56] = 'plante tropicale'
motcarré.append('PASTICHER')
defmotcarré[57] = 'imiter'
motcarré.append('PALUDISME')
defmotcarré[58] = 'maladie tropicale'



def mots_carrés():   # nouveau jeu : choix de grille et de mot à trouver 
    tracer(0)
    indicemot=random.randint(0,len(motcarré))
    
    mot=motcarré[indicemot]
    
    for i in range(9):
                motcaré[i]=mot[i] # mise en mémoire du mot à trouver
        
    defmot[0]=defmotcarré[indicemot]
    
    # choisir une grille    
    grillemot[0]=['002900807403020000000008004005000000090000000030001500010002409600080070700004005']  # pb 1242
    grillemot[1]=['050803700030040010060057000000005096700004800009100000000000153000000000300000270']  # pb 2243
    grillemot[2]=['000060001207030040009000007000010000000540000000000230900008000050470000010006809']  # pb 2221
    grillemot[3]=['600200008007000050800040700040000030005400060010025009070090000000000005000080041']  # pb 2231
    grillemot[4]=['010004000080000036000002010002080000706000509000700000070405000150000090000370060']  # pb 2232
    grillemot[5]=['030060000600879000700000000080300060103000009000050027000000180009020070000000504']  # pb 2233
    for j in range(40):
        ind=random.randint(0, 5) # choix aléatoire de i

    grmot=str(grillemot[ind])  # chaine de 85 caractères 2+81+2

    # grillle sudoku
    for l in range(9):
        for c in range(9):
            i=l*9+c;v=grmot[i+2]
            grille[l,c]=v
                    
    mixer_valeurs()
    initjeu()  # initialisation du jeu
        
    for l in range(9):
        for c in range(9):
            grillesauv[l,c]=grille[l,c] # mémorise la grille
    solution2(-1)  # trouve la solution (grilles de niveaus 1 ou 2)
       
    for l in range(9):
        for c in range(9):
            grille[l,c]=grillesauv[l,c] # restitue la grille
    
    #choix de lignemot    
    ctmini=9 # compteur mini de lettres par ligne de la grille à jouer
    for l in range(9):
        ct=0
        for c in range(9):
            if grille[l,c]>0:
                ct =ct+1
        if ct<=ctmini :
            ctmini=ct
            lignemot=l  # ligne où le compteur est le plus petit
        
    for c in range(9):
        valeur=int(grillesol[lignemot,c])
        valeur_lettre[c]=valeur
    
    # affiche messages fenêtre tortue
    color("white");up();goto (-200,200);color("red")
    write('Mot carré',font=("Arial", 16, "normal"),align="center")
    x=35*(-3);y=35*(4-lignemot)+15
    color("white");goto(x,y)
    down()
    color("yellow");pensize(27)  # couleur et taille de la ligne à trouver
    goto (x+282,y)
    color("white");up()
    x=35*6-5;y=35*(4-lignemot)
    goto(x,y+6)
    color("red")
    write("mot à trouver", font=("Arial", 12))
    color("white");up()
    goto(35,-200);color("black")
    write('!   pour voir la définition', font=("Arial", 12),align="center")
    
    color("white");up()    
    goto(-100,-230)
    color("black")
    write('/  pour quitter', font=("Arial", 12))
    goto(100,-230)
    write('*  nouveau jeu', font=("Arial", 12))

    #affiche_grille_motcarré
    tracer(0)
    dessiner_grille()
    
    # compléter la grille
    color("black")
    for ind in range(9):
        valeur_lettre[ind] != v
    while ct<81 :        
        ind=0
        ct=0
        for l in range(9) :
            for c in range(9):
                if c==0:  # affichage                    
                    if l== lignemot:                    
                        color("red")
                    else :
                        color("black")
                if grille[l,c]>0:
                    v=int(grille[l,c])
                    ind=0
                    while valeur_lettre[ind] != v :
                        ind=ind+1
                    let=motcaré[ind]
                    
                    color("white");up()
                    x=35*(c-3)-4;y=35*(4-l)
                    goto(x,y)          
                    color("black");write(let, font=("Arial", 18))
                        
        ct=81   
    up();goto(35,0) # position initiale du pointeur
    tracer(1)
    color("red")
    wn.listen() # en mode 'tortue' le programme écoute et suit les instructions

def valid_lettr(letr):
    l=num_ligne[0]-1;c=num_colonne[0]-1  # de 0 à 8      
    v=int(grillesol[l,c])
    
    ind=0
    while valeur_lettre[ind] != v:
        ind=ind+1
       
    letrsol=motcaré[ind]  # lettre à touver len l,c
           
    if ord(letr) == ord(letrsol)+32 :  # si le choix est bon
        grille[l,c]=grillesol[l,c]
        
        up()
        x=35*(c-3)-5;y=35*(4-l) # position du curseur d'écriture
        goto(x,y)          
        color("blue");write (letrsol, font=("Arial", 18))
        color("red");up();goto(x+6,y)
    else :       # si pas dans solution
        penduindice[0]=penduindice[0]+1 # alors pénalité
        choixpendu()  # = pénalisation pour erreur
        grille[l-1,c-1]=0
        color("white")
        x=35*(c-3);y=35*(4-l)+5 # position du caractère à écrire
        up(); goto(x,y);color("red") 

# ..................................................
# programme pour jouer avec la tortue
mots_carrés() # nouveau jeu : choix de grille et de mot à trouver 
    
onscreenclick(get_mouse_click_coor)   # à partir des coordonnées faire ...
   
wn.listen() # en mode 'tortue' le programme écoute et suit les instructions du clavier

# ..................................................
#suite=input("Avec IDLE appuyer ici sur une Entrée pour jouer")
# le programme continue tel une application ...
# ..................................................
