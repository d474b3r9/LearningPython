# Exemple 8 : Matrice triée
# Étant donné une matrice de nombres entiers, où chaque ligne et chaque colonne sont triées par ordre croissant, imprimer tous les éléments dans l’ordre croissant.

a = np.array([[1,4], [3,1]])
a.sort(axis=1)

array([[1, 4],
       [1, 3]])

a.sort(axis=0)
array([[1, 3],
       [1, 4]])