# Résolution de sudokus de niveau 1 4 et jeu mot-carré

import numpy as np

grille=np.zeros((9,9))

# ..................................................
def continuer():   # tant que la grille n'est pas complète
    initjeu()    
    menu()  # pour choix d'action    
    continuer() # retour au menu sauf si 'quitter'
# ..................................................
def menu():
    print("...................................................................")
    print("   n  : pour saisir au clavier une nouvelle grille")
    print("   c  : pour charger une grille")
    print("   g  : pour générer une grille complète")
    ct=0
    
    for l in range(9):   
        for c in range(9):
            grillesauv[l,c]=grille[l,c]
            if grille[l,c]>0:
                ct=ct+1
    #if ct>0:
    #   solution(-1)
    ct=0
    for l in range(9):   
        for c in range(9):
            if grillesol[l,c]>0:
                ct=ct+1
    if ct==81:
        print("  gs  : pour générer un nouveau jeu sudoku ")
    print("   q  : pour quitter ")
    
    ct=0
    for l in range(9):   
        for c in range(9):
            if grille[l,c]>0:
                ct=ct+1
    if ct>0:
        affiche_grille(grille)
        print("        ",ct,"/ 81")
        print("jouer : un nombre de 3 chiffres (lcv) ligne - colonne - valeur ")
        print("   s  : pour sauvegarder la grille ")
        print("   g  : pour générer une grille complète")

        print("   a  : (aide) affiche les possibles par cellules ou par zones")
        print("   +  : modif (aide) pour ajouter une valeur de la solution")
        print("  sol : pour afficher la solution du sudoku")
        print("  mx  : nouvelle grille en mixant les valeurs " )
        
        print("   l  : pour lister les valeurs à enlever (pour le même niveau)")
        print("   -  : pour enlever une valeur")
        print("...................................................................")
    ch=choix()
# ..................................................
def RAZposs(): # RAZ des possibles
    for l in range(9):   
        for c in range(9):
            grilleVU[l,c]=0            
    for i in range(81) :
        tabpos[i]=[1,2,3,4,5,6,7,8,9]
# ..................................................
ligne=[0,0,0,0,0,0,0,0,0] # init
def nouvellegrille():  # saisie au clavier
    numpb[0]=0
    for l in range(9): # saisie de 9 lignes de 9 valeurs
        lig=""
        while len(lig) != 9 :
            print("ligne",l+1, end ="  ")
            lig= input()            
        ligne[l]=lig
    for l in range(9):  # compléter la grille (9x9)
        lig=ligne[l]
        for c in range(9):
            v=lig[c]
            if v==" " :  # v : espace ou zéro
                grille[l,c]=0
            else :      # v nombre de 1 à 9
                grille[l,c]=v
    initjeu()  # initialisation du jeu
# ..................................................
def affiche_grille(grille) :
    nom=""
    if numpb[0]>0 :
        num=str(numpb[0]);nom="pb"+num+".txt"
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
    print("       ",nom)
    
# ..................................................
def sauvegrille():
    
    listepb()
    rep="oui"
    while rep=="oui":
        num=input("Numéro de sauvegarde de la grille : ")
        nom="pb"+num+".txt"
        if nom in os.listdir():
            #rep="oui"
            rp=input("écraser pb existant o/n ?  ")
            if rp=="o":
                rep="non" # autorisation à écraser
        else :
            rep="non"
            
    if num>"":
        if str(num) <= "9" :
            numpb[0]=int(num)
    
    cpt=1
    with open(nom,"w") as filout :
        for l in range(9):
            for c in range(9):
                v= str(int(grille[l,c]))
                filout.write(v)
                if cpt % 9 == 0 :
                    filout.write("\n")
                cpt=cpt+1
# ..................................................
import os  # module OS pour lire les noms des fichiers
def listepb():     # Get .txt files
    rep=input("voulez-vous lister les pb enregistrés o/n ?  ")
    if rep=="o":
        suitelistepb()
        
def suitelistepb() :
    ct=0
    for nom in os.listdir():
        if nom.endswith('.txt'):            
            print ("{:<13s}".format(nom),end="") # format de 13 caractères
            ct=ct+1
            if ct%6==0: # 6 problèmes par ligne
                print()
    print()
# ..................................................
numpb=[0] # mémorisation du n° de problème chargé
def charger() : # charger une grille
    
    RAZposs()
    listepb()
    rep="non"
    while rep=="non":
        num=input("charger problème numéro ? : ")
        nom="pb"+num+".txt"
        if nom in os.listdir():
            rep="oui"
    if num>"":
        if str(num) <= "9" :
            numpb[0]=int(num)
        else :
            numpb[0]=0
    
    with open(nom,"r") as filin :
        vals=filin.read() # 9 lignes de 9 caractères        
        for l in range(9):
            for c in range(9):
                v=vals[l*9 + c+l] # on saute 1 caractère en fin de ligne
                grille[l,c]=int(v)
    
    initjeu()  # initialisation du jeu
# ..................................................
grillesauv=np.zeros((9,9))  # pour restituer la grille si nécessaire

def choix():
    ch=input("commande : ")
    
    if ch == "n":
        nouvellegrille()   # saisie d'une nouvelle grille
        for l in range(9):   
            for c in range(9):
                grillesauv[l,c]=grille[l,c]    
    elif ch == "s" :
        sauvegrille()
    elif ch > "0" and ch < "A" : # si choix est un nombre
        if int(ch) > 110 and int(ch) < 1000 :
            jouer(ch)
        else : # nombre incorrect
            continuer()    
    elif ch == "q" :
        exit()
    elif ch == "c" :
        charger()   # nouvelle grille
    elif ch == "a" : # aide pour jouer
        print()
        affiche_grille(grilleVU)
        print("valeurs uniques par cellules")
        affiche_grille(grillePU)
        print("possibles uniques par zones de 9 cellules")
        s=0 # si s>0 il y a des possibles uniques par cellules
        for l in range(9):   
            for c in range(9):
                s=s+grilleVU[l,c]+grillePU[l,c]
        if s==0:
            print()
            print("recherche des possibles à partir de doubles-doubles")
        
            MAJdd();MAJdd()
            affiche_grille(grilleVU)
            print("valeurs uniques par cellules")
            affiche_grille(grillePU)
            print("possibles uniques par zones de 9 cellules")
            s=0 # si s>0 il y a des possibles uniques par cellules
            for l in range(9):   
                for c in range(9):
                    s=s+grilleVU[l,c]+grillePU[l,c]
            if s==0:
                print()
                print("vous devez jouer un double")
                affichegrilledouble(grilleD)
    
            print()
    elif ch == "sol" :
        for l in range(9):   
            for c in range(9):
                grillesauv[l,c]=grille[l,c]
        solution(1)
    elif ch == "sol3" :
        for l in range(9):   
            for c in range(9):
                grillesauv[l,c]=grille[l,c]
        solution123(1)
        affiche_grille(grillesol)
    elif ch == "sol4" :
        for l in range(9):   
            for c in range(9):
                grillesauv[l,c]=grille[l,c]
        solution4(-1)
    
    elif ch == "mx" :
        mixer_valeurs()
    
    elif ch == "+" :
        ajouter_valeurs()
    elif ch == "l" :
        lister_valàenlever()
    elif ch == "-" :
        enlever()
    elif ch == "g":        
        générer()
    elif ch == "gs": 
        nouvelle_grille() # génère une grille aléatoire
# ....................................................
def générer() :
    générer_grille_initiale()
# ....................................................
# générer_grille_initiale()
choix_1_K2=np.zeros(9)
choix_2_K2=np.zeros(9)
choix_3_K2=np.zeros(9)
choix_4_K2=np.zeros(9)
choix_5_K2=np.zeros(9)
n_pos_val=np.zeros(9)

def générer_grille_initiale():
    générer_grille_initiale_5() # ---> teste choix n°5
        
def générer_grille_initiale_1():
    print ("choix n°1")
    # initialisations : remplit le 1er carré
    v=1
    for l in range(3):   
        for c in range(3):
            grille[l,c]=v
            v=v+1
    # choix quelconque de K2
    grille[0,3]=6;grille[0,4]=4;grille[0,5]=9
    grille[1,3]=3;grille[1,4]=8;grille[1,5]=7
    grille[2,3]=2;grille[2,4]=1;grille[2,5]=5
    # choix quelconque de L4 c1 c2 c3
    grille[3,0]=6;grille[3,1]=3;grille[3,2]=7
    
    affiche_grille(grille)
    print ("--> 66096 grilles")

    choix_lig4_col4() # suite
    # --> 66096 grilles

