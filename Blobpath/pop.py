from blob import Blob
import random

class Population:

    def __init__(self, pop_size = 1):

        self.pop_size = pop_size
        self.pop = [Blob(i) for i in range(pop_size)]
        self.created = len(self.pop)

    def run(self, generations = 1):

        for _ in range(generations):

            for blob in self.pop:
                blob.age()

            arrlen = len(self.pop)
            for _ in range(arrlen):
                if blob.alive:
                    if random.random() < blob.replicate:
                        self.pop.append(Blob(self.created))
                        self.created += 1
            ind = 0
            while ind < len(self.pop):

                blob = self.pop[ind]

                if not blob.alive:
                    self.pop.pop(ind)
                    ind -= 1
                ind += 1
            
    def __str__(self,):
        
        string = ''
        for blob in self.pop:
            string += (str(blob) + '\n')
        return string