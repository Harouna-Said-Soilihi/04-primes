# 2. fonction secondaire
def Fermat(n):
    """verifie si un nombre est de Fermat

    Args:

        n (int): le nombre à vérifier.

    Returns:

        bool: True si n est de Fermat, False sinon.

    """
    return 2**(2**n) + 1
    
# 3. fonction principale
def main():
    # appel à la fonction secondaire ici
    print (Fermat(2))
    print (Fermat(3))
    print (Fermat(4))
    print (Fermat(5))

# 4. appel protégé de la fonction principale
if __name__ == '__main__':

    main()