def générer_grille_initiale_2():
    print ("choix n°2")
    # initialisations : remplit le 1er carré
    v=1
    for l in range(3):   
        for c in range(3):
            grille[l,c]=v
            v=v+1
    # choix quelconque de K2
    grille[0,3]=9;grille[0,4]=4;grille[0,5]=5
    grille[1,3]=7;grille[1,4]=3;grille[1,5]=8
    grille[2,3]=1;grille[2,4]=6;grille[2,5]=2
    # choix quelconque de L4 c1 c2 c3
    grille[3,0]=8;grille[3,1]=4;grille[3,2]=1
    
    affiche_grille(grille)
    print ("--> 68832 grilles")

    choix_lig4_col4() # suite
    # --> 68832 grilles

def générer_grille_initiale_3():
    print ("choix n°3")
    # initialisations : remplit le 1er carré
    v=1
    for l in range(3):   
        for c in range(3):
            grille[l,c]=v
            v=v+1
    # choix quelconque de K2
    grille[0,3]=7;grille[0,4]=5;grille[0,5]=9
    grille[1,3]=3;grille[1,4]=8;grille[1,5]=1
    grille[2,3]=4;grille[2,4]=2;grille[2,5]=6
    # choix quelconque de L4 c1 c2 c3
    grille[3,0]=6;grille[3,1]=3;grille[3,2]=4
    
    affiche_grille(grille)
    print ("--> 66096 grilles")

    choix_lig4_col4() # suite
    # --> 66096 grilles

def générer_grille_initiale_4():
    print ("choix n°4")
    # initialisations : remplit le 1er carré
    v=1
    for l in range(3):   
        for c in range(3):
            grille[l,c]=v
            v=v+1
    # choix quelconque de K2
    grille[0,3]=9;grille[0,4]=6;grille[0,5]=5
    grille[1,3]=7;grille[1,4]=9;grille[1,5]=2
    grille[2,3]=1;grille[2,4]=3;grille[2,5]=4
    # choix quelconque de L4 c1 c2 c3
    grille[3,0]=5;grille[3,1]=9;grille[3,2]=2

    affiche_grille(grille)
    print ("--> 74514 grilles")

    choix_lig4_col4() # suite
    # --> 74514 grilles

def générer_grille_initiale_5():
    print ("choix n°5")
    # initialisations : remplit le 1er carré
    v=1
    for l in range(3):   
        for c in range(3):
            grille[l,c]=v
            v=v+1
    # choix quelconque de K2
    grille[0,3]=5;grille[0,4]=7;grille[0,5]=4
    grille[1,3]=7;grille[1,4]=9;grille[1,5]=8
    grille[2,3]=1;grille[2,4]=2;grille[2,5]=6
    # choix quelconque de L4 c1 c2 c3
    grille[3,0]=6;grille[3,1]=7;grille[3,2]=4

    affiche_grille(grille)
    print ("--> 73770 grilles")
    
    choix_lig4_col4() # suite
    # --> 73770 grilles
    
def générer_grille_initiale_b():    # pour générer une -grille initiale-
    print("générer_grille_initiale()")
    print("permet de générer toutes les grilles initiales possibles")

    numpb[0]=0 #init nom
    indice[0]=0 # utilisé comme compteur de possibilités
    
    # initialisations
    for l in range(9):   
        for c in range(9):
            grille[l,c]=0
    initjeu()
    # initialisations : remplit le 1er carré
    v=1
    for l in range(3):   
        for c in range(3):
            grille[l,c]=v
            v=v+1 

    choix_1_carré2() # remplit le carré 2 (1er choix) et cellules suivantes...
    
    print();print("nb de grilles ",indice[0])
    
    for l in range(9):   
        for c in range(9):
            grille[l,c]=grillesauv[l,c] # restitue la dernière grille initiale trouvée
    
# .................................................... 
def choix_1_carré2():  # complète 1ère cellule du carré (puis suivantes) 
    lig=0 ; col=3 # remplit cellule 0 du 2e carré 2 (cellules de  0 à 8)
    nb_poss_cel1=0 # nombre de possibles pour la 1ère cellule
    i2=0
    initjeu()
    
    for i1 in range(9):        
        val=tabpos[lig*9 +col,i1]
        if val>0:
            nb_poss_cel1=nb_poss_cel1 +1
            choix_1_K2[i2]=val
            i2=i2+1        
    
    for i_cell1 in range(nb_poss_cel1):
        #grille[0,3]=0  #init
        
        for i in range(3):  
            for j in range(3):
                grille[i,j+3]=0
                
        grille[lig,col]=choix_1_K2[i_cell1]        
        initjeu()
               
        choix_2_carré2()  # suite : complète la 2e cellule du carré (et les suivantes)
        
# .................................................... 
def choix_2_carré2():  # complète 2e cellule du carré (et suivantes)   
    lig=0 ; col=4 
    nb_poss_cel2=0
    i2=0
        
    for i1 in range(9):        
        val=tabpos[lig*9 +col,i1]
        if val>0:
            nb_poss_cel2=nb_poss_cel2 +1
            choix_2_K2[i2]=val
            i2=i2+1        
    
    for i_cell2 in range(nb_poss_cel2):
        grille[0,4]=0  #init
        grille[0,5]=0
        for i in range(1,3):  
            for j in range(3):
                grille[i,j+3]=0
                
        grille[lig,col]=choix_2_K2[i_cell2]
        
        initjeu()
                
        choix_3_carré2()  # suite : complète la 3e cellule du carré (et les suivantes)
# ....................................................
def choix_3_carré2():  # complète 3e cellule du carré (et suivantes)   
    
    lig=0 ; col=5 
    nb_poss_cel3=0
    i2=0
        
    for i1 in range(9):
        
        val=tabpos[lig*9 +col,i1]
        if val>0:
            nb_poss_cel3=nb_poss_cel3 +1
            choix_3_K2[i2]=val
            i2=i2+1
    #print();print(nb_poss_cel2,"nb de grilles ",indice[0])
    for i_cell3 in range(nb_poss_cel3):
        grille[0,5]=0  #init
        for i in range(1,3):  
            for j in range(3):
                grille[i,j+3]=0
                
        grille[lig,col]=choix_3_K2[i_cell3]
        
        initjeu()
        
        choix_4_carré2() # suite : complète la 4e cellule du carré (et les suivantes)
# ....................................................
def choix_4_carré2():  # indice = 3   complète 4e cellule du carré et suivantes   
    lig=1 ; col=3 #; indice=3
    nb_poss_cel4=0
    i2=0
    for i1 in range(9):
        val=tabpos[lig*9 +col,i1]
        if val>0:
            nb_poss_cel4=nb_poss_cel4 +1
            choix_4_K2[i2]=val
            i2=i2+1
        
    for i_cell4 in range(nb_poss_cel4):

        for i in range(1,3):  #init
            for j in range(3):
                grille[i,j+3]=0
        grille[lig,col]=choix_4_K2[i_cell4]
        
        initjeu()
        
        choix_5_carré2() # test tous les cas et complète la grille si pas d'erreur
