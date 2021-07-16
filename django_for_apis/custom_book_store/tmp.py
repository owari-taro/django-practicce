class Person:
    def __init__(self,name):
        self.name=name


    def __str__(self):
        return self.name


a=Person("hogehoge")

print(f"{a} is me?")