### Exemple 1 : Tail
# Tail est une commande UNIX qui permet d’afficher les x dernières lignes de texte d’un fichier.
# Trouve un algorithme qui permet de coder cette fonctionnalité.

def head(fileName, n_lines):
    with open(fileName, 'r') as f:
        lines = f.readlines()
        return lines[: n_lines]


print(head("huhu.txt", 2))

def tail(fileName,n_lines):
        with open(fileName, 'r') as f:
            lines = f.readlines()
            return lines[- n_lines:]

print("head")
print(head("huhu.txt",2))
print("tail")
print(tail("huhu.txt",2))



