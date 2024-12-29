class Cat:  
    def __init__(self,name):
        self.name = name
    def __add__(self,other):
        result = self.name + other.name
        return Cat (result)

    def __str__(self):
        return f"Cat: {self.name}"


fluffy = Cat('ЯЗАГИ')

igor = Cat('ТЛЕРА')






print(fluffy+igor)






