from math import sqrt 
def isprime(p):
    """verifie si un nombre est premier

    Args:

        p (float): le nombre à vérifier.

    Returns:

        bool: True si p est premier, False sinon.

    """
    # votre code ici
    if p<=1:
        return False
    if p%2==0:
        return False 
    for i in range(3,int(sqrt(p))+1,2):
        if p % i == 0 :
            return False
    return True
    #### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(2,100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()