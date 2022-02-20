WEAPON_DATA = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphic': '../graphics/weapons/sword/'},
    'lance': {'cooldown': 400, 'damage': 30, 'graphic': '../graphics/weapons/lance/'},
    'axe': {'cooldown': 300, 'damage': 20, 'graphic': '../graphics/weapons/axe/'},
    'rapier': {'cooldown': 50, 'damage': 8, 'graphic': '../graphics/weapons/rapier/'},
    'sai': {'cooldown': 80, 'damage': 10, 'graphic': '../graphics/weapons/sai/'}
}


def get_next_index(index):
    next_index = index + 1
    if next_index >= len(WEAPON_DATA):
        next_index = 0
    return next_index


def get_name(index):
    return list(WEAPON_DATA.keys())[index]


def get_graphics(index):
    return WEAPON_DATA[get_name(index)]['graphic']


def get_cooldown(index):
    return WEAPON_DATA[get_name(index)]['cooldown']


def get_damage(index):
    return WEAPON_DATA[get_name(index)]['damage']
