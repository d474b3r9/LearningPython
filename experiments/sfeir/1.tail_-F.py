### Exemple 1 : Tail -F
# Tail est une commande UNIX qui permet d’afficher les x dernières lignes de texte d’un fichier.
# Trouve un algorithme qui permet de coder cette fonctionnalité.


import os, sys
from time import sleep

if len(sys.argv) == 1:
    print("Argument Missing !")
    print("Usage:\n    {0:s} /path/to/log/file".format(sys.argv[0]))
    sys.exit(1)

fileName = sys.argv[1]

if not os.path.exists(fileName) or not os.path.isfile(fileName):
    print("This file '{0:s}' does not exist !".format(fileName))
    sys.exit(2)

try:
    with open(fileName, 'r') as f:
        f.read(1)
except Exception as e:
    print("This file '{0:s}' cannot be opened for reading !".format(fileName))
    sys.exit(3)

folderLogs = os.path.dirname(fileName)

copyLines = []

try:

    while True:
        with open(fileName, 'r') as f:
            lines = f.readlines()

        show = False

        if len(copyLines) == 0:
            showLines = lines[-10:]
            show = True

        elif len(copyLines) != len(lines):
            showLines = lines[len(copyLines) - len(lines):]
            show = True

        if show:
            copyLines = lines.copy()
            for line in showLines:
                print(line, end='')

        sleep(1)

except KeyboardInterrupt as e:
    print("Program stopped by user !")
    sys.exit(0)

except Exception as e:
    print("Unknown error during execution !")
    print(e)
    sys.exit(4)

