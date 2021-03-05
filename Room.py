import pygame
import item


class Room(object):

    def __init__(self, enemies, chests, walls, bullets):
        self.enemies = enemies
        self.doors = []
        self.chests = chests
        self.walls = walls
        self.bullets = bullets
        self.plot = []

    def get_enemies(self):
        return self.enemies

    def get_doors(self):
        return self.doors

    def get_chests(self):
        return self.chests

    def get_walls(self):
        return self.walls

    def set_plot(self, plot):
        self.plot = plot

    def add_bullet(self, bullet):
        self.bullets.append(bullet)


class Door(object):

    def __init__(self, X_1, Y_1, X_2, Y_2, room_1, room_2):
        self.X_1 = X_1 + 100
        self.Y_1 = Y_1 + 100
        self.X_2 = X_2 + 100
        self.Y_2 = Y_2 + 100
        self.room_1 = room_1
        self.room_2 = room_2
        self.current_room = ""

    def change_room(self):
        if self.current_room == "one":
            return self.room_2
        if self.current_room == "two":
            return self.room_1


class Chest(object):
    def __init__(self, X, Y, items, is_verticql):
        self.X = X + 100
        self.Y = Y + 100
        self.items = items
        self.is_open = False
        self.is_vertical = is_verticql
        self.chest_slots = []

    def toggle_chest(self):
        if self.is_open:
            self.is_open = False
            self.chest_slots = []
        else:
            self.is_open = True
            self.create_chest_slots()

    def remove_Item(self):
        items = ['Assets/Items/health_potion.png', 'Assets/Items/red_bullet.png',
                 'Assets/Items/blue_bullet.png', 'Assets/Items/purple_bullet.png',
                 'Assets/Items/key.png']
        for i in self.chest_slots:
            if self.slot_mouse_over() != None:
                if i == self.slot_mouse_over():
                    for j in range(0, 5):
                        if i.item_str == items[j]:
                            self.items[j] = 0
                            slot = item.Slot(i.x, i.y)
                            self.chest_slots[j] = slot
                            break
                    break

    def create_chest_slots(self):
        items = ['Assets/Items/health_potion.png', 'Assets/Items/red_bullet.png',
                 'Assets/Items/blue_bullet.png', 'Assets/Items/purple_bullet.png',
                 'Assets/Items/key.png']
        chest_item = []
        chest_counts = []
        for i in range(0, 5):
            if (self.items[i] > 0):
                chest_item.append(items[i])
                chest_counts.append(self.items[i])

        for i in range(0, 5):
            slot = item.Slot(self.X + i * 42 + 2, self.Y + 2)
            if i < len(chest_item):
                image = pygame.image.load(chest_item[i])
                slot.item = image
                slot.item_str = chest_item[i]
                slot.itemCount = chest_counts[i]
            self.chest_slots.append(slot)

    def draw_chest_slot(self, screen):
        pygame.draw.rect(screen, (1, 1, 1), (self.X, self.Y, 5 * 42 + 2, 44))
        if (self.slot_mouse_over() != None):
            slot = self.slot_mouse_over()
            x = slot.x - 2
            y = slot.y - 2
            pygame.draw.rect(screen, (255, 255, 100), (x, y, 44, 44))

        for i in self.chest_slots:
            i.draw_Slot(screen)

    def slot_mouse_over(self):
        pos_X, pos_Y = pygame.mouse.get_pos()
        for i in self.chest_slots:
            if i.x < pos_X and i.x + 40 > pos_X:
                if i.y < pos_Y and i.y + 40 > pos_Y:
                    return i
        return None

    def draw_chest(self, screen):
        if self.is_vertical:
            pygame.draw.rect(screen, (1, 1, 1), (self.X, self.Y, 50, 100))
            pygame.draw.rect(screen, (153, 101, 21), (self.X + 5, self.Y + 5, 40, 90))
            pygame.draw.rect(screen, (1, 1, 1), (self.X + 5, self.Y + 5, 40, 5))
            pygame.draw.rect(screen, (1, 1, 1), (self.X + 5, self.Y + 90, 40, 3))
            pygame.draw.rect(screen, (255, 223, 0), (self.X + 5, self.Y + 5, 40, 3))
            pygame.draw.rect(screen, (255, 223, 0), (self.X + 5, self.Y + 92, 40, 3))
            pygame.draw.rect(screen, (1, 1, 1), (self.X + 3, self.Y + 44, 12, 12))
            pygame.draw.rect(screen, (1, 1, 1), (self.X + 35, self.Y + 44, 12, 12))
            pygame.draw.rect(screen, (255, 223, 0), (self.X + 5, self.Y + 46, 8, 8))
            pygame.draw.rect(screen, (255, 223, 0), (self.X + 37, self.Y + 46, 8, 8))
        else:
            pygame.draw.rect(screen, (1, 1, 1), (self.X, self.Y, 100, 50))
            pygame.draw.rect(screen, (153, 101, 21), (self.X + 5, self.Y + 5, 90, 40))
            pygame.draw.rect(screen, (1, 1, 1), (self.X + 5, self.Y + 5, 5, 40))
            pygame.draw.rect(screen, (1, 1, 1), (self.X + 90, self.Y + 5, 3, 40))
            pygame.draw.rect(screen, (255, 223, 0), (self.X + 5, self.Y + 5, 3, 40))
            pygame.draw.rect(screen, (255, 223, 0), (self.X + 92, self.Y + 5, 3, 40))
            pygame.draw.rect(screen, (1, 1, 1), (self.X + 44, self.Y + 3, 12, 12))
            pygame.draw.rect(screen, (1, 1, 1), (self.X + 44, self.Y + 35, 12, 12))
            pygame.draw.rect(screen, (255, 223, 0), (self.X + 46, self.Y + 5, 8, 8))
            pygame.draw.rect(screen, (255, 223, 0), (self.X + 46, self.Y + 37, 8, 8))


class Wall(object):
    def __init__(self, X, Y, width, height, vertical):
        self.X = X + 100
        self.Y = Y + 100
        self.width = width
        self.height = height
        self.vertical = vertical
        self.rect = pygame.Rect(X, Y, width, height)

    def get_X(self):
        return self.X

    def get_Y(self):
        return self.Y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_vertical(self):
        return self.vertical


class Bullet(object):
    def __init__(self, X, Y, X_speed, Y_speed, damage, attack_range, go_X, go_Y, bullet_type):
        self.init_X = X
        self.init_Y = Y
        self.X = X
        self.Y = Y
        self.X_SPEED = X_speed
        self.Y_SPEED = Y_speed
        self.DAMAGE = damage
        self.ATTACK_RANGE = attack_range
        self.go_X = go_X
        self.go_Y = go_Y
        self.bullet_owner = None
        self.bullet_type = bullet_type

    def get_X(self):
        return self.X

    def get_Y(self):
        return self.Y

    def get_init_X(self):
        return self.init_X

    def get_init_Y(self):
        return self.init_Y

    def set_go_X(self, bool_X):
        self.go_X = bool_X

    def set_go_Y(self, bool_Y):
        self.go_Y = bool_Y

    def get_damage(self):
        return self.DAMAGE

    def bullet_move(self):
        if self.go_X:
            self.X = self.X + self.X_SPEED
        if self.go_Y:
            self.Y = self.Y + self.Y_SPEED
