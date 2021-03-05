import pygame


class Item(object):

    def __init__(self, icon, attack_power):
        self.icon = icon
        self.ATTACK_POWER = attack_power

    def get_icon(self):
        return self.icon

    def set_icon(self, icon):
        self.icon = icon

    def get_ATTACK_POWER(self):
        return self.ATTACK_POWER

    def set_ATTACK_POWER(self, attack_power):
        self.ATTACK_POWER = attack_power


class Slot(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.item = None
        self.itemCount = 0
        self.item_str = None

    def add_Item(self, slot):
        self.itemCount = self.itemCount + slot.itemCount

    def remove_Item(self):
        self.itemCount = 0
        self.item_str = None
        self.item = None

    def draw_Slot(self, screen):
        pygame.draw.rect(screen, (200, 200, 200), (self.x, self.y, 40, 40))

        if self.item != None:
            screen.blit(self.item, (self.x + 4, self.y + 4))

        font = pygame.font.Font('freesansbold.ttf', 12)
        count = font.render(str(self.itemCount), True, (5, 5, 5))
        screen.blit(count, (self.x + 25, self.y + 27))
