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
    "l": "pneumatic",

}

rim_sizes = {
    "a": '1-1/8" LSL',
    "b": '1-1/4" LSL',
    "c": '1-1/2" LSL',
    "d": '1-3/4" LSL', 
    "e": '3-1/2" LSL',
}

# user inputs values into this dictionary. dictionary is comprised of values in this order: label: spacing, rows, fastener type
#     "A": [6, 2, fastener_size["a"]]

shear = {}

pp.pprint(rim_sizes)
project_min_rim = input(f"What's the minimum rim sized allowed per project or preferences? ")

def store_value(lab, spac, row, fast):
    """ stores the user input values into a dictionary """
    shear[lab] = [spac, row, fast]
    # 1-1/8" width logic
    if project_min_rim == "a" and spac >= 16 and row == 1 and fast == "b" or fast == "j" or fast == "k":
        shear[lab].append(rim_sizes["a"])
    elif project_min_rim == "a" and spac >= 12 and row == 1 and fast == "l":
        shear[lab].append(rim_sizes["a"])
    elif project_min_rim == "a" and spac >= 6 and row == 1 and fast == "c" or fast == "d" or fast == "e" or fast == "f" or fast == "g" or fast == "h" or fast == "i":
        shear[lab].append(rim_sizes["a"])

more_shear_walls = True
while more_shear_walls:
    label = input("Input label for shear wall: ")
    spacing = float(input("Input the spacing (in inches): "))
    rows = int(input("Input number of rows: "))
    pp.pprint(fastener_size)
    fastener_type = input("Select a fastener type: ")
    store_value(label, spacing, rows, fastener_type)
    
    another = input("Input another shear wall? ").lower()
    if another == "yes":
        continue
    else:
        more_shear_walls = False

pp.pprint(shear)

# for k in shear.values():
#     # print(f" spacing = {k[0]}, rows = {k[1]}, fastener = {k[2]}")
#     k_spacing = k[0]
#     k_rows = k[1]
#     k_fasteners = k[2]
