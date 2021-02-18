import matplotlib.pyplot as plt
import numpy as np

file = np.loadtxt("donnees-basket2.csv", skiprows=3, delimiter=";")
T = file[ : ,0];X = file[ : ,1];Y = file[ : ,2]

# les listes associées au mouvement sont X (abscisses), Y (ordonnées), T(dates de chaque point)

# points de la trajectoire
# A COMPLETER

# un label (indice des listes) pour tous ces points
for i in range(len(X)) :
    if i < 7 :
        plt.text(X[i]-0.05, Y[i]-0.05, "{}".format(i))
    elif i > 7 :
        plt.text(X[i]+0.05, Y[i]-0.05, "{}".format(i))
    else :
        plt.text(X[i], Y[i]-0.05, "{}".format(i))



# temps entre deux points de la trajectoire
delta_t = 0.08

# vecteur vitesse au premier point de la trajectoire
# A COMPLETER : plt.quiver(........)

# vecteurs vitesse pour tous les points
for i in range(len(T)-1) :
    # A COMPLETER : plt.quiver(.........)





plt.xlabel("abscisses (en mètres)")
plt.ylabel("ordonnées (en mètres)")
plt.title("Un lancer franc réussi")
plt.legend(title = "$\\Delta t = ${} s.".format(delta_t))
plt.show()
