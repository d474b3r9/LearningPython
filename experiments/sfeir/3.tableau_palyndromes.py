# Un nombre est un palindrome si il s’écrit de la même manière après l’inversion de ce dernier.
def check_palindrome(v):
    if len(v) < 1:
        return True
    else:
        if v[0] == v[-1]:
            return check_palindrome(v[1:-1])
        else:
            return False
var = input(("Entrez une valeur: "))
if(check_palindrome(var)):
    print("L'entrée est un palindrome")
else:
    print("L'entrée n'est pas un palindrome")