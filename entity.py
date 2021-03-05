import pygame


# Entity object
class Entity(object):

    def __init__(self, s_prite, current_x, current_y, speed, X_change, Y_change,
                 health, attack_power):
        self.SPRITE = s_prite
        self.CURRENT_X = current_x + 100
        self.CURRENT_Y = current_y + 100
        self.SPEED = speed
        self.X_change = X_change
        self.Y_change = Y_change
        self.init_HEALTH = health
        self.HEALTH = health
        self.ATTACK_POWER = attack_power
        self.entity_moving_X = False
        self.entity_moving_Y = False
        self.X_move_direction = "None"
        self.Y_move_direction = "down"
        self.X_faced_direction = "None"
        self.Y_faced_direction = "down"
        self.facing = "y"
        self.ATTACKING = False

    def get_SPRITE(self):
        return self.SPRITE

    def set_SPRITE(self, image):
        self.SPRITE = image

    def get_CURRENT_X(self):
        return self.CURRENT_X

    def set_CURRENT_X(self, x):
        self.CURRENT_X = x

    def get_CURRENT_Y(self):
        return self.CURRENT_Y

    def set_CURRENT_Y(self, y):
        self.CURRENT_Y = y

    def get_init_HEALTH(self):
        return self.init_HEALTH

    def get_HEALTH(self):
        return self.HEALTH

    def set_HEALTH(self, health):
        self.HEALTH = health

    def get_ATTACK_POWER(self):
        return self.ATTACK_POWER

    def set_ATTACK_POWER(self, attack_power):
        self.ATTACK_POWER = attack_power

    def get_speed(self):
        return self.SPEED

    def set_speed(self, speed):
        self.SPEED = speed

    def get_entity_moving_X(self):
        return self.entity_moving_X

    def set_entity_moving_X(self, moving):
        self.entity_moving_X = moving

    def get_entity_moving_Y(self):
        return self.entity_moving_Y

    def set_entity_moving_Y(self, moving):
        self.entity_moving_Y = moving

    def get_X_move_direction(self):
        return self.X_move_direction

    def set_X_move_directon(self, direction):
        self.X_move_direction = direction

    def get_Y_move_direction(self):
        return self.Y_move_direction

    def set_Y_move_directon(self, direction):
        self.Y_move_direction = direction

    def get_X_faced_direction(self):
        return self.X_faced_direction

    def set_X_faced_directon(self, direction):
        self.X_faced_direction = direction

    def get_Y_faced_direction(self):
        return self.Y_faced_direction

    def set_Y_faced_directon(self, direction):
        self.Y_faced_direction = direction

    def get_facing(self):
        return self.facing

    def set_facing(self, direction):
        self.facing = direction

    def stop_X(self):
        self.X_change = 0

    def stop_Y(self):
        self.Y_change = 0

    def update(self):
        self.CURRENT_X += self.X_change
        self.CURRENT_Y += self.Y_change
        if self.CURRENT_X < 100:  # 0
            self.CURRENT_X = 100  # 0
        elif self.CURRENT_X > 836:  # 736
            self.CURRENT_X = 836  # 736

        if self.CURRENT_Y < 100:  # 0
            self.CURRENT_Y = 100  # 0
        elif self.CURRENT_Y > 636:  # 536
            self.CURRENT_Y = 636  # 536

    def Move_Left(self):
        self.X_change = 0
        self.X_change -= self.SPEED

    def Move_Right(self):
        self.X_change = 0
        self.X_change += self.SPEED

    def Move_UP(self):
        self.Y_change = 0
        self.Y_change -= self.SPEED

    def Move_Down(self):
        self.Y_change = 0
        self.Y_change += self.SPEED

    def set_ATTACKING(self, attacking):
        self.ATTACKING = attacking

    def get_ATTACKING(self):
        return self.ATTACKING


# Player object
class Player(Entity):

    def __init__(self, s_prite, current_x, current_y):
        self.INVENTORY = []
        self.CURRENT_ITEM = 'gun'
        super().__init__(s_prite, current_x, current_y, 3.5, 0, 0, 200, 10)

    def stop_X(self):
        super().stop_X()

    def stop_Y(self):
        super().stop_Y()

    def Move_Left(self):
        super().Move_Left()

    def Move_Right(self):
        super().Move_Right()

    def Move_UP(self):
        super().Move_UP()

    def Move_Down(self):
        super().Move_Down()

    def update(self):
        super().update()


# Enemy object
# Agro range?
class Enemy(Entity):

    def __init__(self, s_prite, current_x, current_y, speed, health,
                 attack_power, attack_range, agro_range, enemy_type):
        self.AGRO_RANGE = agro_range
        self.ATTACK_RANGE = attack_range
        self.ENEMY_TYPE = enemy_type
        super().__init__(s_prite, current_x, current_y, speed, 0, 0, health, attack_power)

    def get_ATTACK_RANGE(self):
        return self.ATTACK_RANGE

    def set_ATTACK_RANGE(self, attack_range):
        self.ATTACK_RANGE = attack_range

    def get_AGRO_RANGE(self):
        return self.AGRO_RANGE

    def set_AGRO_RANGE(self, agro_range):
        pass

    def get_ENEMY_TYPE(self):
        return self.ENEMY_TYPE

    def stop_X(self):
        super().stop_X()

    def stop_Y(self):
        super().stop_Y()

    def Move_Left(self):
        super().Move_Left()

    def Move_Right(self):
        super().Move_Right()

    def Move_UP(self):
        super().Move_UP()

    def Move_Down(self):
        super().Move_Down()

    def update(self):
        super().update()


class SpriteSheet(object):

    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name)
        self.image = "none"

    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        image.set_colorkey((0, 0, 0))

        self.image = image
        return image
