# -----------------------------------------------------------------------------
# Fonction : square
# Description : Calcule le carré d'un nombre.
# Paramètres :
#     - number (int/float) : Le nombre dont on veut calculer le carré.
# Retour :
#     - int/float : Le carré du nombre.
# -----------------------------------------------------------------------------
def square(number):
    """
    Calcule le carré d'un nombre.

    @param number: Le nombre dont on veut calculer le carré.
    @type number: int ou float

    @return: Le carré du nombre.
    @rtype: int ou float
    """
    return number * number


# -----------------------------------------------------------------------------
# Classe : Person
# Description : Représente une personne avec son nom et son âge.
# -----------------------------------------------------------------------------
class Person:
    """
    Représente une personne avec son nom et son âge.

    Attributes:
        name (str): Le nom de la personne.
        age (int): L'âge de la personne.
    """

    def __init__(self, name, age):
        """
        Initialise une nouvelle instance de la classe Person.

        @param name: Le nom de la personne.
        @type name: str

        @param age: L'âge de la personne.
        @type age: int
        """
        self.name = name
        self.age = age

    def greet(self):
        """
        Affiche un message de salutation pour la personne.
        """
        print(f"Bonjour, je m'appelle {self.name} et j'ai {self.age} ans.")


# -----------------------------------------------------------------------------
# Fonction principale pour tester les exemples de balises Doxygen.
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    """
    Fonction principale pour tester les exemples de balises Doxygen.
    """
    # Créer une personne et afficher un message de salutation
    person = Person("Alice", 30)
    person.greet()

    # Calculer le carré d'un nombre et l'afficher
    number = 5
    squared = square(number)
    print(f"Le carré de {number} est {squared}.")
