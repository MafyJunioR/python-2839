class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if valor is None or valor.strip() == '':
            raise ValueError('No aceptamos None como valor de nombre, ni textos vacíos')

        self.__nombre = valor.strip()

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        if valor is None or valor < 0:
            raise ValueError('No se acepta un precio None ni menor que 0')

        self.__precio = valor

    def __eq__(self, otro):
        return isinstance(otro, Producto) and self.nombre == otro.nombre and self.precio == otro.precio

    def __hash__(self):
        return hash((self.nombre, self.precio))

    def __str__(self):
        return f'Producto(nombre={self.nombre}, precio={self.precio})'
