import pygame
import entity
import Room_Data
import dynamic_rooms
import collision
import item_slots
from Entity_movement import entity_animation
from Entity_movement import enemy_movements
from Key_Inputs import key_inputs
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 25)

pygame.init()

screen = pygame.display.set_mode((1000, 800))

background = pygame.image.load('Assets/Background/temple_room.png').convert()

pygame.display.set_caption("Temple Game")
icon = pygame.image.load('Assets/temple.png')
pygame.display.set_icon(icon)

player_image_sheet = entity.SpriteSheet('Assets/Sprite/Cowboy_Top.png')
player1 = entity.Player(player_image_sheet, 360, 40)

dynamic_rooms.create_plot()
item_slots.create_slots()

font = pygame.font.Font('freesansbold.ttf', 28)


def show_FPS(frames, x, y):
    fps = font.render("FPS: " + str(frames), True, (5, 5, 5))
    screen.blit(fps, (x, y))


# Game Loop
animation_frame = 0
next_frame = pygame.time.get_ticks()
timer = pygame.time.get_ticks()
clock = pygame.time.Clock()
fps = 0
game_frames = 0
running = True
while running:
    screen.fill((211, 211, 211))

    screen.blit(background, (0, 0))

    dynamic_rooms.create_Room(screen)
    item_slots.draw_inventory_slots(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        key_inputs(event, player1)

    if pygame.time.get_ticks() > next_frame:
        animation_frame = (animation_frame + 1) % 3
        next_frame += 100

    game_frames += 1
    if pygame.time.get_ticks() - timer > 1000:
        timer += 1000
        fps = game_frames
        game_frames = 0

    entity_animation(screen, player1, animation_frame)
    pygame.draw.rect(screen, (202, 0, 0),
                     [round(player1.get_CURRENT_X()) + 12, round(player1.get_CURRENT_Y()) + 64, 40, 3])
    pygame.draw.rect(screen, (18, 155, 41), [round(player1.get_CURRENT_X()) + 12, round(player1.get_CURRENT_Y()) + 64,
                                             round(player1.get_HEALTH() / player1.get_init_HEALTH() * 40), 3])
    if player1.get_HEALTH() <= 0:
        print("Player dead")
        running = False
        break

    for i in Room_Data.CURRENT_ROOM.enemies:
        enemy_movements(i, player1, game_frames)
        entity_animation(screen, i, animation_frame)
        collision.check_wall_collision(i)
        collision.check_entity_collision(i, player1)
        collision.check_bullet_collision(i)
        if i.get_HEALTH() <= 0:
            Room_Data.CURRENT_ROOM.enemies.remove(i)
        pygame.draw.rect(screen, (202, 0, 0), [round(i.get_CURRENT_X()) + 12, round(i.get_CURRENT_Y()) + 64, 40, 3])
        pygame.draw.rect(screen, (18, 155, 41), [round(i.get_CURRENT_X()) + 12, round(i.get_CURRENT_Y()) + 64,
                                                 round(i.get_HEALTH() / i.get_init_HEALTH() * 40), 3])

    collision.check_bullet_collision(player1)
    collision.check_wall_collision(player1)
    item_slots.draw_chest_slots(screen)
    show_FPS(fps, 50, 15)

    clock.tick(100)
    pygame.display.update()
