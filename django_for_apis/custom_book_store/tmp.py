class Person:
    def __init__(self,name):
        self.name=name


    def __str__(self):
        return self.name


a=Person("hogehoge")

print(f"{a} is me?")



def dict_factory(cursor, row):
   d = {}
   for idx, col in enumerate(cursor.description):
       d[col[0]] = row[idx]
   return d