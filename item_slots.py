import item
import pygame
import Room_Data

invetory_slots = []
selected_islot = 0
chest_open = False

items = ['Assets/Items/black_bullet.png', 'Assets/Items/health_potion.png',
         'Assets/Items/red_bullet.png', 'Assets/Items/blue_bullet.png',
         'Assets/Items/purple_bullet.png', 'Assets/Items/key.png']


def create_slots():
    for i in range(0, 6):
        slot = item.Slot(i * 42 + 600, 30)
        image = pygame.image.load(items[i])
        slot.item = image
        slot.item_str = items[i]
        invetory_slots.append(slot)
    invetory_slots[0].itemCount = 99
    invetory_slots[1].itemCount = 3


def draw_inventory_slots(screen):
    pygame.draw.rect(screen, (1, 1, 1), (598, 28, 6 * 42 + 2, 44))
    pygame.draw.rect(screen, (255, 255, 100), (selected_islot * 42 + 598, 28, 44, 44))
    for i in invetory_slots:
        i.draw_Slot(screen)


def create_chest_slots():
    for i in Room_Data.CURRENT_ROOM.chests:
        i.create_chest_slots()


def draw_chest_slots(screen):
    for i in Room_Data.CURRENT_ROOM.chests:
        if i.is_open:
            chest_open = True
            if (i.slot_mouse_over() != None):
                slot = i.slot_mouse_over()
                x = slot.x - 2
                y = slot.y - 2
                pygame.draw.rect(screen, (255, 255, 100), (x, y, 44, 44))
            i.draw_chest_slot(screen)
            break
        chest_open = False


def set_selected_islot(n):
    global selected_islot
    selected_islot = n
