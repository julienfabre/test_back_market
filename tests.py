from parse_molecule import parse_molecule
from parse_molecule import water, magnesium_hydroxide, fremy_salt


def test_empty_string():
    assert parse_molecule(None) is None


def test_water():
    water_dict = {'H': 2, 'O': 1}
    assert parse_molecule(water) == water_dict


def test_magnesium_hydroxide():
    magnesium_hydroxide_dict = {'Mg': 1, 'O': 2, 'H': 2}
    assert parse_molecule(magnesium_hydroxide) == magnesium_hydroxide_dict


def test_fremy_salt():
    fremy_salt_dict = {'K': 4, 'O': 14, 'N': 2, 'S': 4}
    assert parse_molecule(fremy_salt) == fremy_salt_dict


def test_fremy_salt_curly_braces():
    fremy_salt_curly = 'K4{ON(SO3)2}2'
    fremy_salt_dict = {'K': 4, 'O': 14, 'N': 2, 'S': 4}
    assert parse_molecule(fremy_salt_curly) == fremy_salt_dict