# ....................................................
def choix_5_carré2():  # complète la 5e cellule du carré (et les suivantes)
    
    # choix successifs pour 5e cellule du carré K2 en (2,5) l=1,c=4
    # init choix
    lig=1 ; col=4 
    nb_poss=0
    i2=0
    
    for i1 in range(9):
        val=tabpos[lig*9 +col,i1]
        if val>0:
            nb_poss=nb_poss +1
            choix_5_K2[i2]=val
            i2=i2+1
    
    for i_cell5 in range(nb_poss):
        
        grille[lig,col]=choix_5_K2[i_cell5]
        initjeu()
        
        # recherche si erreur
        erreurVU=0 ; erreurPU=0
        
        for i in range(9):
            n_pos_val[i]=0 # init
        
        for val in range(9):
            if tabpos[14,val]>0:
                n_pos_val[val]=n_pos_val[val]+1
        
        for val in range(9):
            if tabpos[21,val]>0:
                n_pos_val[val]=n_pos_val[val]+1
        
        for val in range(9):
            if tabpos[22,val]>0:
                n_pos_val[val]=n_pos_val[val]+1
        
        for val in range(9):
            if tabpos[23,val]>0:
                n_pos_val[val]=n_pos_val[val]+1
        
        # recherche d'erreur pour PU pour les 4 cellules du K2
        # en 2,6
        nbPU_en26=0
        #print ('Possibles Uniques en 2,6 :  ',end='')
        for val in range(9):
            #print("val = ",val,tabpos[14],n_pos_val)
            #print(tabpos[14,val],n_pos_val[val])
            if n_pos_val[val] == 1 and tabpos[14,val]>0:
                #print(int(tabpos[14,val]),end='')
                nbPU_en26=nbPU_en26+1
        #print()#;print("nbPU en 2,6 : ",nbPU_en26)
        if nbPU_en26 >1:
            #print("Erreur : ",nbPU_en26," Possibles uniques en 2,6")
            erreurPU=1
            
        # en 3,4
        nbPU_en34=0
        #print ('Possibles Uniques en 3,4 :  ',end='')
        for val in range(9):
            if n_pos_val[val] == 1 and tabpos[21,val]>0:
                #print(int(tabpos[21,val]),end='')
                nbPU_en34=nbPU_en34+1
        #print()#;print("nbPU en 3,4 : ",nbPU_en34)
        if nbPU_en34 >1:
            #print("Erreur : ",nbPU_en34," Possibles uniques en 3,4")
            erreurPU=1

        # en 3,5
        nbPU_en35=0
        #print ('Possibles Uniques en 3,5 :  ',end='')
        for val in range(9):
            if n_pos_val[val] == 1 and tabpos[22,val]>0:
                #print(int(tabpos[22,val]),end='')
                nbPU_en35=nbPU_en35+1
        #print()#;print("nbPU en 3,5 : ",nbPU_en35)
        if nbPU_en35 >1:
            print("Erreur")
            #print("Erreur : ",nbPU_en35," Possibles uniques en 3,5")
            erreurPU=1
            
        # en 3,6
        nbPU_en36=0
        #print ('Possibles Uniques en 3,6 :  ',end='')
        for val in range(9):
            if n_pos_val[val] == 1 and tabpos[23,val]>0:
                #print(int(tabpos[23,val]),end='')
                nbPU_en36=nbPU_en36+1
        #print();print("nbPU en 3,6 : ",nbPU_en36)
        if nbPU_en36 >1:
            #print("Erreur")
            #print("Erreur : ",nbPU_en36," Possibles uniques en 3,6")
            erreurPU=1
        
        # recherche d'erreur pour VU pour les 4 cellules du K2
        # recherche de valeurs uniques identiques
        
        erreur=0
        n_pos=0 
        for v in range(9):
            if tabpos[14,v]>0:
                n_pos=n_pos+1
                val6=v+1
        if n_pos>1 :            
            
            val6=0
        
        n_pos=0        
        for v in range(9):
            if tabpos[21,v]>0:
                n_pos=n_pos+1
                val7=v+1
        if n_pos==1 :            
            #print("valeur possible en 3,4 : ",val7)
            if val7 == val6:
                erreur=1
        else :
            val7=0
        
        n_pos=0 
        for v in range(9):
            if tabpos[22,v]>0:
                n_pos=n_pos+1
                val8=v+1
        if n_pos==1 :
            #print("valeur possible en 3,5 : ",val8)
            if val8 == val6 or val8 == val7:
                erreur=1
        else :
            val8=0            
        
        n_pos=0 
        for v in range(9):
            if tabpos[23,v]>0:
                n_pos=n_pos+1
                val9=v+1
        if n_pos==1 :
            #print("valeur possible en 3,6 : ",val9)
            if val9 == val6 or val9 == val7 or val9 == val8 :
                erreur=1
        else :
            val9=0
            
        if erreur == 1:            
            erreurVU=1
                
        if erreurVU + erreurPU == 0:  # si pas d'erreur                     
            
            grille[1,5]=0;grille[2,3]=0;grille[2,4]=0;grille[2,5]=0
            initjeu()
            
            #print ("faire suite ....")
            
            choix_6_carré2()
            #n=input()
        
        # fin recherche d'erreur pour ce choix pour cellule 5 du K2  (en 2,5)
        
# .................................................... 
choix_6_K2=np.zeros(3)
def choix_6_carré2():
        
    if grilleVU[1,5]>0:
        grille[1,5]=grilleVU[1,5]
        choix_7_carré2()
        
    elif grillePU[1,5]>0:
        grille[1,5]=grillePU[1,5]
        choix_7_carré2()
    else :
        # choix multiples (plusieurs possibles)
        
        lig=1 ; col=5 
        nb_poss=0
        i2=0
        for i1 in range(9):
            val=tabpos[lig*9 +col,i1]
            if val>0:
                nb_poss=nb_poss +1
                choix_6_K2[i2]=val
                i2=i2+1
        
        for i_cell6 in range(nb_poss):
            
            grille[lig,col]=choix_6_K2[i_cell6]
            
            initjeu()
                        
            choix_7_carré2()
# ....................................................
choix_7_K2=np.zeros(3)
def choix_7_carré2(): # choix 7, 8 et 9
    
    grille[2,3]=0
    initjeu()
    # choix multiples
    lig=2 ; col=3 
    nb_poss=0
    i2=0
    for i1 in range(9):
        val=tabpos[lig*9 +col,i1]
        if val>0:
            nb_poss=nb_poss +1
            choix_7_K2[i2]=val
            i2=i2+1
            
    for i_cell7 in range(nb_poss):
        grille[lig,col]=choix_7_K2[i_cell7]
        initjeu()        
        
        npos=0;v1=0;v2=0
        for i in range(9):
            if tabpos[22,i]>0:
                if v1==0:
                    v1=int(tabpos[22,i])
                else :
                    v2=int(tabpos[22,i])
                
                npos=npos+1
        
        # restent 2 possibilités pour cellules 8 et 9 (v1 et v2)
        grille[2,4]=v1;grille[2,5]=v2  # 1er choix                
        choix_lig4_col1() # suite
        
        grille[2,4]=v2;grille[2,5]=v1  # 2e choix                
        choix_lig4_col1() # suite
        
        grille[2,4]=0;grille[2,5]=0 #init pour suite recherche cellules 7 à 9
        initjeu()
    
# ....................................................
choix_l4_c1=np.zeros(6)
def choix_lig4_col1(): # 1er choix ligne 4 (et suivants)
    
    grille[3,0]=0
    initjeu()
    lig=3 ; col=0
    nb_poss=0
    i2=0
    for i1 in range(9):
        val=tabpos[lig*9 +col,i1]
        if val>0:
            nb_poss=nb_poss +1
            choix_l4_c1[i2]=val
            i2=i2+1
    #print(tabpos[lig*9 +col],nb_poss)
    for i_lig4col1 in range(nb_poss):
        grille[lig,col]=choix_l4_c1[i_lig4col1]
        
        initjeu()
        
        choix_lig4_col2() # 2e choix ligne 4        
        
        grille[3,0]=0 # init pour choix suivant
# ....................................................
choix_l4_c2=np.zeros(6)
def choix_lig4_col2(): # 2e choix ligne 4
    
    grille[3,1]=0
    initjeu()
    lig=3 ; col=1
    nb_poss=0
    i2=0
    for i1 in range(9):
        val=tabpos[lig*9 +col,i1]
        if val>0:
            nb_poss=nb_poss +1
            choix_l4_c2[i2]=val
            i2=i2+1

    for i_lig4col2 in range(nb_poss):
        grille[lig,col]=choix_l4_c2[i_lig4col2]
        
        initjeu()
        
        # faire suite
        choix_lig4_col3()
        grille[3,1]=0 # init pour choix suivant
