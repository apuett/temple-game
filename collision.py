import math
import entity
import Room_Data


def check_wall_collision(entity_obj):
    entity_X = entity_obj.CURRENT_X + 32
    entity_Y = entity_obj.CURRENT_Y + 32
    num = 32
    if isinstance(entity_obj, entity.Enemy):
        num = 12
    for i in Room_Data.CURRENT_ROOM.walls:
        if i.get_Y() - num < entity_Y < i.get_Y() + i.get_height() + num:
            if abs(entity_X - i.get_X() + 32) < 5:
                if not entity_obj.X_move_direction == "left":
                    entity_obj.set_CURRENT_X(i.get_X() - 64)
            if abs(entity_obj.CURRENT_X - (i.get_X() + i.get_width())) < 5:
                if not entity_obj.X_move_direction == "right":
                    entity_obj.set_CURRENT_X(i.get_X() + i.get_width())

        if i.get_X() - num < entity_X < i.get_X() + i.get_width() + num:
            if abs(entity_Y - i.get_Y() + 32) < 5:
                if not entity_obj.Y_move_direction == "up":
                    entity_obj.set_CURRENT_Y(i.get_Y() - 64)
            if abs(entity_obj.CURRENT_Y - (i.get_Y() + i.get_height())) < 5:
                if not entity_obj.Y_move_direction == "down":
                    entity_obj.set_CURRENT_Y(i.get_Y() + i.get_height())


def check_entity_collision(entity_obj, player1):
    entity_X = entity_obj.CURRENT_X + 32
    entity_Y = entity_obj.CURRENT_Y + 32
    for i in Room_Data.CURRENT_ROOM.enemies:
        i_X = i.get_CURRENT_X() + 32
        i_Y = i.get_CURRENT_Y() + 32
        dist_apart = math.sqrt((math.pow(i_X - entity_X, 2))
                               + (math.pow(i_Y - entity_Y, 2)))

        if dist_apart < 32:
            if 0 <= entity_X - i_X < 16:
                entity_obj.set_CURRENT_X(i.get_CURRENT_X() + 16)
            if 0 <= i_X - entity_X < 16:
                entity_obj.set_CURRENT_X(i.get_CURRENT_X() - 16)

            if 0 <= entity_Y - i_Y < 16:
                entity_obj.set_CURRENT_Y(i.get_CURRENT_Y() + 16)
            if 0 <= i_Y - entity_Y < 16:
                entity_obj.set_CURRENT_Y(i.get_CURRENT_Y() - 16)

        p_X = player1.get_CURRENT_X() + 32
        p_Y = player1.get_CURRENT_Y() + 32
        dist_apart = math.sqrt((math.pow(p_X - entity_X, 2))
                               + (math.pow(p_Y - entity_Y, 2)))
        if dist_apart < 32:
            if 0 <= entity_X - p_X < 16:
                entity_obj.set_CURRENT_X(player1.get_CURRENT_X() + 16)
            if 0 <= p_X - entity_X < 16:
                entity_obj.set_CURRENT_X(player1.get_CURRENT_X() - 16)

            if 0 <= entity_Y - p_Y < 16:
                entity_obj.set_CURRENT_Y(player1.get_CURRENT_Y() + 16)
            if 0 <= p_Y - entity_Y < 16:
                entity_obj.set_CURRENT_Y(player1.get_CURRENT_Y() - 16)


def check_bullet_collision(entity):
    for i in Room_Data.CURRENT_ROOM.bullets:
        if not i.bullet_owner == entity:
            en_X = entity.get_CURRENT_X() + 32
            en_Y = entity.get_CURRENT_Y() + 32
            dist = math.sqrt(math.pow(i.get_X() - en_X, 2) +
                             math.pow(i.get_Y() - en_Y, 2))
            if dist < 32:
                entity.set_HEALTH(entity.get_HEALTH() - i.get_damage())
                Room_Data.CURRENT_ROOM.bullets.remove(i)
