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
    shear[lab] = {"spacing": spac, "rows": row, "fastener": fastener_size[fast]}
    # 1-1/8" width logic, single row
    if ((project_min_rim == "a" and spac >= 16 and row == 1 and fast in "bjk") or
        (project_min_rim == "a" and spac >= 12 and row == 1 and fast in "l") or
        (project_min_rim == "a" and spac >= 6 and row == 1 and fast in "cdefghi")):
        shear[lab]["rim_sizes"] = rim_sizes["a"]
    # 1-1/4" width logic, single row
    if ((project_min_rim == "b" and spac >= 6 and row == 1 and fast in "ab") or
        (project_min_rim == "b" and spac >= 6 and row == 1 and fast in "cedefghijkl")):
        shear[lab]["rim_sizes"] = rim_sizes["b"]

    # if any of the above calculations do not return a favorable value, outputs an error
    else:
        shear[lab]["rim_sizes"] = "NO SOLUTION, REFERENCE TB-206 FOR MORE INFORMATION"

more_shear_walls = True
while more_shear_walls:
    label = input("Input label for shear wall: ")
    spacing = float(input("Input the spacing (in inches): "))
    while spacing <= 0 or spacing >= 50:
        spacing = float(input("Invalid quantity, please input a valid spacing (in inches): "))
        if spacing > 0 and spacing < 50:
            break
        else:
            continue
    rows = int(input("Input number of rows: "))
    while rows <= 0 or rows >5:
        rows = int(input("Invalid quantity, please input a valid number of rows: "))
        if rows > 0 and rows <=5:
            break
        else:
            continue
    pp.pprint(fastener_size)
    fastener_type = input("Select a fastener type: ")
    store_value(label, spacing, rows, fastener_type)
    
    another = input("Input another shear wall? ").lower()
    if another == "yes":
        continue
    else:
        more_shear_walls = False

pp.pprint(shear)