# ....................................................
choix_l4_c3=np.zeros(6)
def choix_lig4_col3(): # 3e choix ligne 4
    grille[3,2]=0
    initjeu()
    lig=3 ; col=2
    nb_poss=0
    i2=0
    for i1 in range(9):
        val=tabpos[lig*9 +col,i1]
        if val>0:
            nb_poss=nb_poss +1
            choix_l4_c3[i2]=val
            i2=i2+1
    
    for i_lig4col3 in range(nb_poss):
        
        grille[lig,col]=choix_l4_c3[i_lig4col3]
        initjeu()
        
        # faire suite
        choix_lig4_col4()
        
        grille[3,2]=0 # init pour choix suivant
# ....................................................
choix_l4_c4=np.zeros(6)
def choix_lig4_col4(): # 4e choix ligne 4
    
    grille[3,3]=0
    initjeu()
    lig=3 ; col=3
    nb_poss=0
    i2=0
    for i1 in range(9):
        val=tabpos[lig*9 +col,i1]
        if val>0:
            nb_poss=nb_poss +1
            choix_l4_c4[i2]=val
            i2=i2+1
    
    for i_lig4col4 in range(nb_poss):
        
        grille[lig,col]=choix_l4_c4[i_lig4col4]
        
        initjeu()
        #faire suite")
        choix_lig4_col5()
               
        grille[3,3]=0 # init pour choix suivant
    print();print("fin choix_lig4_col4()", indice)
    
# ....................................................
choix_l4_c5=np.zeros(6)
def choix_lig4_col5(): # 5e choix ligne 4
    
    grille[3,4]=0
    initjeu()
    lig=3 ; col=4
    nb_poss=0
    i2=0
    for i1 in range(9):
        val=tabpos[lig*9 +col,i1]
        if val>0:
            nb_poss=nb_poss +1
            choix_l4_c5[i2]=val
            i2=i2+1
    #print("choix_lig4_col5(), possibles : ",tabpos[lig*9 +col])
    for i_lig4col5 in range(nb_poss):
        
        grille[lig,col]=choix_l4_c5[i_lig4col5]
        
        initjeu()
        #print("choix_lig4_col5() : en (4,5) valeur ",int(choix_l4_c5[i_lig4col5]))
        choix_lig4_col6() # suite
        
        grille[3,4]=0 # init pour choix suivant
        
    print();print("fin choix_lig4_col5()", indice)
    
# .................................................... 
choix_l4_c6=np.zeros(6)
def choix_lig4_col6(): # 4e choix ligne 4 en (4,6)
    #print();print("début choix_lig4_col6()",indice)
    grille[3,5]=0
    initjeu()
    #print(grille)
    #print("choix possibles en (4,6) : ",tabpos[3*9 +5])
    lig=3 ; col=5
    nb_poss=0
    i2=0
    for i1 in range(9):
        val=tabpos[lig*9 +col,i1]
        if val>0:
            nb_poss=nb_poss +1
            choix_l4_c6[i2]=val
            i2=i2+1
    
    for i_lig4col6 in range(nb_poss):
        
        grille[lig,col]=choix_l4_c6[i_lig4col6]
        #print("  en (4,6) valeur ",int(choix_l4_c6[i_lig4col6]))
        initjeu()
        
        # faire suite
        choix_1_col7()
        
        grille[3,5]=0 # init pour choix suivant
        print("choix_lig4_col6() ", indice,"avec en (4,6) la valeur :",choix_l4_c6[i_lig4col6])
        
    print();print("fin choix_lig4_col6()", indice)
    
# ....................................................
choix_c7_l1=np.zeros(3)
def choix_1_col7(): # 1er choix colonne 7
    
    grille[0,6]=0
    initjeu()
    lig=0 ; col=6
    nb_poss=0
    i2=0
    for i1 in range(9):
        val=tabpos[lig*9 +col,i1]
        if val>0:
            nb_poss=nb_poss +1
            choix_c7_l1[i2]=val
            i2=i2+1
    
    for i_col7lig1 in range(nb_poss):
        grille[lig,col]=choix_c7_l1[i_col7lig1]
        
        initjeu()
        
        choix_2_col7() # suite
        
        grille[0,6]=0 # init pour choix suivant
    print("fin choix_1_col7() ", indice)
# ....................................................
choix_c7_l2=np.zeros(3)
def choix_2_col7(): # 2e choix colonne 7
    
    #print("choix_1_col7(): # 1er choix colonne 7")
    grille[1,6]=0
    initjeu()
    lig=1 ; col=6
    nb_poss=0
    i2=0
    for i1 in range(9):
        val=tabpos[lig*9 +col,i1]
        if val>0:
            nb_poss=nb_poss +1
            choix_c7_l2[i2]=val
            i2=i2+1
    
    for i_col7lig2 in range(nb_poss):
        grille[lig,col]=choix_c7_l2[i_col7lig2]
                
        initjeu()
        
        choix_3_col7()        
        
        grille[1,6]=0 # init pour choix suivant
    print("   fin choix_2_col7() ", indice)
# ....................................................
choix_c7_l3=np.zeros(3)
def choix_3_col7(): # 3e choix colonne 7
    
    grille[2,6]=0
    initjeu()
    lig=2 ; col=6
    nb_poss=0
    i2=0
    for i1 in range(9):
        val=tabpos[lig*9 +col,i1]
        if val>0:
            nb_poss=nb_poss +1
            choix_c7_l3[i2]=val
            i2=i2+1
    
    for i_col7lig3 in range(nb_poss):
        grille[lig,col]=choix_c7_l3[i_col7lig3]
        
        choix_4_col7()
        
        grille[2,6]=0 # init pour choix suivant
    print("       fin choix_3_col7() ", indice)
# ....................................................
choix_c7_l4=np.zeros(3)

def choix_4_col7(): # 4e choix colonne 7
    
    grille[3,6]=0
    initjeu()
    lig=3 ; col=6
    nb_poss=0
    i2=0
    for i1 in range(9):
        val=tabpos[lig*9 +col,i1]
        if val>0:
            nb_poss=nb_poss +1
            choix_c7_l4[i2]=val
            i2=i2+1
    
    for i_col7lig4 in range(nb_poss):
        
        grille[lig,col]=choix_c7_l4[i_col7lig4]
        initjeu()
        
        choix_7_col7() # suite
        
        grille[3,6]=0 # init pour choix suivant
    print("           fin choix_4_col7() ", indice)
# ....................................................
choix_c7_l7=np.zeros(6)

def choix_7_col7(): # choix colonne 7 ligne 7 - et lignes 8 et 9

    # ligne 4 colonnes 8 et 9 : double double valeurs V1 et V2
    # V1 et V2 sont nécessairement présentes colonne 7 lignes 7, 8 et 9

    #print (tabpos[3 * 9 + 7],tabpos[3 * 9 + 8])
    V1=0;V2=0
    for i in range(9):
        if tabpos[3 * 9 + 7, i] > 0 and V1 == 0:
            V1 = int(tabpos[3 * 9 + 7, i])
        elif tabpos[3 * 9 + 7, i] > 0 and V1 > 0:
            V2 = int(tabpos[3 * 9 + 7, i])
    #print(tabpos[3 * 9 + 7])
    #print(tabpos[3 * 9 + 8])
    #print("V1,V2",V1,V2)
    
    grille[6,6]=0
    initjeu()
    lig=6 ; col=6
    nb_poss=0
    i2=0
    
    for i1 in range(9):
        val=tabpos[lig*9 +col,i1]
        
        if val>0:
            nb_poss=nb_poss +1
            choix_c7_l7[i2]=val
            i2=i2+1
    #print(nb_poss,tabpos[lig*9 +col])
    for i_col7lig7 in range(nb_poss):
        V=choix_c7_l7[i_col7lig7]
        grille[lig,col]=V
        initjeu()
        
        #print(grille);print("lig,col",lig,col,",V1,V2",V1,V2)
        choix_8_col7()        

        grille[6,6]=0
    print("              fin choix_7_col7() ", indice)
# ....................................................
choix_c7_l8=np.zeros(6)

