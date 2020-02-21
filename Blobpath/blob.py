
import random

class Blob:

    colors = ['red','yellow','green' ]
    
    def __init__(self, name = 0):
        
        self.blob_color = random.choice(Blob.colors)
        self.years     = 0
        self.alive     = True
        self.been_dead = None
        self.genes     = [random.randint(1,10) for _ in range(10)]
        self.replicate = [.1, .25, .4][Blob.colors.index(self.blob_color)]
        self.name = name

    def age(self,):

        chance_of_death = (100 - sum(self.genes))/100
        self.die = random.random()

        if self.alive:
            self.years += 1
            if self.die < chance_of_death:
                self.alive = False
        
        if not self.alive:
            if self.been_dead == None:
                self.been_dead = 0
            else:
                self.been_dead += 1
    
                
    def __str__(self,):
        if self.alive == True:
            return f'{self.name} is a {self.blob_color} blob. He is currently {self.years} years old.'
        else:
            return f'{self.name} was a {self.blob_color} blob. He lived to be {self.years} years old and died {self.been_dead} years ago.'
        


