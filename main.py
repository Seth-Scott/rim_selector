import pprint as pp

# TODO clear screen before input 
import os

fastener_size = {
    "a": "SDS",
    "b": "16d common",
    "c": "8d common",
    "d": "8d N8 or NA11",
    "e": "10d box",
    "f": "12d box",
    "g": "10d common",
    "h": "12d common",
    "i": "10d N10 or NA9D",
    "j": "16d box",
    "k": "16d sinker",
    "l": "16d common",
}

# user inputs values into this dictionary. dictionary is comprised of values in this order: label: spacing, rows, fastener type
#     "A": [6, 2, fastener_size["a"]]

shear = {}

def store_value(lab, spac, row, fast):
    shear[lab] = [spac, row, fast]


more_shear_walls = True
while more_shear_walls:
    label = input("Input label for shear wall: ")
    spacing = input("Input the spacing (in inches): ")
    rows = input("Input number of rows: ")
    pp.pprint(fastener_size)
    fastener_type = input("Select a fastener type: ")
    store_value(label, spacing, rows, fastener_type)
    
    another = input("Input another shear wall? ").lower()
    if another == "yes":
        continue
    else:
        more_shear_walls = False
        break

pp.pprint(shear)

# TODO work on hierarchy for if statements