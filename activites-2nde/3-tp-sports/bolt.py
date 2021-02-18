# coding: utf8
import matplotlib.pyplot as plt
import numpy as np

##################
# listes X, Y et T
##################
delta_t = 1.5
T = [0, 1.5, 3.0, 4.5, 6.0, 7.5, 9.0, " "]
X = [0, 7.94, 21.33, 38.37, 56.46, 74.88, 93.01, 111.08]
Y = [0,0,0,0,0,0,0,0]

##########################################
# création des éléments généraux du graphe
##########################################
graphe=plt.gca(facecolor='b')
plt.title("Positions successives d'Usain Bolt (2009 -- Berlin), record du monde 100 m : 9,58 secondes", fontsize=18)
plt.xlabel("Distance parcourue (en mètres)", fontsize=15)
plt.yticks([], [])# pas de graduation ni d'étiquette sur Oy
graphe.xaxis.set_ticks(X)# les graduations sur Ox
graphe.xaxis.set_ticklabels([str(i) for i in X],fontsize=11,horizontalalignment='left')# les étiquettes sur Ox (qui doit être une liste de strings)
plt.xlim(min(X)-10,max(X)+10)

# lignes blanches
plt.plot([-10,130],[0.015,0.015],"w--",lw=3)
plt.plot([-10,130],[-0.015,-0.015],"w--",lw=3)

# départ
plt.plot([0,0],[-0.05,0.05],"w.-", lw=1)
plt.text(0,0.04,"DEPART", horizontalalignment='center', fontsize=13,color="orange")
# arrivée
plt.plot([100,100],[-0.05,0.05],"w.-", lw=1)
plt.text(100,0.04,"ARRIVEE", horizontalalignment='center', fontsize=13,color="orange")
# notation des indices
plt.text(-5,-0.007,"indice : ",fontsize=10,color="w",horizontalalignment='center')

##################################
# initialisation de la trajectoire
##################################
# représentation de la trajectoire
plt.plot(X,Y,"ro--", ms=10)

# un texte pour les dates et pour les indices
for i in range(len(X)) :
    if T[i] != 0 :
        plt.text(X[i],0.01,"{} s".format(T[i]),fontsize=13,color="w",horizontalalignment='center')
        plt.text(X[i],-0.007,"{}".format(i),fontsize=10,color="w",horizontalalignment='center')
    else :
        plt.text(X[i],-0.01,"{} s".format(T[i]),fontsize=13,color="w",horizontalalignment='center')
        plt.text(X[i],-0.007,"{}".format(i),fontsize=10,color="w",horizontalalignment='center')

##################################################
# question 3 : calcul de la vitesse au 6ème point
##################################################
#vx = # À COMPLÉTER




#####################################################
# question 4 : affichage de la vitesse au 6ème point
#####################################################
# À COMPLÉTER

##############################################
# question 5 : flèche de la vitesse au 6ème point
##############################################
#x = # À COMPLÉTER
#y = # À COMPLÉTER
#vx = # À COMPLÉTER
#vy = # À COMPLÉTER

# décommentez la ligne suivante puis compilez pour voir le résultat
#plt.quiver(x,y, vx, vy, color = "orange", angles='xy', scale_units='xy', scale=1)



#########################################
# enregistrement comme image et affichage
#########################################
plt.savefig("record2.png")
plt.show()



