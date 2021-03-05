import entity
import math
import Room_Data
import Room


# Creates Animation
def entity_animation(screen, entity_obj, frame):
    isenemy = False
    if isinstance(entity_obj, entity.Enemy):
        isenemy = True
    entity_obj.update()
    x = entity_obj.CURRENT_X
    y = entity_obj.CURRENT_Y
    entity_Img_sheet = entity_obj.get_SPRITE()
    num = frame * 64
    if not entity_obj.entity_moving_X and not entity_obj.entity_moving_Y:
        num = 0
    if entity_obj.entity_moving_X and entity_obj.entity_moving_Y:
        entity_obj.set_facing("xy")
    if entity_obj.get_facing() == "y":
        if entity_obj.get_Y_faced_direction() == "down":
            entity_Img = entity_Img_sheet.get_image(num, 0, 64, 64)
        if entity_obj.get_Y_faced_direction() == "up":
            entity_Img = entity_Img_sheet.get_image(num, 64, 64, 64)
    elif entity_obj.get_facing() == "x":
        if entity_obj.get_X_faced_direction() == "right" and not entity_obj.entity_moving_Y:
            entity_Img = entity_Img_sheet.get_image(num, 64 * 2, 64, 64)
        if entity_obj.get_X_faced_direction() == "left" and not entity_obj.entity_moving_Y:
            entity_Img = entity_Img_sheet.get_image(num, 64 * 3, 64, 64)
    else:
        if entity_obj.get_X_faced_direction() == "right":
            if entity_obj.get_Y_faced_direction() == "down":
                entity_Img = entity_Img_sheet.get_image(num, 64 * 4, 64, 64)
            else:
                entity_Img = entity_Img_sheet.get_image(num, 64 * 6, 64, 64)
        else:
            if entity_obj.get_Y_faced_direction() == "up":
                entity_Img = entity_Img_sheet.get_image(num, 64 * 5, 64, 64)
            else:
                entity_Img = entity_Img_sheet.get_image(num, 64 * 7, 64, 64)
    if entity_obj.get_ATTACKING():
        entity_Img = entity_Img_sheet.get_image(0, 64 * 8, 64, 64)
        entity_obj.set_ATTACKING(False)

    screen.blit(entity_Img, (x, y))


