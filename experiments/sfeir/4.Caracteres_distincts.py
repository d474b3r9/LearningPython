# Dans une chaîne, détecter la plus longue chaîne de caractères composée de caractères distincts.
# Par exemple : “abcdemo” est la plus longue chaîne de caractères distincts de “abcdemoderneancien”
# définit la plage de caractères se règle avec du windowing
def longeur_max(phrase):
    max_index = 0
    for i in range(len(phrase)):
        if len(phrase[i]) >= len(phrase[max_index]):
            max_index = i

    return len(phrase[max_index])

def longuestElement(maListe):
        len(max(maListe, key=len))


print(longeur_max("abcbdbdbbdcdabd"))
# version hardcore
CHAR_RANGE = 128

# Fonction pour trouver la plus longue sous-string d'un contenant donné
# `k` caractères distincts utilisant une fenêtre glissante
def findLongestSubstring(s, k):
    # stocke les limites de sous-string les plus longues
    end = begin = 0

    # configuré pour stocker des caractères distincts dans une fenêtre
    window = set()

    # `freq` mémorise la fréquence des caractères présents dans le
    # fenêtre courante. Nous pouvons également utiliser un dictionnaire à la place.

    freq = [0] * CHAR_RANGE

    # `[low…high]` maintient les limites de la fenêtre glissante
    low = high = 0

    while high < len(s):

        window.add(s[high])
        freq[ord(s[high])] = freq[ord(s[high])] + 1

        # si la taille de la fenêtre est supérieure à `k`, supprimez les caractères de gauche
        while len(window) > k:

            # Si la fréquence du caractère le plus à gauche devient 0 après
            # en le retirant dans la fenêtre, enlevez-le également de l'ensemble
            freq[ord(s[low])] = freq[ord(s[low])] - 1
            if freq[ord(s[low])] == 0:
                window.remove(s[low])

            low = low + 1  # réduit la taille de la fenêtre

        # mettre à jour la taille maximale de la fenêtre si nécessaire
        if end - begin < high - low:
            end = high
            begin = low

        high = high + 1

    # renvoie la plus longue sous-string trouvée à `s[begin…end]`
    return s[begin:end + 1]


if __name__ == '__main__':
    s = 'abcbdbdbbdcdabd'
    k = 3

    print(findLongestSubstring(s, k))
