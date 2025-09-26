import math

def syracuse(n):

    # initialisation des variables
    tv = 0  # temps de vol
    tva = 0 # temps de vol en altitude
    am = n  # altitude maximale
    n0 = n  # valeur initiale


    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        tv = tv+1
        if n > am:
            am = n
        if n > n0:
            tva = tva+1

    return tv, tva, am # retour de tv, tva, am


def main():
    # exemple d'exécution
    n = 127
    tv, tva, am = syracuse(n)
    print(n, tv, tva, am)

if __name__ == "__main__":
    main()
