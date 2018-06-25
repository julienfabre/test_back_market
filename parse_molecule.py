# Built-in imports
import collections
from pprint import pprint

water = 'H2O'
magnesium_hydroxide = 'Mg(OH)2'
fremy_salt = 'K4[ON(SO3)2]2'


def parse_molecule(chemical_formula):
    """
    Count the number of atoms of each element contained in a chemical formula and return a dict.
    :param chemical_formula: Chemical formula to parse.
    :type chemical_formula: basestring
    :return: Dict with the counts of each atom.
    :rtype: dict
    """

    if not chemical_formula:
        return None

    formula_length = len(chemical_formula)

    # An array of Counters, where each Counter represents a subformula. A subformula is a formula in between an opening
    # and closing bracket. Each counter is keeping track of the subformula's atom count . Storing multiple Counters
    # allows us to handle multiple and nested brackets.
    subformulas_list = [collections.Counter()] 

    # Brackets can be round, squared or curly.
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']

    main_index = 0
    while main_index < formula_length:
        # Iterating through the chemical formula.

        if chemical_formula[main_index] in opening_brackets:  # Beginning of a subformula.
            subformulas_list.append(collections.Counter())  # Adding a new subformula to the subformulas list
            main_index += 1

        elif chemical_formula[main_index] in closing_brackets:  # End of a subformula.
            subformula = subformulas_list.pop()  # Popping the subformula from the subformulas list.
            main_index += 1
            temp_index_start = main_index

            while main_index < formula_length and chemical_formula[main_index].isdigit():
                # Parsing the multiplicity of the subformula.
                main_index += 1

            # Default multiplicity is 1.
            multiplicity = int(chemical_formula[temp_index_start: main_index] or 1)

            for atom_name, atom_count in subformula.items():
                # Applying multiplicity to each atom of the subformula.
                subformulas_list[-1][atom_name] += atom_count * multiplicity

        else:  # Parsing an atom.
            temp_index_start = main_index
            main_index += 1

            #  Handling the case of atoms represented by multiple characters (ex: Al for Aluminium or Cl for chlorine).
            while main_index < formula_length and chemical_formula[main_index].islower():
                main_index += 1

            atom_name = chemical_formula[temp_index_start: main_index]
            temp_index_start = main_index

            while main_index < formula_length and chemical_formula[main_index].isdigit():
                # Parsing the multiplicty of the atom.
                main_index += 1

            # Default multiplicity is 1.
            multiplicity = int(chemical_formula[temp_index_start: main_index] or 1)

            # Adding the mulitiplicity of the atom to the subformula's Counter.
            subformulas_list[-1][atom_name] += multiplicity

    return subformulas_list[-1]


if __name__ == '__main__':
    pprint(parse_molecule(water))
    pprint(parse_molecule(magnesium_hydroxide))
    pprint(parse_molecule(fremy_salt))