def enemy_movements(enemy, player1, frames):
    dist_from_player = math.sqrt((math.pow(enemy.get_CURRENT_X() - player1.get_CURRENT_X(), 2))
                                 + (math.pow(enemy.get_CURRENT_Y() - player1.get_CURRENT_Y(), 2)))

    if dist_from_player < enemy.get_AGRO_RANGE():
        if not detect_wall(enemy, player1):
            if enemy.get_ENEMY_TYPE() == 0:
                if abs(enemy.get_CURRENT_X() - player1.get_CURRENT_X()) > 32:
                    if player1.get_CURRENT_X() < enemy.get_CURRENT_X():
                        enemy.Move_Left()
                        enemy.set_entity_moving_X(True)
                        enemy.set_X_move_directon("left")
                        enemy.set_X_faced_directon("left")
                        if not enemy.entity_moving_Y:
                            enemy.set_facing("x")
                    elif player1.get_CURRENT_X() > enemy.get_CURRENT_X():
                        enemy.Move_Right()
                        enemy.set_entity_moving_X(True)
                        enemy.set_X_move_directon("right")
                        enemy.set_X_faced_directon("right")
                        if not enemy.entity_moving_Y:
                            enemy.set_facing("x")
                    else:
                        enemy.stop_X()
                        enemy.set_entity_moving_X(False)
                else:
                    enemy.stop_X()
                    enemy.set_entity_moving_X(False)

                if abs(enemy.get_CURRENT_Y() - player1.get_CURRENT_Y()) > 32:
                    if player1.get_CURRENT_Y() < enemy.get_CURRENT_Y():
                        enemy.Move_UP()
                        enemy.set_entity_moving_Y(True)
                        enemy.set_Y_move_directon("up")
                        enemy.set_Y_faced_directon("up")
                        enemy.set_facing("y")
                    elif enemy.get_CURRENT_Y() < player1.get_CURRENT_Y():
                        enemy.Move_Down()
                        enemy.set_entity_moving_Y(True)
                        enemy.set_Y_move_directon("down")
                        enemy.set_Y_faced_directon("down")
                        enemy.set_facing("y")
                    else:
                        enemy.stop_Y()
                        enemy.set_entity_moving_Y(False)
                        if enemy.entity_moving_X:
                            enemy.set_facing("x")
                else:
                    enemy.stop_Y()
                    enemy.set_entity_moving_Y(False)

                if dist_from_player < enemy.get_ATTACK_RANGE() and 0 <= frames % 100 <= 10:
                    enemy.set_ATTACKING(True)
                    if frames % 100 == 1:
                        player1.set_HEALTH(player1.get_HEALTH() - enemy.get_ATTACK_POWER())
                    if player1.get_CURRENT_X() > enemy.get_CURRENT_X():
                        player1.set_CURRENT_X(player1.get_CURRENT_X() + 6)
                    elif player1.get_CURRENT_X() < enemy.get_CURRENT_X():
                        player1.set_CURRENT_X(player1.get_CURRENT_X() - 6)
                    if player1.get_CURRENT_Y() > enemy.get_CURRENT_Y():
                        player1.set_CURRENT_Y(player1.get_CURRENT_Y() + 6)
                    elif player1.get_CURRENT_Y() < enemy.get_CURRENT_Y():
                        player1.set_CURRENT_Y(player1.get_CURRENT_Y() - 6)

            if enemy.get_ENEMY_TYPE() == 1:
                if frames % 100 == 1:
                    pos_X = player1.get_CURRENT_X()
                    pos_Y = player1.get_CURRENT_Y()

                    hypot = math.sqrt(math.pow(pos_X - enemy.CURRENT_X, 2) + math.pow(pos_Y - enemy.CURRENT_Y, 2))
                    mouse_angle = math.asin((pos_X - enemy.CURRENT_X) / hypot)
                    mouse_angle = mouse_angle * (180 / math.pi)

                    time = hypot / 15
                    X_speed = (pos_X - enemy.get_CURRENT_X()) / time
                    Y_speed = (pos_Y - enemy.get_CURRENT_Y()) / time

                    if -22.5 <= mouse_angle < 22.5 and pos_Y < enemy.CURRENT_Y:
                        enemy.set_facing('y')
                        enemy.set_Y_faced_directon('up')

                        bullet = Room.Bullet(enemy.CURRENT_X + 32, enemy.CURRENT_Y + 32, X_speed, Y_speed, 10,
                                             enemy.get_ATTACK_RANGE(), True, True, 0)
                    elif 22.5 <= mouse_angle < 67.5 and pos_Y < enemy.CURRENT_Y:
                        enemy.set_facing('xy')
                        enemy.set_X_faced_directon('right')
                        enemy.set_Y_faced_directon('up')
                        bullet = Room.Bullet(enemy.CURRENT_X + 32, enemy.CURRENT_Y + 32, X_speed, Y_speed, 10,
                                             enemy.get_ATTACK_RANGE(), True, True, 0)
                    elif 67.5 <= mouse_angle:
                        enemy.set_facing('x')
                        enemy.set_X_faced_directon('right')
                        enemy.set_entity_moving_Y(False)

                        bullet = Room.Bullet(enemy.CURRENT_X + 32, enemy.CURRENT_Y + 32, X_speed, Y_speed, 10,
                                             enemy.get_ATTACK_RANGE(), True, True, 0)
                    elif 22.5 <= mouse_angle < 67.5 and pos_Y > enemy.CURRENT_Y:
                        enemy.set_facing('xy')
                        enemy.set_X_faced_directon('right')
                        enemy.set_Y_faced_directon('down')
                        bullet = Room.Bullet(enemy.CURRENT_X + 32, enemy.CURRENT_Y + 32, X_speed, Y_speed, 10,
                                             enemy.get_ATTACK_RANGE(), True, True, 0)
                    elif -22.5 <= mouse_angle < 22.5 and pos_Y > enemy.CURRENT_Y:
                        enemy.set_facing('y')
                        enemy.set_Y_faced_directon('down')
                        bullet = Room.Bullet(enemy.CURRENT_X + 32, enemy.CURRENT_Y + 32, X_speed, Y_speed, 10,
                                             enemy.get_ATTACK_RANGE(), True, True, 0)
                    elif -67.5 <= mouse_angle < -22.5 and pos_Y > enemy.CURRENT_Y:
                        enemy.set_facing('xy')
                        enemy.set_Y_faced_directon('down')
                        enemy.set_X_faced_directon('left')
                        bullet = Room.Bullet(enemy.CURRENT_X + 32, enemy.CURRENT_Y + 32, X_speed, Y_speed, 10,
                                             enemy.get_ATTACK_RANGE(), True, True, 0)
                    elif mouse_angle < -67.5:
                        enemy.set_facing('x')
                        enemy.set_X_faced_directon('left')
                        enemy.set_entity_moving_Y(False)
                        bullet = Room.Bullet(enemy.CURRENT_X + 32, enemy.CURRENT_Y + 32, X_speed, Y_speed, 10,
                                             enemy.get_ATTACK_RANGE(), True,
                                             True, 0)
                    elif -67.5 <= mouse_angle < -22.5 and pos_Y < enemy.CURRENT_Y:
                        enemy.set_facing('xy')
                        enemy.set_Y_faced_directon('up')
                        enemy.set_X_faced_directon('left')
                        bullet = Room.Bullet(enemy.CURRENT_X + 32, enemy.CURRENT_Y + 32, X_speed, Y_speed, 10,
                                             enemy.get_ATTACK_RANGE(), True,
                                             True, 0)

                    bullet.bullet_owner = enemy
                    Room_Data.CURRENT_ROOM.add_bullet(bullet)

        else:
            enemy.stop_X()
            enemy.stop_Y()
            enemy.set_entity_moving_Y(False)
            enemy.set_entity_moving_X(False)
    else:
        enemy.stop_X()
        enemy.stop_Y()
        enemy.set_entity_moving_Y(False)
        enemy.set_entity_moving_X(False)


