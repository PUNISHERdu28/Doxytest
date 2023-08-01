# -----------------------------------------------------------------------------
# Fonction : add
# Description : Effectue l'addition de deux nombres.
# Paramètres :
#     - num1 (int/float) : Le premier nombre.
#     - num2 (int/float) : Le second nombre.
# Retour :
#     - int/float : Le résultat de l'addition.
# Exceptions :
#     - ValueError : Si l'un des paramètres n'est pas un nombre.
# -----------------------------------------------------------------------------
def add(num1, num2):
    """
    Effectue l'addition de deux nombres.

    Cette fonction prend deux nombres (int ou float) en entrée et renvoie le résultat de l'addition.
    Si l'un des paramètres n'est pas un nombre valide, une exception ValueError est levée.

    Args:
        num1 (int or float): Le premier nombre.
        num2 (int or float): Le second nombre.

    Returns:
        int or float: Le résultat de l'addition.

    Raises:
        ValueError: Si l'un des paramètres n'est pas un nombre valide.
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Les paramètres doivent être des nombres (int ou float).")
    return num1 + num2


# -----------------------------------------------------------------------------
# Classe : Rectangle
# Description : Représente un rectangle avec sa largeur et sa hauteur.
# -----------------------------------------------------------------------------
class Rectangle:
    """
    Représente un rectangle avec sa largeur et sa hauteur.

    Cette classe définit une représentation basique d'un rectangle avec sa largeur et sa hauteur.
    Elle peut être utilisée pour effectuer des calculs de surface et de périmètre.

    Attributes:
        width (int/float): La largeur du rectangle.
        height (int/float): La hauteur du rectangle.
    """

    def __init__(self, width, height):
        """
        Initialise une nouvelle instance de la classe Rectangle.

        Cette méthode permet de créer un nouvel objet de la classe Rectangle en fournissant une largeur et une hauteur.

        Args:
            width (int or float): La largeur du rectangle.
            height (int or float): La hauteur du rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calcule la surface du rectangle.

        Returns:
            int/float: La surface du rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calcule le périmètre du rectangle.

        Returns:
            int/float: Le périmètre du rectangle.
        """
        return 2 * (self.width + self.height)


# -----------------------------------------------------------------------------
# Fonction : is_prime
# Description : Vérifie si un nombre est premier.
# Paramètres :
#     - num (int) : Le nombre à vérifier.
# Retour :
#     - bool : True si le nombre est premier, False sinon.
# -----------------------------------------------------------------------------
def is_prime(num):
    """
    Vérifie si un nombre est premier.

    Cette fonction prend un nombre entier en entrée et vérifie s'il est premier.
    Un nombre premier est un nombre entier supérieur à 1 et qui n'a aucun diviseur autre que 1 et lui-même.

    Args:
        num (int): Le nombre à vérifier.

    Returns:
        bool: True si le nombre est premier, False sinon.
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# -----------------------------------------------------------------------------
# Classe : Point
# Description : Représente un point dans un espace 2D.
# -----------------------------------------------------------------------------
class Point:
    """
    Représente un point dans un espace 2D.

    Cette classe définit une représentation d'un point dans un espace 2D avec ses coordonnées x et y.
    Elle peut être utilisée pour effectuer des opérations géométriques simples.

    Attributes:
        x (int/float): La coordonnée x du point.
        y (int/float): La coordonnée y du point.
    """

    def __init__(self, x, y):
        """
        Initialise une nouvelle instance de la classe Point.

        Cette méthode permet de créer un nouvel objet de la classe Point en fournissant des coordonnées x et y.

        Args:
            x (int or float): La coordonnée x du point.
            y (int or float): La coordonnée y du point.
        """
        self.x = x
        self.y = y

    def distance_to_origin(self):
        """
        Calcule la distance du point à l'origine (0, 0).

        Returns:
            float: La distance du point à l'origine.
        """
        return (self.x**2 + self.y**2)**0.5


# -----------------------------------------------------------------------------
# Variables globales
# -----------------------------------------------------------------------------
PI = 3.14159
MAX_ITERATIONS = 100
DEFAULT_WIDTH = 10
DEFAULT_HEIGHT = 5.5
name = "John Doe"
age = 30
temperature = 25.5
is_raining = True
