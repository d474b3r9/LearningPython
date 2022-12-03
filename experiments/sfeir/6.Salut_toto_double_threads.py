# Exemple 6 : Salut Toto
# À l’aide de deux threads, écrire “Salut Toto Salut Toto Salut Toto”, sachant que le premier thread écrit “Salut” et que le deuxième écrit “Toto”.
# ici sync
# sinon asyncio
# sinon threading
# sinon multiprocessing

import threading

def do_first():
    print("Running do_first line 1")
    print("Running do_first line 2")
    print("Running do_first line 3")

def do_second():
    print("Running do_second line 1")
    print("Running do_second line 2")
    print("Running do_second line 3")

def main():
    t1 = threading.Thread(target=do_first)
    t2 = threading.Thread(target=do_second)

    # Start threads
    t1.start(), t2.start()

    # Wait threads to complete
    t1.join(), t2.join()

if __name__ == "__main__":
    main()