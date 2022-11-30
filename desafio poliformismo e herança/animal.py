class Animal():
    def __init__(self, nome, peso):
        self.__nome = nome
        self.__peso = peso

    def locomove(self):
        pass

class Aquatico(Animal):

    def locomove(self):
        print("Um animal aquatico nada.")


class Terrestre(Animal):

    def locomove(self):
        print("animal terrestre anda.")

