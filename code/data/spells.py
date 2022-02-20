MAGIC_DATA = {
    'flame': {'strength': 5, 'cost': 20, 'graphic': '../graphics/particles/flame/fire.png'},
    'heal': {'strength': 20, 'cost': 10, 'graphic': '../graphics/particles/heal/heal.png'}
}


def get_next_index(index):
    next_index = index + 1
    if next_index >= len(MAGIC_DATA):
        next_index = 0
    return next_index


def get_name(index):
    return list(MAGIC_DATA.keys())[index]


def get_graphics(index):
    return MAGIC_DATA[get_name(index)]['graphic']


def get_strength(index):
    return MAGIC_DATA[get_name(index)]['strength']


def get_cost(index):
    return MAGIC_DATA[get_name(index)]['cost']
