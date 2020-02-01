import math

def find_color(r, g, b):

    obj = {
        'Red' : (255, 0, 0),
        'Yellow' : (255, 255, 0),
        'Green' : (0, 255, 0),
        'Cyan' : (0, 255, 255),
        'Blue' : (0, 0, 255,),
        'Purple' : (255, 0, 255),
        'Black' : (0, 0, 0),
        'White' : (255, 255, 255),
        }

    low_dist = None
    color = None

    for i, key in enumerate(obj):

        dis = euc_dist((r, g, b,), obj[key])

        if low_dist == None or dis <= low_dist:

            low_dist = dis
            color = key
            
    return color


def euc_dist(arr1, arr2):

   
    distance = 0.0
    
    for i, val in enumerate(arr1):

        dis = val - arr2[i]

        distance += dis * dis

    return math.sqrt(distance)

##r, g, b = , 128, 194
##
##print(r, g, b)
##
##print("Here is your color:", find_color(r, g, b))


colors = [
  (52,38,43),
  (128,129,97),
  (48,250,178),
  (200,200,200),
  (185,179,112),
  (300,421,419),
]

for color in colors:
  r,g,b=color
  print(find_color(r,g,b))
