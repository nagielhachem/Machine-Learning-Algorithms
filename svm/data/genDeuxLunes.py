import numpy as np
import numpy.matlib
from math import pi
import matplotlib.pyplot as plt

def genDeuxLunes(d, N):
    """ 
    Génération aléatoire de deux classes de points 2D
    sous forme de lune espacées de d 
    """

    # INPUTS:
    # d: distance entre les deux lunes


    # OUTPUTS:
    # X: matrice (2 x 2N) : Les coordonn<E9>es des points 2D
    # Y: vecteur (2N X 1) : +1 pour la lune du haut et -1 la lune du bas

    # Rayon et largeur
    r = 10
    w = 6

    # Première lune

    # Génération aléatoire des rayons des points entre r-w/2 et r + w/2
    R = (r - w / 2) * np.ones(N) + np.matlib.rand(N) * w

    # Génération aléatoire des angles entre 0 et pi
    theta = np.matlib.rand(N) * pi

    # Calcul des coordonnées des points
    X = np.concatenate((np.multiply(R, np.cos(theta)), np.multiply(R, np.sin(theta))))
    Y = np.ones(N)

    # Deuxième lune

    # Génaration aléatoire des rayons des points entre r-w/2 et r + w/2
    R = (r - w / 2) * np.ones(N) + np.matlib.rand(N) * w

    # Génération aléatoire des angles entre 0 et -pi
    theta = -np.matlib.rand(N) * pi

    # Déplacer les points de dx et dy
    dx = r
    dy = -d

    x = np.concatenate((np.multiply(R, np.cos(theta)) + dx, np.multiply(R, np.sin(theta)) + dy))
    y = -np.ones(N)

    # les deux lunes en un seul vecteur
    X = np.concatenate((X, x), axis = 1)
    Y = np.concatenate((Y, y))

    #Permutation al<E9>atoire de points
    seq = np.random.permutation(2 * N)
    X = X[:, seq]
    Y = Y[seq]

    #Plot des données
    nd = np.where(Y == 1)
    plt.plot(X[0, nd], X[1, nd],'r+')
    nd = np.where(Y != 1)
    plt.plot(X[0, nd], X[1, nd],'bo')
    plt.title('2 moons dataset : r=' + str(r) + ' w=' + str(w) + ' d=' + str(d) + ' N=' + str(N))
    plt.show()

    return X, Y
