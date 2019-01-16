class Dog:

    def __init__(self, name, age):
        Dog.name = name
        Dog.age = age


if __name__ == "__main__":
    perro = Dog("uno", 5)
    perro2 = Dog("dos", 8)

    print("%d %d" %(perro.age, perro2.age))
    perro2.age = 10

    print("%d %d" %(perro.age, perro2.age))