# Exemple 5 : En commun
# Concevoir un algorithme pour trouver tous les caractères communs à deux listes triées.
# Par exemple, pour les listes a, e, e, e et b, b, c, e, e, g, la sortie doit être de e, e.


# Python program to find the common elements Using Set’s & property
# in two lists
def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        print(a_set & b_set)
        print("No common elements")


a = [1, 2, 3, 4, 5, 6]
b = [5, 6, 7, 8, 9]
common_member(a, b)
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
common_member(a, b)

