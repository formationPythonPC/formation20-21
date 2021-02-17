import matplotlib.pyplot as plt
import numpy as np

########################
# extraction des donnees
########################
file = np.loadtxt("donnees-planetes.csv", skiprows=4, delimiter=";")
X_M = file[ : ,0]
Y_M = file[ : ,1]
X_V = file[ : ,2]
Y_V = file[ : ,3]

###########
# le Soleil
###########
plt.scatter(0,0, marker = "*", s = 800, color = "orange", label = "Soleil")
plt.text(0.05,0, "Soleil",color="orange",fontsize=10)

#############################
# initialisation des planetes
#############################
XM, YM, XV, YV = [],[],[],[]
courbeM, = plt.plot(XM,YM,'b.', markersize=8,label = "positions de Mercure")
courbeV, = plt.plot(XV,YV,'r.', markersize=20,label = "positions de Venus")

##################################
# limites du graphe, noms des axes
##################################
plt.xlim(-0.8, 0.8)
plt.ylim(-0.8,0.8)
plt.xlabel("distance au soleil en unités astronomiques (1 u.a. = $1,5\\times 10^{11}$ m)")
plt.ylabel("distance au soleil en unités astronomiques (1 u.a. = $1,5\\times 10^{11}$ m)")

##########
# légendes
##########
plt.text(-0.75,0.7,"mouvement de Mercure", color="blue")
plt.text(-0.75,0.65,"mouvement de Venus", color="red")

###########################
# mouvement avec effacement
###########################
"""
for i in range(len(X_M)) :
    if i%5 == 0 :
        courbeM.set_data(X_M[i],Y_M[i])
        courbeV.set_data(X_V[i],Y_V[i])
        plt.pause(1e-10)

plt.title("Mouvements de Mercure et Venus")
plt.legend()
plt.show()
"""
###########################
# mouvement sans effacement
###########################

for i in range(len(X_M)) :
    if i%5 == 0 :
        XM.append(X_M[i]);YM.append(Y_M[i]);XV.append(X_V[i]);YV.append(Y_V[i])
        courbeM.set_data(XM,YM)
        courbeV.set_data(XV,YV)
        plt.pause(1e-10)

plt.title("Mouvements de Mercure et Venus")
plt.legend()
plt.show()