def choix_8_col7(): # choix colonne 7 ligne 8
    
    V1=0;V2=0
    for i in range(9):
        if tabpos[3 * 9 + 7, i] > 0 and V1 == 0:
            V1 = int(tabpos[3 * 9 + 7, i])
        elif tabpos[3 * 9 + 7, i] > 0 and V1 > 0:
            V2 = int(tabpos[3 * 9 + 7, i])
    #print("V1,V2",V1,V2)
    
    grille[7,6]=0
    initjeu()
    lig=7 ; col=6
    nb_poss=0
    i2=0
    for i1 in range(9):
        val=tabpos[lig*9 +col,i1]
        if val>0:
            nb_poss=nb_poss +1
            choix_c7_l8[i2]=val
            i2=i2+1
    #print(nb_poss)
    #print("possibles en (8,7)",tabpos[lig*9 +col])
    #n=input()

    for i_col7lig8 in range(nb_poss):
        
        grille[lig,col]=choix_c7_l8[i_col7lig8]
        initjeu()

        choix_9_col7()
        grille[7,6]=0 # init pour choix suivant       
        
        
        grille[7,6]=0 # init pour choix suivant
# ....................................................
def choix_9_col7(): # choix colonne 7 ligne 9
    MAJdd() #;print(grille);print(grilleVU);print(grillePU);print(grilleD)
    
    if grillePU[8,6]>0:
        #print(".........................")
        grille[8,6]=grillePU[8,6]
        initjeu()
        #print(grille)
        fin_grille_initiale() # recherche d'erreurs, maj compteur indice et affichage
        grille[8,6]=0 # init pour choix suivants
        initjeu()
    else :
        #print("choix multiples")
        #print(grille)
        npos=0
        for i in range(9):
            if tabpos[8*9 +6,i] >0 :
                npos=npos+1
        #print(npos," possibles :",tabpos[8*9 +6])
        #n=input()
        for i in range(9):
            if tabpos[8*9 +6,i]>0:
            
                grille[8,6]=tabpos[8*9 +6,i]
                initjeu()
                #print(grille)
                fin_grille_initiale() # recherche d'erreurs, maj compteur indice et affichage
                grille[8,6]=0 # init pour choix suivant
                initjeu()
        
# ....................................................
def fin_grille_initiale(): # pour afficher et tester (ou non) la grille (ou son indice)

    MAJdd()      # pour apparaître des ereurs (VU en colonne 7 ligne 4)
    #if grilleVU[4,6] > 0:
    #    print("erreur",indice,end=" ") # grille non validée ---> compteur inchangé ex. grilles 1945, 1947...
    #    #n=input()
    #else :
    if grilleVU[4,6] == 0:
        indice[0]=indice[0]+1 # grille initiale validée , sinon choix oublié
    #affiche_grille(grille);print(grilleD)
    #print(indice)
    #if indice[0] % 500 == 0 :  # pas de 500 ici
    
        # affiche selon le pas choisi
            
        #print(indice)
        #affiche_grille(grille)
    if indice[0] == 1 :  
        print("1ère grille initiale :")
        affiche_grille(grille)
        n=input()
        
    # fin de l'écriture de la procédure "générer grille initiale" avec tests multiples

# ....................................................    
def choix_aléatoire(lig,col):
    choi=0
    
    while choi==0:
        val=random.randint(1, 9)
                
        if tabpos[lig*9 +col,val-1]>0: # val doit être possible
            choi=1
    
        if grilleVU[lig,col]==val or grillePU[lig,col]==val:
            grille[lig,col]=val
        
        if grilleVU[lig,col]==0 and grillePU[lig,col]==0:
            #test si possible à placer dans la ligne lig
            nbvl=0
            for c in range(9):
                if grille[lig,c]==val:
                    nbvl=nbvl+1
            #test si possible à placer dans la colonne col
            nbvc=0            
            for l in range(9):
                if grille[l,col]==val:
                    nbvc=nbvc+1
            #test si possible à placer dans le carré (lig,col)
            nbvk=0       
            l1 = lig - lig%3
            c1 = col - col%3             
            for i in range(3) :
                for j in range(3) :
                    if grille[l1+i,c1+j]==val:
                        nbvk=nbvk+1
                  
            if nbvl+nbvc+nbvk==0 :
                if grille[lig,col]==0 :
                    grille[lig,col]=val
                    #print(grille)
                
                    initjeu()                
                
                    solution3(-1) # complète la grille
                    
                    for l in range(9):   
                        for c in range(9):
                            grille[l,c]=grillesol[l,c]
                
                    initjeu()
                    
        
        

# ..................................................
def nouvelle_grille(): # à partir d'une grille complète ou non
    numpb[0]=0
    # init
    mixer_valeurs() # nouvelle grille de départ
    nbsolniv4[0]=0
    
    solution(-1) # permet de commencer avec la grille solution sans l'afficher
    nivrep=1 # def
    print("pour diminuer ensuite le nombre de valeur utiliser 'lister valeur à enlever'")
    print("1 -> 33 val 2 -> 30 val  3 -> niv 3    4 ->  27 val   5 -> jouer des doubles")
    print("1 =  facile 2 =   moyen  3 = difficile 4 =  difficile 5  =  expert ",end="")
    
    niv=int(input("?  "))
    # enlève des valeurs jusqu'à nb
    if niv==1 :
        nb=33
        print("facile   ",end="")
    elif niv==2 :
        nb=30
        print("moyen    ",end="")
    elif niv==4 or niv ==3:
        nb=27
        
        
    elif niv==5 :
        nb=30
        print("expert    niveau de résolution 4  (jouer des doubles) ")

    for i in range(9):   # init
        for j in range(9):
            grille[i,j]=grillesol[i,j]
    ct=81
    
    while ct>nb:
        for l in range(9):   
            for c in range(9):
                grilleinit[l,c]=grille[l,c] # restitution
        
        val=0
        while val==0 :
            lig=random.randint(0, 8)
            col=random.randint(0, 8)
            val=grille[lig,col]

        grille[lig,col]=0
        ct=0
        for l in range(9):   
            for c in range(9):
                grillesauv[l,c]=grille[l,c] # sauvegarde avant sol
                if grille[l,c]>0:
                    ct=ct+1
        
        # La grille a-t-elle une solution ?
        
        initjeu()
        
        solution123(-1)  # solution (ou non) sans jouer un double (niv 1 à 3)
       
        ctsol=0;ct=0
        for l in range(9):
            for c in range(9):
                if grillesol[l,c]>0:
                    ctsol=ctsol+1
                if grille[l,c]>0:
                    ct=ct+1
        print(end=".")
        if nivsol[0]==0 and niv < 5:
            grille[lig,col]=val
            ct= ct+1
        if nivsol[0]==0 and niv ==5 : # pour trouver des pb niv 4
            initjeu()
            solution(-1)
            print(ct,nbsolniv4[0],end="")
            if nbsolniv4[0]==1:  # tester ici le nombre de solutions (1, 2 ou plus ?)
                ct=nb
            else :
                grille[lig,col]=val
            ct= ct+1
        
        if ct==nb and niv ==3:  # niveau 3
            if nivsol[0]!=3:
                print (nivsol[0])
                for i in range(9):   # init   recommencer
                    for j in range(9):
                        grille[i,j]=grillesol[i,j]
                ct=81
        if nivsol[0]==3 and niv == 3: # niveau 3 suite
            ct=nb  # arrêt
            
        if ct==nb and niv ==5:  # niveau 4
            if nbsolniv4[0]!=1:
                for i in range(9):   # init   recommencer
                    for j in range(9):
                        grille[i,j]=grillesol[i,j]
                ct=81
        if nbsolniv4[0]==1 and niv ==5:  # niveau 4
            ct=nb   
