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
def store_value(lab, spac, row, fast):
    """ stores the user input values into a dictionary """
    shear[lab] = [spac, row, fast]

pp.pprint(rim_sizes)
project_min_rim = input(f"What's the minimum rim sized allowed per project or preferences? ")

def rim_calcs(k_spacing, k_rows, k_fasteners):
    """ performs calculations for rim width per user input """
    # print(k_spacing, k_rows, k_fasteners)
    if project_min_rim == "a" and k_spacing >= 16 and k_rows == 1 and k_fasteners != "a" != "b" != "c" != "d" != "e" != "f" != "g" != "h" != "i":
        # 1-1/8" LSL logic for 16d box, 16d sinker, 16d common
        print('You can use 1-1/8" rim ')        

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

for k in shear.values():
    # print(f" spacing = {k[0]}, rows = {k[1]}, fastener = {k[2]}")
    k_spacing = k[0]
    k_rows = k[1]
    k_fasteners = k[2]

    rim_calcs(k_spacing, k_rows, k_fasteners)
# TODO work on hierarchy for if statements

