from blob import Blob
import json

# with open('blobby.json') as f:
#     data = json.load(f)
#     print(data)

# blobby = Blob()
# # blobby.__dict__ = data
# for _ in range(10):
    
    
#     blobby.age()
#     print(blobby)
# print(blobby.__dict__)
# with open('blobby.json', 'w') as f:
#     json.dump(blobby.__dict__, f)

from pop import Population

ga = Population(20)
print(ga)
print()
ga.run(5)
print(ga)