# ..................................................     
def jouer(ch) :
    
    n = int(ch)
    lig = n // 100 
    col = (n- lig * 100) // 10
    val = (n- lig * 100) % 10
    l=lig-1
    c=col-1
    
    s=0 # si s>0 il y a des possibles uniques par cellules pour niveau 3
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
        print()
        print("recherche des possibles à partir de doubles-doubles")
        MAJdd();MAJdd()   # niveau 3
        s=0 # si s>0 il y a des possibles uniques par cellules
        for lig in range(9):   
            for col in range(9):
                s=s+grilleVU[lig,col]+grillePU[lig,col]
        if s==0:
            print() # niveau 4
            print("vous devez jouer un double")
            print("vous pouvez sauvegarder la grille à ce niveau")
            affichegrilledouble(grilleD)
        
    if grilleVU[l,c] == val :     # niveau 1 2 et 3
        grille[l,c] = val
    if grillePU[l,c] == val :     # niveau 2 et 3
        grille[l,c] = val
    
    s=0 # si s>0 il y a des possibles uniques par cellules
    for lig in range(9):   
        for col in range(9):
            s=s+grilleVU[lig,col]+grillePU[lig,col]
    initjeu()
    MAJdoubles()
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
# ..................................................# initialisation de la grille de valeurs uniques possibles par cellule
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
nivsol=[0]
# ..................................................
def solution(sol):
    nivsol[0]=0
    #print()
    solution1(sol) # solution niveau 1
    ctsol=0
    for l in range(9):   
        for c in range(9):
            if grillesol[l,c]>0:
                ctsol=ctsol+1
    if ctsol == 81 :
        nivsol[0]=1
    else :
        solution2(sol)  # solution niveau 2
        ctsol=0
        for l in range(9):   
            for c in range(9):
                if grillesol[l,c]>0:
                    ctsol=ctsol+1
        if ctsol == 81 :
            nivsol[0]=2
        else :
            solution3(sol)  # solution niveau 3
            ctsol=0
            for l in range(9):   
                for c in range(9):
                    if grillesol[l,c]>0:
                        ctsol=ctsol+1
            if ctsol == 81 :
                nivsol[0]=3
            else :
                solution4(sol)  # solution niveau 4
                ctsol=0
                for l in range(9):   
                    for c in range(9):
                        if grillesol[l,c]>0:
                            ctsol=ctsol+1
                if ctsol == 81 :
                    nivsol[0]=4
   
    ctsol=0
    for l in range(9):   
        for c in range(9):
            if grillesol[l,c]>0:
                ctsol=ctsol+1
    
# ..................................................
def solution123(sol): # pour lister valeurs à enlever (sans niv 4)
    nivsol[0]=0
    
    solution1(sol) # solution niveau 1
    ctsol=0
    for l in range(9):   
        for c in range(9):
            if grillesol[l,c]>0:
                ctsol=ctsol+1
    
    if ctsol == 81 :
        nivsol[0]=1
    else :
        solution2(sol)  # solution niveau 2
        ctsol=0
        for l in range(9):   
            for c in range(9):
                if grillesol[l,c]>0:
                    ctsol=ctsol+1
        if ctsol == 81 :
            nivsol[0]=2
        else :
            solution3(sol)  # solution niveau 3
            ctsol=0
            for l in range(9):   
                for c in range(9):
                    if grillesol[l,c]>0:
                        ctsol=ctsol+1
            if ctsol == 81 :
                nivsol[0]=3

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
def ajouter_valeurs() :
    # modif
    initjeu()
    MAJdoubles()
    #affichegrilledouble(grilleD)
    
    for l in range(9):   
        for c in range(9):
            grillesauv[l,c]=grille[l,c]
    #print("recherche de la solution")
    #solution(-1)    
    #for l in range(9):   
    #    for c in range(9):
    #        grille[l,c]=grillesauv[l,c]
    lc=0
    while int(lc) < 11 or int(lc) > 99 :
        print("ajouter une valeur (de la solution) :")
        lc=input("saisir un nombre de 2 chiffres (lc) -->  ")
        if lc<"0" or lc>"9":  #   lc doit être un nombre
            lc=0
    
    n = int(lc)
    lig = n // 10 
    col = (n- lig * 10) % 10
    l=lig-1
    c=col-1

    print (tabpos[l*9+c])
    v=input("valeur ? ")
    grille[l,c]=v
    initjeu()
    for l in range(9):   
            for c in range(9):
                grillesauv[l,c]=grille[l,c]
    solution123(1)
    #affiche_grille(grillesol)
    for l in range(9):   
        for c in range(9):
            grille[l,c]=grillesol[l,c]
    initjeu()
    
    
# ..................................................
def lister_valàenlever():  # sans changer de niveau de résolution
    nivsol[0]=0
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
                #print(l+1,c+1,int(v),end="  ")
                grille[l,c]=0
                initjeu()
                for lig in range(9):   
                    for col in range(9):
                        grillesauv[lig,col]=grille[lig,col]
                solution123(-1)
                
                if grillesol[l,c]>0 and nivsol[0]==0:  # si la valeur enlevée se retrouve dans la solution niv 1 2 3
                    solution4(-1)
                ct=0
                for lig in range(9):   
                    for col in range(9):
                        if grillesol[lig,col]>0 :
                            ct=ct+1
                
                if ct==81:
                    print("ligne",l+1,"colonne",c+1,"on peut enlever ",int(v),"  (solution de niveau ",nivsol[0],")")
                    
                for lig in range(9):   
                    for col in range(9):
                        grille[l,c]=grilleinit[l,c]
                        grillesol[l,c]=0
                        grillesauv[l,c]=0
                initjeu()
# ..................................................
def enlever() :
    lc=""
    while lc < "11" or lc > "99" :
        print("enlever une valeur :")
        lc=input("saisir un nombre de 2 chiffres (lc) -->  ")
        
    
    n = int(lc)
    lig = n // 10 
    col = (n- lig * 10) % 10
    l=lig-1
    c=col-1
    
    grille[l,c]=0
    initjeu()    
# ..................................................
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
# ..................................................
# initialisation de la grille des doubles-doubles
grilleDD=np.zeros((9,9))
grilleD=np.zeros((9,9))

# ..................................................
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
# ..................................................
def affichegrilledouble(grille):
    print ("┌——————————┬——————————┬——————————┐")
    for l in range(9) :
        print ("│ ",end="")
        for c in range(9):
            if grille[l,c]>0 :
                n=int(grille[l,c])
                print (n,end=" ")
                
            else :
                print("  ",end=" ")  # n'affiche pas les 0
            if c==2 or c==5:
                print("│",end=" ")
        print ("│")
        if l==2 or l==5 :
            print ("├——————————┼——————————┼——————————┤")
    print ("└——————————┴——————————┴——————————┘")

# ..................................................
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
def solution4(sol):  # appelée si sol1 , 2 et 3 ont échoué
    nbsolniv4[0]=0  # init nb de sol
    nivsol[0]=4   # init niveau de solution
    
            
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

choixval1=np.zeros(80) # mémorise les 1ères valeurs
choixval2=np.zeros(80) # mémorise les 2èmes valeurs
choixval_index=np.zeros(80) # mémorises l'index de choix entre 2 valeurs
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
            print("     pas de solution ")               
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
            #if sol == -1:
            #    print(nbsolniv4[0],end=" ")
            #solniv[1]=4 # solution de niveau 4

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
    grillinitial()
    rd();rd()
    
def grillinitial():
    for l in range(9):
        for c in range(9):
            grille[l,c]=grilleinit[l,c]

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
import turtle as turtle # pour afficher le jeu avec turtle

from turtle import *  # pour importer les fonctions du module turtle
   
num_ligne=[0]
num_ligne[0]=5
num_colonne=[0]
num_colonne[0]=5
num_valeur=[0]
# ..................................................
penduindice=[0]
def choixpendu():
    
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
def  pendu1() : # soleil
    up();goto(-70,200);color("yellow")  
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
# ..................................................  
def  dessiner_grille() : # et remplir la grille avec Turtle
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
def remplir_grille_sudo(): # remplir la grille
    color("black")
    ct=0 
    for lig in range (0,9):
        for col in range (0,9):
            if grille[lig][col]!=0:
                ct=ct+1  
                #x=35*(col-3)+2;y=35*(4-lig)
                x=(col-3)*35 - 5 ; y = (4 - lig)*35
                up()
                color("black")
                goto(x,y)          
                write(int(grille[lig,col]), font=("Arial", 18))
        
    # messages
    up();goto (-200,200);color("red")
    write('Sudoku',font=("Arial", 16, "normal"),align="center")
    up();goto (-200,180);color("black")
    write('pb '+str(numpb[0]),font=("Arial", 10, "normal"),align="center")
    # numpb[0]=numérogrille
    up();goto (25,-170);color("black")    
    write(str(ct)+' / 81 ',font=("Arial", 8, 'normal', 'bold', 'italic', 'underline'))
    goto (0,-260);color("red")
    write("+  :  pour ajouter une valeur de la solution",font=("Arial", 8, "normal"),align="center")
    color("black")
    goto(0,-240)
    write('&  :  pour nouvelle grille en mixant les valeurs                              /  :  pour quitter           ',align="center")
    goto (0,-220)
    write('$  :  pour afficher la solution (fenêtre Python Shell)             ?  :  pour afficher ou non les aides',align="center")
    num_colonne[0]=5;num_ligne[0]=5
    up;goto(35*(num_colonne[0]-4)+2,35*(5-num_ligne[0])) # retour du pointeur en (5,5)
    
    color("red")

