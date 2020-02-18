
import random

class Blob:

    colors = ['red', 'green', 'yellow']
    
    def __init__(self,):
        
        self.blob_color = random.choice(Blob.colors)
        self.years = 0
        self.alive = True
        self.been_dead = None
        
    def age(self, chance_of_death = .5):
        
        self.die = random.random()
        
        if self.die < chance_of_death:
            self.alive = False
        if not self.alive == False:
            self.years += 1
        if not self.alive:
            if self.been_dead == None:
                self.been_dead = 0
            else:
                self.been_dead += 1
                
    def __str__(self,):
        if self.alive == True:
            return f'Blobby is a {self.blob_color} blob. He is currently {self.years} years old.'
        else:
            return f'Blobby was a {self.blob_color} blob. He lived to be {self.years + 1} years old and died {self.been_dead} years ago.'
        
blobby = Blob()
for _ in range(10):
    
    
    blobby.age()
    print(blobby)

