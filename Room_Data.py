import Room
import entity

import random

# When u make a corner make sure to add the width to length,
# this will make sure the enemies don't path find through corner
#
# Objects:
# Room: enemies[], chests[], walls[], bullets[]
# Enemy: sprite, current_x, current_y, speed, health, attack_power, attack_range, agro_range, enemy_type
# Door: X_1, Y_1, X_2, Y_2, room_1, room_2
# Chest: X, Y, items[]
# Wall: X, Y, width, height, vertical
#
#
chest_array = [[1, 20, 20, 10, 1], [1, 20, 20, 10, 1], [1, 20, 20, 10, 1], [1, 20, 20, 0, 1]]

enemy_image_sheet_type_0 = entity.SpriteSheet('Assets/Sprite/Close_Enemy.png')
enemy_image_sheet_type_1 = entity.SpriteSheet('Assets/Sprite/eye_shooter.png')

## ROOM 1
room_1_enemies = [
    entity.Enemy(enemy_image_sheet_type_0, 15, 500, 2.5, 100, 50, 64, 500, 0),
    entity.Enemy(enemy_image_sheet_type_0, 700, 15, 2.5, 100, 50, 64, 200, 0),
    entity.Enemy(enemy_image_sheet_type_1, 700, 500, 2.5, 100, 50, 500, 500, 1),
]
room_1_walls = [
    Room.Wall(100, 300, 10, 300, True),
    Room.Wall(500, 100, 300, 10, False),
    Room.Wall(400, 300, 10, 160, True),
    Room.Wall(400, 450, 150, 10, False),
    # Room.Wall(550, 290, 10, 170, True),
    # Room.Wall(400, 290, 150, 10, False)
]
room_1_chests = [
    Room.Chest(550, 120, chest_array[0], False)
]
room_1 = Room.Room(room_1_enemies, room_1_chests, room_1_walls, [])

# ROOM 2
room_2_enemies = [
    entity.Enemy(enemy_image_sheet_type_0, 100, 100, 4.0, 20, 20, 64, 500, 0),
    entity.Enemy(enemy_image_sheet_type_0, 700, 100, 4.0, 20, 20, 64, 500, 0),
    entity.Enemy(enemy_image_sheet_type_0, 200, 250, 4.0, 20, 20, 64, 500, 0),
    entity.Enemy(enemy_image_sheet_type_0, 600, 250, 4.0, 20, 20, 64, 500, 0),
    entity.Enemy(enemy_image_sheet_type_0, 100, 500, 4.0, 20, 20, 64, 500, 0),
    entity.Enemy(enemy_image_sheet_type_0, 700, 500, 4.0, 20, 20, 64, 500, 0),
]
room_2_walls = [
    Room.Wall(400, 100, 10, 400, True),
]
room_2_chests = [
    Room.Chest(410, 250, chest_array[1], True)
]
room_2 = Room.Room(room_2_enemies, room_2_chests, room_2_walls, [])

# ROOM 3
room_3_enemies = [
    entity.Enemy(enemy_image_sheet_type_0, 370, 270, 2.5, 1000, 50, 64, 500, 0),
]
room_3_walls = [
    Room.Wall(0, 240, 350, 10, False),
    Room.Wall(100, 350, 250, 10, False),
    Room.Wall(340, 100, 10, 150, True),
    Room.Wall(450, 0, 10, 250, True),
    Room.Wall(450, 240, 250, 10, False),
    Room.Wall(450, 350, 350, 10, False),
    Room.Wall(340, 350, 10, 250, True),
    Room.Wall(450, 350, 10, 150, True),
]
room_3_chests = [
    Room.Chest(550, 10, chest_array[2], False)
]
room_3 = Room.Room(room_3_enemies, room_3_chests, room_3_walls, [])

# ROOM 4
room_4_enemies = [
    entity.Enemy(enemy_image_sheet_type_1, 10, 10, 2.5, 30, 50, 500, 500, 1),
    entity.Enemy(enemy_image_sheet_type_1, 340, 240, 2.5, 30, 50, 500, 500, 1),
    entity.Enemy(enemy_image_sheet_type_1, 10, 520, 2.5, 30, 50, 500, 500, 1),
    entity.Enemy(enemy_image_sheet_type_1, 340, 290, 2.5, 30, 50, 500, 500, 1),
    entity.Enemy(enemy_image_sheet_type_1, 720, 520, 2.5, 30, 50, 500, 500, 1),
    entity.Enemy(enemy_image_sheet_type_1, 390, 290, 2.5, 30, 50, 500, 500, 1),
    entity.Enemy(enemy_image_sheet_type_1, 720, 10, 2.5, 30, 50, 500, 500, 1),
    entity.Enemy(enemy_image_sheet_type_1, 390, 240, 2.5, 30, 50, 500, 500, 1),


]
room_4_walls = [
    Room.Wall(395, 250, 10, 100, True),
    Room.Wall(350, 295, 100, 10, False),
]
room_4_chests = [
]
room_4 = Room.Room(room_4_enemies, room_4_chests, room_4_walls, [])

# ROOM 5
room_5_enemies = [
    entity.Enemy(enemy_image_sheet_type_0, 20, 20, 1.8, 100, 50, 64, 500, 0),
    entity.Enemy(enemy_image_sheet_type_0, 120, 20, 1.8, 100, 50, 64, 500, 0),
    entity.Enemy(enemy_image_sheet_type_0, 220, 20, 1.8, 100, 50, 64, 500, 0),
    entity.Enemy(enemy_image_sheet_type_0, 520, 20, 1.8, 100, 50, 64, 500, 0),
    entity.Enemy(enemy_image_sheet_type_0, 620, 20, 1.8, 100, 50, 64, 500, 0),
    entity.Enemy(enemy_image_sheet_type_0, 720, 20, 1.8, 100, 50, 64, 200, 0),
    entity.Enemy(enemy_image_sheet_type_0, 20, 520, 1.8, 100, 50, 64, 500, 0),
    entity.Enemy(enemy_image_sheet_type_0, 120, 520, 1.8, 100, 50, 64, 500, 0),
    entity.Enemy(enemy_image_sheet_type_0, 220, 520, 1.8, 100, 50, 64, 500, 0),
    entity.Enemy(enemy_image_sheet_type_0, 520, 520, 1.8, 100, 50, 64, 500, 0),
    entity.Enemy(enemy_image_sheet_type_0, 620, 520, 1.8, 100, 50, 64, 500, 0),
    entity.Enemy(enemy_image_sheet_type_0, 720, 520, 1.8, 100, 50, 64, 200, 0),

]
room_5_walls = [
    Room.Wall(95, 370, 10, 230, True),
    Room.Wall(195, 370, 10, 230, True),
    Room.Wall(295, 370, 10, 230, True),
    Room.Wall(495, 370, 10, 230, True),
    Room.Wall(595, 370, 10, 230, True),
    Room.Wall(695, 370, 10, 230, True),

    Room.Wall(95, 0, 10, 230, True),
    Room.Wall(195, 0, 10, 230, True),
    Room.Wall(295, 0, 10, 230, True),
    Room.Wall(495, 0, 10, 230, True),
    Room.Wall(595, 0, 10, 230, True),
    Room.Wall(695, 0, 10, 230, True),

]
room_5 = Room.Room(room_5_enemies, [], room_5_walls, [])

rooms = [room_1, room_2, room_3, room_4, room_5]
CURRENT_ROOM = None