def k1():  # up
    if num_ligne[0]>1:
        num_ligne[0]=num_ligne[0]-1
        up()
        goto(35*(num_colonne[0]-4)+2,35*(5-num_ligne[0]))
        down()
    up()
def k2():  # down
    if num_ligne[0]<9:
        num_ligne[0]=num_ligne[0]+1
        up()
        goto(35*(num_colonne[0]-4)+2,35*(5-num_ligne[0]))
        down()
    up()
def k3(): # left
    if num_colonne[0]>1:
        num_colonne[0]=num_colonne[0]-1
        up()
        goto(35*(num_colonne[0]-4)+2,35*(5-num_ligne[0]))
        down()
    up()
def k4():  # right
    if num_colonne[0]<9:
        num_colonne[0]=num_colonne[0]+1
        up()
        goto(35*(num_colonne[0]-4)+2,35*(5-num_ligne[0]))
        down()
    up()
def valide_lcv():
    c=num_colonne[0]
    l=num_ligne[0]
    v=num_valeur[0]

    ch=str(l*100+c*10+v)
    jouer(ch)
    if grille[l-1,c-1]!=v : # si non validé
        penduindice[0]=penduindice[0]+1
        choixpendu()
        color("red");up();goto(35,0)
    if grille[l-1,c-1]==v : #si validé par le programme
        # complète la grille : v en (l,c)
        x=35*(c-4)-3;y=35*(5-l) # position du caractère à écrire
        up(); goto(x,y);color("blue")
    
        write(int(grille[l-1,c-1]),font=("Arial", 18)) # écrit la valeur validée
    affich_compteur()
    for i in range(40):
        print() # efface écran Shell
    
def affich_compteur():
    ct=0  # maj du compteur affiché
    for l in range(9):
        for c in range(9):
            if grille[l,c]>0:
                ct=ct+1
    
    up();goto (25,-165);color("white") # pour effacer le compteur
    turtle.pensize(20)
    down(); goto (70,-165)
    
    up();goto (25,-170);color("black")    
    write(str(ct)+' / 81 ',font=("Arial", 8, 'normal', 'bold', 'italic', 'underline'))
    
    color("red") # couleur du pointeur
    goto(35*(num_colonne[0]-4)+6,35*(5-num_ligne[0])) # replacer le pointeur

def k10():  #   + ajouter une valeur de la solution
    if jeumot[0]==0:
        penduindice[0]=penduindice[0]+1
        choixpendu()
        color("red");up();goto(35,0)
        suite_k10()
def suite_k10():
    col=num_colonne[0]-1 ; lig=num_ligne[0]-1
    if grillesol[lig,col]==0:  # si solution n'ont encore recherchée
        for l in range(9):   
            for c in range(9):
                grillesauv[l,c]=grille[l,c]
        solution(-1)    # solution non affichée
    v=grillesol[lig,col]
    if grille[lig,col]==0:
        grille[lig,col]=v
        grilleVU[lig,col]=0
        
        x=35*(col-3)+2;y=35*(4-lig) # position du pointeur pour écrire
        color("red")
        goto(x-5,y)          
        write(int(grille[lig,col]), font=("Arial", 18))
        affich_compteur()  
    initjeu()
    
def k11():
    if jeumot[0]==0:
        suite_k11()
def suite_k11():
    num_valeur[0]=1
    valide_lcv()
        
def k12():
    if jeumot[0]==0:
        suite_k12()
def suite_k12():
    num_valeur[0]=2
    valide_lcv()
    
def k13():
    if jeumot[0]==0:
        suite_k13()
def suite_k13():
    num_valeur[0]=3
    valide_lcv()
    
def k14():
    if jeumot[0]==0:
        suite_k14()
def suite_k14():
    num_valeur[0]=4
    valide_lcv()
    
def k15():
    if jeumot[0]==0:
        suite_k15()
def suite_k15():
    num_valeur[0]=5
    valide_lcv()
    
def k16():
    if jeumot[0]==0:
        suite_k16()     
def suite_k16():
    num_valeur[0]=6
    valide_lcv()
        
def k17():
    if jeumot[0]==0:
        suite_k17()
def suite_k17():
    num_valeur[0]=7
    valide_lcv()
    
def k18():
    if jeumot[0]==0:
        suite_k18()
def suite_k18():
    num_valeur[0]=8
    valide_lcv()
    
def k19():
    if jeumot[0]==0:
        suite_k19()
def suite_k19():
    num_valeur[0]=9
    valide_lcv()

def k20():
    if jeumot[0]==0:
        penduindice[0]=penduindice[0]+1
        choixpendu()
        color("red");up();goto(35,0)
        suite_k20()
def suite_k20():
    initjeu()
    print()
    affiche_grille(grilleVU)
    print("valeurs uniques par cellules")
    affiche_grille(grillePU)
    print("possibles uniques par zones de 9 cellules")
    s=0 # si s>0 il y a des possibles uniques par cellules
    for l in range(9):   
        for c in range(9):
            s=s+grilleVU[l,c]+grillePU[l,c]
    if s==0:
        print()
        print("recherche des possibles à partir de doubles-doubles")
        
        MAJdd();MAJdd()
        affiche_grille(grilleVU)
        print("valeurs uniques par cellules")
        affiche_grille(grillePU)
        print("possibles uniques par zones de 9 cellules")
        s=0 # si s>0 il y a des possibles uniques par cellules
        for l in range(9):   
            for c in range(9):
                s=s+grilleVU[l,c]+grillePU[l,c]
        if s==0:
            print()
            print("vous devez jouer un double")
            affichegrilledouble(grilleD)
    
def k21():
    exit()

def k25():
    if jeumot[0]==0:
        penduindice[0]=penduindice[0]+1
        choixpendu()
        color("red");up();goto(35,0)
        suite_k25()
def suite_k25():
    print()
    for l in range(9):   
        for c in range(9):
            grillesauv[l,c]=grille[l,c]
    solution(+1)  # solution affichée
            
def k26():
    if jeumot[0]==0:
        suite_k26()
def suite_k26():
    mixer_valeurs()        
    #remplir_grille_sudo()
    color("black")
    ct=0 
    for lig in range (0,9):
        for col in range (0,9):
            x=35*(col-3)-3;y=35*(4-lig)
            up()
            goto(x+5,y+15)
            down()
            color("white")
            turtle.pensize(28)  # couleur de la ligne
            goto (x+5,y+15)
            if grille[lig][col]!=0:
                up()
                color("black")
                goto(x,y)          
                write(int(grille[lig,col]), font=("Arial", 18))
    up();goto(35*(num_colonne[0]-4)+2,35*(5-num_ligne[0])) # retour du pointeur en (5,5)
    color("red")
    # annule solution
    for lig in range (0,9):
        for col in range (0,9):
            grillesol[lig,col]=0

def k31():
    letr='a'
    if jeumot[0] == 1:
        valid_lettr(letr)
def k32():
    letr='b'
    if jeumot[0] == 1:
        valid_lettr(letr)
def k33():
    letr='c'
    if jeumot[0] == 1:
        valid_lettr(letr)
def k34():
    letr='d'
    if jeumot[0] == 1:
        valid_lettr(letr)
def k35():
    letr='e'
    if jeumot[0] == 1:
        valid_lettr(letr)
def k36():
    letr='f'
    if jeumot[0] == 1:
        valid_lettr(letr)
def k37():
    letr='g'
    if jeumot[0] == 1:
        valid_lettr(letr)
def k38():
    letr='h'
    if jeumot[0] == 1:
        valid_lettr(letr)
def k39():
    letr='i'
    if jeumot[0] == 1:
        valid_lettr(letr)
def k40():
    letr='j'
    if jeumot[0] == 1:
        valid_lettr(letr)
def k41():
    letr='k'
    if jeumot[0] == 1:
        valid_lettr(letr)
def k42():
    letr='l'
    if jeumot[0] == 1:
        valid_lettr(letr)
