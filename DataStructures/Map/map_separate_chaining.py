from DataStructures.Map import map_functions as mp
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list  as lt
import math
import random


def new_map(num_elements,load_factor,prime):
    prime = 109345121
    if load_factor > 0:
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

def rehash(my_map):
    capacity = my_map["capacity"] * 2
    capacity = mp.next_prime(capacity)

    nueva_tabla = al.new_list()
    for i in range(capacity):
        lista = lt.new_list()
        al.add_last(nueva_tabla, lista)

    vieja_tabla = my_map["table"]
    my_map["capacity"] = capacity
    my_map["table"] = nueva_tabla
    my_map["size"] = 0
    my_map["current_factor"] = 0

    for bucket in vieja_tabla["elements"]:
        for elemento in bucket["elements"]:
            if elemento["key"] is not None:
                put(my_map, elemento["key"], elemento["value"])

    return my_map


def put(my_map, key, value):
    hash = mp.hash_value(my_map, key)
    lista = my_map["table"]["elements"][hash]

    existe = False
    for elemento in lista["elements"]:
        if elemento["key"] == key:
            elemento["value"] = value
            existe = True
            break

    if existe == False:
        lt.add_last(lista, {"key": key, "value": value})
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
        if my_map["current_factor"] > my_map["limit_factor"]:
            rehash(my_map)

    return my_map



