import math

# Clase que representa un cuadrado
class Cuadrado:
    def __init__(self, lado):
        """Inicializa el cuadrado con un lado dado."""
        self.lado = lado  # Propiedad que almacena el lado del cuadrado

    def calcular_area(self):
        """Calcula el área del cuadrado.
        Devuelve un valor float, se utiliza para calcular el área de un cuadrado,
        requiere como argumento el lado del cuadrado.
        """
        return self.lado ** 2  # Fórmula: lado^2

    def calcular_perimetro(self):
        """Calcula el perímetro del cuadrado.
        Devuelve un valor float, se utiliza para calcular el perímetro de un cuadrado,
        requiere como argumento el lado del cuadrado.
        """
        return 4 * self.lado  # Fórmula: 4 * lado


# Clase que representa un rectángulo
class Rectangulo:
    def __init__(self, ancho, alto):
        """Inicializa el rectángulo con un ancho y alto dados."""
        self.ancho = ancho  # Propiedad que almacena el ancho del rectángulo
        self.alto = alto    # Propiedad que almacena el alto del rectángulo

    def calcular_area(self):
        """Calcula el área del rectángulo.
        Devuelve un valor float, se utiliza para calcular el área de un rectángulo,
        requiere como argumento el ancho y alto del rectángulo.
        """
        return self.ancho * self.alto  # Fórmula: ancho * alto

    def calcular_perimetro(self):
        """Calcula el perímetro del rectángulo.
        Devuelve un valor float, se utiliza para calcular el perímetro de un rectángulo,
        requiere como argumento el ancho y alto del rectángulo.
        """
        return 2 * (self.ancho + self.alto)  # Fórmula: 2 * (ancho + alto)


# Clase principal para ejecutar el programa
if __name__ == "__main__":

    # Crear una instancia de Cuadrado con un lado de 4
    cuadrado = Cuadrado(4)
    print(f"Área del cuadrado: {cuadrado.calcular_area():.2f}")
    print(f"Perímetro del cuadrado: {cuadrado.calcular_perimetro():.2f}")

    # Crear una instancia de Rectangulo con un ancho de 3 y alto de 6
    rectangulo = Rectangulo(3, 6)
    print(f"Área del rectángulo: {rectangulo.calcular_area():.2f}")
    print(f"Perímetro del rectángulo: {rectangulo.calcular_perimetro():.2f}")