def k43():
    letr='m'
    if jeumot[0] == 1:
        valid_lettr(letr)
def k44():
    letr='n'
    if jeumot[0] == 1:
        valid_lettr(letr)
def k45():
    letr='o'
    if jeumot[0] == 1:
        valid_lettr(letr)
def k46():
    letr='p'
    if jeumot[0] == 1:
        valid_lettr(letr)
def k47():
    letr='q'
    if jeumot[0] == 1:
        valid_lettr(letr)
def k48():
    letr='r'
    if jeumot[0] == 1:
        valid_lettr(letr)
def k49():
    letr='s'
    if jeumot[0] == 1:
        valid_lettr(letr)
def k50():
    letr='t'
    if jeumot[0] == 1:
        valid_lettr(letr)
def k51():
    letr='u'
    if jeumot[0] == 1:
        valid_lettr(letr)
def k52():
    letr='v'
    if jeumot[0] == 1:
        valid_lettr(letr)
def k53():
    letr='w'
    if jeumot[0] == 1:
        valid_lettr(letr)
def k54():
    letr='x'
    if jeumot[0] == 1:
        valid_lettr(letr)
def k55():
    letr='y'
    if jeumot[0] == 1:
        valid_lettr(letr)
def k56():
    letr='z'
    if jeumot[0] == 1:
        valid_lettr(letr)

# ..................................................

def sudo() :
    tracer(0)
    dessiner_grille()
    remplir_grille_sudo()
    left(90) # pointe vers le haut
    color("red")
    
    turtle.onscreenclick(get_mouse_click_coor)

    wn.listen() # en mode 'tortue' le programme écoute et suit les instructions

def get_mouse_click_coor(x, y):
    tracer(1)
    color("red") # couleur du pointeur
    goto(x,y) # replacer le pointeur
    up()
    num_colonne[0]=int((x+10)//35 +4)
    num_ligne[0]=int(5-y//35)
    
    if num_ligne[0]>9 or num_colonne[0]>9:
        num_ligne[0]=5;num_colonne[0]=5
        up();goto(35,0)
    if num_ligne[0]<1 or num_colonne[0]<1:
        num_ligne[0]=5;num_colonne[0]=5
        up();goto(35,0)

# ..................................................       
#continuer() # accès programme complet sans graphics turtle
# ..................................................
jeumot=[0]
# commandes du programme en mode tortue
wn = turtle.Screen()  # commande nécessaire pour utiliser onkey

wn.onkey(k1, "Up")
wn.onkey(k2, "Down")
wn.onkey(k3, "Left")
wn.onkey(k4, "Right")

wn.onkey(k10, "+")
wn.onkey(k11, "1")
wn.onkey(k12, "2")
wn.onkey(k13, "3")
wn.onkey(k14, "4")
wn.onkey(k15, "5")
wn.onkey(k16, "6")
wn.onkey(k17, "7")
wn.onkey(k18, "8")
wn.onkey(k19, "9")

wn.onkey(k20, "?") # aides
wn.onkey(k21, "/") # quitter

wn.onkey(k25, "$") # solution
wn.onkey(k26, "&") # mixer

# commandes pour mot-carré
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
motcaré=[0,0,0,0,0,0,0,0,0]
def mots_carrés():   # avec turtle
    
    #motcarré=''    
    définition=''
    with open("mots_carrés"+".txt","r") as filin :
        listemotscarrés=filin.read()
        
        nblettres=len(listemotscarrés)
        nbmots=0
        for i in range(nblettres):
            if listemotscarrés[i]== '\n' :
                nbmots=nbmots+1
        indicemot=random.randint(1, nbmots)
        
    i=1
    k=0
    while i<indicemot:
        if listemotscarrés[k]=='\n' :
            i=i+1
        k=k+1
        
    for j in range(9):
        motcaré[j]=listemotscarrés[j+k]
    j=j+1
    while listemotscarrés[j+k]!= '\n' :
        définition=définition+listemotscarrés[j+k]
        j=j+1

    # charger une grille
    RAZposs()
    listepb()
    rep="non"
    while rep=="non":
        num=input("charger problème numéro ? : ")
        nom="pb"+num+".txt"
        if nom in os.listdir():
            rep="oui"
           
    with open(nom,"r") as filin :
        vals=filin.read() # 9 lignes de 9 caractères
        ct=0
        for l in range(9):
            for c in range(9):
                v=vals[l*9 + c+l] # on saute 1 caractère en fin de ligne
                grille[l,c]=int(v)
                if grille[l,c]>0 :
                    ct=ct+1
    mixer_valeurs()
    initjeu()  # initialisation du jeu
    
    for l in range(9):
        for c in range(9):
            grillesauv[l,c]=grille[l,c] # mémorise la grille
    solution(-1)  # trouve la solution
    for l in range(9):
        for c in range(9):
            grille[l,c]=grillesauv[l,c] # restitue la grille
    for i in range(40):
        print()  # efface la grille de chiffres fenêtre Shell
       
    #choix de lignemot    
    ctmini=9
    for l in range(9):
        ct=0
        for c in range(9):
            if grille[l,c]>0:
                ct =ct+1
        if ct<=ctmini :
            ctmini=ct
            lignemot=l
        
    for c in range(9):
        valeur=int(grillesol[lignemot,c])
        valeur_lettre[c]=valeur
    
    # affiche messages fenêtre tortue
    tracer(0)
    up();goto (-200,200);color("red")
    write('Jeu-mot',font=("Arial", 16, "normal"),align="center")
    x=35*(-3);y=35*(4-lignemot)+15
    goto(x,y)
    down()
    color("yellow");pensize(27)  # couleur et taille de la ligne à trouver
    goto (x+282,y)
    up()
    x=35*(-7)-5;y=35*(4-lignemot)
    goto(x,y)
    color("red")
    write("mot à trouver : ", font=("Arial", 12))
    up()
    
    goto(-60,-200)
    color("blue")
    write(définition, font=("Arial", 10))
    up()    
    goto(180,-230)
    color("black")
    write('/  pour quitter', font=("Arial", 8))

    #affiche_grille_motcarré
    tracer(0)
    dessiner_grille()
    
    # compléter la grille
    color("black")
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
                    while valeur_lettre[ind] != v:
                        ind=ind+1                  
                        ind=ind%9 # sinon parfois erreur
                    up()
                    x=35*(c-3)-4;y=35*(4-l)
                    goto(x,y)          
                    write(motcaré[ind], font=("Arial", 18))
        ct=81
    # jouer avec tortue
    left(90) # pointe vers le haut
    up();goto(35,0) # position initiale du pointeur
    onscreenclick(get_mouse_click_coor)
    color("red")
    wn.listen() # en mode 'tortue' le programme écoute et suit les instructions

# ......
def valid_lettr(letr):
    l=num_ligne[0]-1;c=num_colonne[0]-1  # de 0 à 8      
    v=int(grillesol[l,c])
    
    ind=0
    while valeur_lettre[ind] != v:
        ind=ind+1
       
    letrsol=motcaré[ind]  # lettre à touver len l,c
           
    if ord(letr) == ord(letrsol)+32 :  # si le choix est bon
        grille[l,c]=grillesol[l,c]
        #print("en ",l+1,c+1," ",letrsol)
        up()
        x=35*(c-3)-5;y=35*(4-l) # position du curseur d'écriture
        goto(x,y)          
        color("blue");write (letrsol, font=("Arial", 18))
        color("red");up();goto(x+6,y)
# ..................................................
# programme sans turtle graphics

turtle.bye()
continuer()

# ..................................................
# programme avec turtle graphics
for i in range(40):
    print()
print("│   jouer avec la tortue")
print("│        c  : pour charger une grille sudoku")
print("│        m  : pour jouer à mot-carré")
print("│ ")
print("│    ou ")
print("│      apc  : accès programme complet niveau 1")
print()
commnand=0
while commnand==0 :
       
    jeumot[0] = 0 # faux
    ch=input("commande : ")
    tracer(0)
    if ch == 'c' :
        commnand=1
        charger()   # nouvelle grille
        sudo()
    elif ch == 'apc' :
        commnand=1
        continuer() # accès programme complet
    elif ch == 'm' :
        jeumot[0] = 1 # vrai
        commnand=1
        mots_carrés() # jouer avec la tortue
# ..................................................
