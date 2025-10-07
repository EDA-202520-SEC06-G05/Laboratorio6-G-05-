from DataStructures.Map import map_functions as mp
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list  as lt
import math
import random


def new_map(num_elements,load_factor,prime):
    prime = 109345121
    if load_factor <= 0:
        capacity = int(math.ceil(num_elements/load_factor))
        capacity = mp.next_prime(capacity)
        
        scale = random.randint(1,prime -1)
        shift = random.randint(0,prime -1)
        table = al.new_list()
        for each in range(capacity):
            element = lt.new_list()
            al.add_last(table,element)
            
        
        current_factor = 0
        limit_factor = load_factor
        size = 0
        my_map = {
            "prime": prime,
            "capacity": capacity,
            "scale": scale,
            "shift": shift,
            "table": table,
            "current_factor" : current_factor,
            "limit_factor":limit_factor,
            "size": 0
        }
    else:
        return ("ValueError. load_factor debe ser > 0")
        
    return my_map 