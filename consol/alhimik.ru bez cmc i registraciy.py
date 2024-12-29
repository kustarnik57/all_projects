from random import random,randint 




class Potion:
    def __init__(self,name,quality):
        self.name = name
        self.quality = quality


    def __str__(self):
        return f'Tnis potion named: {self.name}'

    def __add__(self,other):
        _new_quality_ = (self.quality + other.quality) / 2  - (abs(self.quality - other.quality)) * (random() * (1 + 1) -1)
        if _new_quality_ < 30:
            raise ValueError('плохой из тебя алхимик!')
        self_len = len(self.name) // 2        
        other_len = len(other.name) // 2        
        new_name = self.name[:self_len] + other.name[other_len:]
        return Potion(new_name,_new_quality_)

a=Potion('smetana',randint(30, 80))

b=Potion('ketchup',randint(30, 80))

print (a + b)