# Flip display 90 degrees counter_clock wise
# Use display_X as Y and display_Y as X
# Pixels as units
def detect_wall(enemy, player):
    wall_in = False
    e_Y = enemy.get_CURRENT_X() + 32.001
    p_Y = player.get_CURRENT_X() + 32
    e_X = enemy.get_CURRENT_Y() + 32.001
    p_X = player.get_CURRENT_Y() + 32
    for i in Room_Data.CURRENT_ROOM.walls:
        if i.get_vertical():
            if not e_X == p_X:
                m = int((e_Y - p_Y) / (e_X - p_X))
                b = int((m * e_X) - e_Y)
                b = 0 - b

                y = i.get_X() + (i.get_width() / 2)
                x = -1
                if not m == 0:
                    x = int((y - b) / m)
                elif e_Y < y < p_Y or p_Y < y < e_Y:
                    wall_in = True
                if i.get_Y() <= x <= i.get_Y() + i.get_height():
                    if e_Y < y < p_Y or p_Y < y < e_Y:
                        wall_in = True

        else:
            if not e_X == p_X:
                m = int((e_Y - p_Y) / (e_X - p_X))
                b = int((m * e_X) - e_Y)
                b = 0 - b

                x = i.get_Y() + (i.get_height() / 2)
                y = int((m * x) + b)
                if i.get_X() <= y <= i.get_X() + i.get_width():
                    if p_X < x < e_X or e_X < x < p_X:
                        wall_in = True
    return wall_in
