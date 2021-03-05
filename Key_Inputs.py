import pygame
import math
import Room_Data
import Room
import item_slots


# key inputs
def key_inputs(event, player):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            player.Move_Left()
            player.set_entity_moving_X(True)
            player.set_X_move_directon("left")
            player.set_X_faced_directon("left")
            if not player.entity_moving_Y:
                player.set_facing("x")
        if event.key == pygame.K_d:
            player.Move_Right()
            player.set_entity_moving_X(True)
            player.set_X_move_directon("right")
            player.set_X_faced_directon("right")
            if not player.entity_moving_Y:
                player.set_facing("x")
        if event.key == pygame.K_w:
            player.Move_UP()
            player.set_entity_moving_Y(True)
            player.set_Y_move_directon("up")
            player.set_Y_faced_directon("up")
            player.set_facing("y")
        if event.key == pygame.K_s:
            player.Move_Down()
            player.set_entity_moving_Y(True)
            player.set_Y_move_directon("down")
            player.set_Y_faced_directon("down")
            player.set_facing("y")

        if event.key == pygame.K_SPACE:
            for i in Room_Data.CURRENT_ROOM.chests:
                if (i.is_vertical):
                    chest_X = i.X + 25
                    chest_Y = i.Y + 50
                else:
                    chest_X = i.X + 50
                    chest_Y = i.Y + 25
                cd = math.sqrt((math.pow(chest_X - (player.get_CURRENT_X() + 32), 2))
                               + (math.pow(chest_Y - (player.get_CURRENT_Y() + 32), 2)))
                if (cd < 50):
                    i.toggle_chest()

            if len(Room_Data.CURRENT_ROOM.enemies) == 0:
                for i in Room_Data.CURRENT_ROOM.doors:
                    if i[0].current_room == "one":
                        door_X = i[0].X_1
                        door_Y = i[0].Y_1
                    if i[0].current_room == "two":
                        door_X = i[0].X_2
                        door_Y = i[0].Y_2
                    d = math.sqrt((math.pow(door_X - player.get_CURRENT_X(), 2))
                                  + (math.pow(door_Y - player.get_CURRENT_Y(), 2)))
                    if d < 100:
                        Room_Data.CURRENT_ROOM = i[0].change_room()
                        if i[0].current_room == "one":
                            player.set_CURRENT_X(i[0].X_2)
                            player.set_CURRENT_Y(i[0].Y_2)
                            break
                        if i[0].current_room == "two":
                            player.set_CURRENT_X(i[0].X_1)
                            player.set_CURRENT_Y(i[0].Y_1)
                            break

        if event.key == pygame.K_LEFT:
            if item_slots.selected_islot > 0:
                item_slots.set_selected_islot(item_slots.selected_islot - 1)

        if event.key == pygame.K_RIGHT:
            if item_slots.selected_islot < 4:
                item_slots.set_selected_islot(item_slots.selected_islot + 1)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a and player.get_X_move_direction() == "left":
            player.stop_X()
            player.set_entity_moving_X(False)
            if player.entity_moving_Y:
                player.set_facing("y")
        if event.key == pygame.K_d and player.get_X_move_direction() == "right":
            player.stop_X()
            player.set_entity_moving_X(False)
            if player.entity_moving_Y:
                player.set_facing("y")
        if event.key == pygame.K_w and player.get_Y_move_direction() == "up":
            player.stop_Y()
            player.set_entity_moving_Y(False)
            if player.entity_moving_X:
                player.set_facing("x")
        if event.key == pygame.K_s and player.get_Y_move_direction() == "down":
            player.stop_Y()
            player.set_entity_moving_Y(False)
            if player.entity_moving_X:
                player.set_facing("x")

    if event.type == pygame.MOUSEBUTTONDOWN:
        over_slot = False
        for i in Room_Data.CURRENT_ROOM.chests:
            if (i.slot_mouse_over() != None):
                over_slot = True
                if over_slot:
                    for j in item_slots.invetory_slots:
                        if j.item_str == i.slot_mouse_over().item_str:
                            j.add_Item(i.slot_mouse_over())
                            i.remove_Item()
                            print(i.items)
        if not over_slot:
            if item_slots.invetory_slots[item_slots.selected_islot].itemCount > 0:
                if item_slots.selected_islot in [0, 2, 3, 4]:
                    pos_X, pos_Y = pygame.mouse.get_pos()
                    pos_X = pos_X - 32
                    pos_Y = pos_Y - 32

                    hypot = math.sqrt(math.pow(pos_X - player.CURRENT_X, 2) + math.pow(pos_Y - player.CURRENT_Y, 2))
                    mouse_angle = math.asin((pos_X - player.CURRENT_X) / hypot)
                    mouse_angle = mouse_angle * (180 / math.pi)
                    bullet_type = 0
                    bullet_damage = 10
                    bullet_attack_range = 200
                    if item_slots.selected_islot == 2:
                        bullet_type = 1
                        bullet_damage = 20
                    if item_slots.selected_islot == 3:
                        bullet_type = 2
                        bullet_attack_range = 400
                    if item_slots.selected_islot == 4:
                        bullet_type = 3
                        bullet_damage = 20
                        bullet_attack_range = 400

                    if -22.5 <= mouse_angle < 22.5 and pos_Y < player.CURRENT_Y:
                        player.set_facing('y')
                        player.set_Y_faced_directon('up')
                        if player.CURRENT_ITEM == 'gun':
                            bullet = Room.Bullet(player.CURRENT_X + 32, player.CURRENT_Y + 32, 10, -10, bullet_damage,
                                                 bullet_attack_range, False, True,
                                                 bullet_type)
                    elif 22.5 <= mouse_angle < 67.5 and pos_Y < player.CURRENT_Y:
                        player.set_facing('xy')
                        player.set_X_faced_directon('right')
                        player.set_Y_faced_directon('up')
                        if player.CURRENT_ITEM == 'gun':
                            bullet = Room.Bullet(player.CURRENT_X + 32, player.CURRENT_Y + 32, 10, -10, bullet_damage,
                                                 bullet_attack_range, True, True,
                                                 bullet_type)
                    elif 67.5 <= mouse_angle:
                        player.set_facing('x')
                        player.set_X_faced_directon('right')
                        player.set_entity_moving_Y(False)
                        if player.CURRENT_ITEM == 'gun':
                            bullet = Room.Bullet(player.CURRENT_X + 32, player.CURRENT_Y + 32, 10, -10, bullet_damage,
                                                 bullet_attack_range, True, False,
                                                 bullet_type)
                    elif 22.5 <= mouse_angle < 67.5 and pos_Y > player.CURRENT_Y:
                        player.set_facing('xy')
                        player.set_X_faced_directon('right')
                        player.set_Y_faced_directon('down')
                        if player.CURRENT_ITEM == 'gun':
                            bullet = Room.Bullet(player.CURRENT_X + 32, player.CURRENT_Y + 32, 10, 10, bullet_damage,
                                                 bullet_attack_range, True, True,
                                                 bullet_type)
                    elif -22.5 <= mouse_angle < 22.5 and pos_Y > player.CURRENT_Y:
                        player.set_facing('y')
                        player.set_Y_faced_directon('down')
                        if player.CURRENT_ITEM == 'gun':
                            bullet = Room.Bullet(player.CURRENT_X + 32, player.CURRENT_Y + 32, 10, 10, bullet_damage,
                                                 bullet_attack_range, False, True,
                                                 bullet_type)
                    elif -67.5 <= mouse_angle < -22.5 and pos_Y > player.CURRENT_Y:
                        player.set_facing('xy')
                        player.set_Y_faced_directon('down')
                        player.set_X_faced_directon('left')
                        if player.CURRENT_ITEM == 'gun':
                            bullet = Room.Bullet(player.CURRENT_X + 32, player.CURRENT_Y + 32, -10, 10, bullet_damage,
                                                 bullet_attack_range, True, True,
                                                 bullet_type)
                    elif mouse_angle < -67.5:
                        player.set_facing('x')
                        player.set_X_faced_directon('left')
                        player.set_entity_moving_Y(False)
                        if player.CURRENT_ITEM == 'gun':
                            bullet = Room.Bullet(player.CURRENT_X + 32, player.CURRENT_Y + 32, -10, -10, bullet_damage,
                                                 bullet_attack_range, True, False,
                                                 bullet_type)
                    elif -67.5 <= mouse_angle < -22.5 and pos_Y < player.CURRENT_Y:
                        player.set_facing('xy')
                        player.set_Y_faced_directon('up')
                        player.set_X_faced_directon('left')
                        if player.CURRENT_ITEM == 'gun':
                            bullet = Room.Bullet(player.CURRENT_X + 32, player.CURRENT_Y + 32, -10, -10, bullet_damage,
                                                 bullet_attack_range, True, True,
                                                 bullet_type)

                    if player.CURRENT_ITEM == 'gun':
                        bullet.bullet_owner = player
                        Room_Data.CURRENT_ROOM.add_bullet(bullet)
                    if item_slots.selected_islot != 0:
                        item_slots.invetory_slots[item_slots.selected_islot].itemCount = item_slots.invetory_slots[
                                                                                             item_slots.selected_islot].itemCount - 1

                else:
                    player.set_HEALTH(player.get_HEALTH() + 50)
                    if player.get_HEALTH() > 200:
                        player.set_HEALTH(200)
                    item_slots.invetory_slots[item_slots.selected_islot].itemCount = item_slots.invetory_slots[
                                                                                         item_slots.selected_islot].itemCount - 1
