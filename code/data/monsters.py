MONSTER_DATA = {
    'squid': {'health': 100, 'experience': 100, 'damage': 20, 'attack_type': 'slash',
              'attack_sound': '../audio/attack/slash.wav', 'collide_inflate': (-30, -10),
              'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'raccoon': {'health': 300, 'experience': 250, 'damage': 40, 'attack_type': 'claw',
                'attack_sound': '../audio/attack/claw.wav', 'collide_inflate': (-100, -90),
                'speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
    'spirit': {'health': 100, 'experience': 110, 'damage': 8, 'attack_type': 'thunder',
               'attack_sound': '../audio/attack/fireball.wav', 'collide_inflate': (-10, -20),
               'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
    'bamboo': {'health': 70, 'experience': 120, 'damage': 6, 'attack_type': 'slash',
               'attack_sound': '../audio/attack/slash.wav', 'collide_inflate': (-20, -10),
               'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}
}


def get_index(name):
    return list(MONSTER_DATA.keys()).index(name)


def get_next_index(index):
    next_index = index + 1
    if next_index >= len(MONSTER_DATA):
        next_index = 0
    return next_index


def get_name(index):
    return list(MONSTER_DATA.keys())[index]


def get_health(index):
    return MONSTER_DATA[get_name(index)]['health']


def get_experience(index):
    return MONSTER_DATA[get_name(index)]['experience']


def get_damage(index):
    return MONSTER_DATA[get_name(index)]['damage']


def get_attack_type(index):
    return MONSTER_DATA[get_name(index)]['attack_type']


def get_attack_sound(index):
    return MONSTER_DATA[get_name(index)]['attack_sound']


def get_speed(index):
    return MONSTER_DATA[get_name(index)]['speed']


def get_resistance(index):
    return MONSTER_DATA[get_name(index)]['resistance']


def get_attack_radius(index):
    return MONSTER_DATA[get_name(index)]['attack_radius']


def get_notice_radius(index):
    return MONSTER_DATA[get_name(index)]['notice_radius']


def get_collide_inflate(index):
    return MONSTER_DATA[get_name(index)]['collide_inflate']
