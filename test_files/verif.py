import re
import sys
import os

equivalence = {}

with open("src/oplsaa.lt", 'r') as oplsaa_file:
    for line in oplsaa_file:
        line = line.strip()

        if re.match("^replace{", line):
            line = line.split()
            equivalence[line[1][6:]] = line[2][6:]

lst_files = os.listdir("src")
lst_files.remove("oplsaa.lt")

for f in lst_files:

    atoms = {}
    bonds = []

    with open("src/{}".format(f), 'r') as aa_file:
        for line in aa_file:
            line = line.strip()

            if re.match("^\$atom", line):
                line = line.split()
                atoms[line[0][6:]] = "{}".format(int(line[2][6:]))
            elif re.match("^\$bond", line):
                line = line.split()
                bonds.append([line[0][6:], line[1][6:], line[2][6:], line[3][6:]]) 
            else:
                pass

    for b in bonds:
        names = b[0].split("-")
        bond_type = [int(i) for i in b[1].split("_")]

        if b[2] not in names or b[3] not in names:
            raise ValueError("Erreur de nom dans le lien {} dans le fichier {}.".format(b[0], f))

        eq_a = equivalence[atoms[b[2]]].split("_")[1][1:]
        eq_b = equivalence[atoms[b[3]]].split("_")[1][1:]

        verif_bond_type = sorted([int(eq_a), int(eq_b)])

        if bond_type != verif_bond_type:
            raise ValueError("Erreur de bond type dans le lien {} dans le fichier {}. eq_a:{} eq_b:{}".format(b[0], f, eq_a, eq_b))

    print("Pas d'erreur dans le fichier {}".format(f))