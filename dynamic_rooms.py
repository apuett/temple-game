import Room_Data
import Room
import pygame
import math
import random


def create_plot():
    random.shuffle(Room_Data.rooms)
    plots = [[5, 0]]
    for i in range(2):
        max = 4
        if plots[i][0] == 0 or plots[i][1] == 0 or plots[i][0] == 7 or plots[i][1] == 7:
            max = max - 1
        for j in plots_next_to(plots[i], plots):
            max = max - j
        for j in range(0, random.randint(1, 2)):  # change this for more plots?
            plots_next = plots_next_to(plots[i], plots)
            rand_int = random.randint(0, 6)
            if rand_int > 3:
                rand_int = 2
            if plots_next[rand_int] == 0 and new_plot_next(plots, plot_add(plots[i], rand_int), rand_int):
                plots.append(plot_add(plots[i], rand_int))
            else:
                rand_int = (rand_int - 1) % 4
                if plots_next[rand_int] == 0 and new_plot_next(plots, plot_add(plots[i], rand_int), rand_int):
                    plots.append(plot_add(plots[i], rand_int))
                else:
                    rand_int = (rand_int - 1) % 4
                    if plots_next[rand_int] == 0 and new_plot_next(plots, plot_add(plots[i], rand_int), rand_int):
                        plots.append(plot_add(plots[i], rand_int))
                    else:
                        rand_int = (rand_int - 1) % 4
                        if plots_next[rand_int] == 0 and new_plot_next(plots, plot_add(plots[i], rand_int), rand_int):
                            plots.append(plot_add(plots[i], rand_int))
    print(plots)
    create_Doors(plots)
    Room_Data.CURRENT_ROOM = Room_Data.rooms[0]


def plots_next_to(plot, plots):
    arr = [0, 0, 0, 0]
    for i in plots:
        temp = sub_plots(plot, [0, 1])
        if (i[0] == temp[0] and i[1] == temp[1]) or plot[1] == 0:
            arr[0] = 1
        temp = sub_plots(plot, [1, 0])
        if (i[0] == temp[0] and i[1] == temp[1]) or plot[0] == 0:
            arr[1] = 1
        temp = add_plots(plot, [0, 1])
        if (i[0] == temp[0] and i[1] == temp[1]) or plot[1] == 10:
            arr[2] = 1
        temp = add_plots(plot, [1, 0])
        if (i[0] == temp[0] and i[1] == temp[1]) or plot[0] == 10:
            arr[3] = 1
    return arr


def sub_plots(arr1, arr2):
    arr3 = []
    for i in range(0, 2):
        arr3.append(arr1[i] - arr2[i])
    return arr3


def add_plots(arr1, arr2):
    arr3 = []
    for i in range(0, 2):
        arr3.append(arr1[i] + arr2[i])
    return arr3


def plot_add(plot, rand_int):
    new_plot = [-1, -1]
    if rand_int == 0:
        new_plot = sub_plots(plot, [0, 1])
    if rand_int == 1:
        new_plot = sub_plots(plot, [1, 0])
    if rand_int == 2:
        new_plot = add_plots(plot, [0, 1])
    if rand_int == 3:
        new_plot = add_plots(plot, [1, 0])
    return new_plot


def new_plot_next(plots, new_plot, rand_int):
    if rand_int == 0:
        return [0, 0, 1, 0] == plots_next_to(new_plot, plots)
    if rand_int == 1:
        return [0, 0, 0, 1] == plots_next_to(new_plot, plots)
    if rand_int == 2:
        return [1, 0, 0, 0] == plots_next_to(new_plot, plots)
    if rand_int == 3:
        return [0, 1, 0, 0] == plots_next_to(new_plot, plots)


def create_Doors(plots):
    doors = []
    for i in plots:
        for j in plots:
            if (j[0] == i[0] and abs(j[1] - i[1]) == 1) or (j[1] == i[1] and abs(j[0] - i[0]) == 1):
                do = True
                for d in doors:
                    if (d[0] == j and d[1] == i) or (d[0] == i and d[1] == j):
                        do = False
                if (do):
                    doors.append([i, j])
                    if j[0] == i[0] and j[1] - i[1] == 1:
                        Door = Room.Door(400, 600, 400, 0, Room_Data.rooms[plots.index(i)],
                                         Room_Data.rooms[plots.index(j)])
                        Room_Data.rooms[plots.index(i)].doors.append([Door, "one"])
                        Room_Data.rooms[plots.index(j)].doors.append([Door, "two"])
                    if j[0] == i[0] and i[1] - j[1] == 1:
                        Door = Room.Door(400, 0, 400, 600, Room_Data.rooms[plots.index(i)],
                                         Room_Data.rooms[plots.index(j)])
                        Room_Data.rooms[plots.index(i)].doors.append([Door, "one"])
                        Room_Data.rooms[plots.index(j)].doors.append([Door, "two"])
                    if j[1] == i[1] and j[0] - i[0] == 1:
                        Door = Room.Door(800, 300, 0, 300, Room_Data.rooms[plots.index(i)],
                                         Room_Data.rooms[plots.index(j)])
                        Room_Data.rooms[plots.index(i)].doors.append([Door, "one"])
                        Room_Data.rooms[plots.index(j)].doors.append([Door, "two"])
                    if j[1] == i[1] and i[0] - j[0] == 1:
                        Door = Room.Door(0, 300, 800, 300, Room_Data.rooms[plots.index(i)],
                                         Room_Data.rooms[plots.index(j)])
                        Room_Data.rooms[plots.index(i)].doors.append([Door, "one"])
                        Room_Data.rooms[plots.index(j)].doors.append([Door, "two"])


def create_Room(screen):
    for i in Room_Data.CURRENT_ROOM.chests:
        i.draw_chest(screen)
    for i in Room_Data.CURRENT_ROOM.walls:
        pygame.draw.rect(screen, (1, 1, 1), [i.get_X(), i.get_Y(), i.get_width(), i.get_height()])
        pygame.draw.rect(screen, (100, 65, 23), [i.get_X() + 3, i.get_Y() + 3, i.get_width() - 6, i.get_height() - 6])
    for i in Room_Data.CURRENT_ROOM.bullets:
        i.bullet_move()
        color = (1, 1, 1)
        if i.bullet_type == 1:
            color = (178, 34, 34)
        if i.bullet_type == 2:
            color = (65, 105, 225)
        if i.bullet_type == 3:
            color = (148, 1, 211)
        pygame.draw.circle(screen, color, (round(i.get_X()), round(i.get_Y())), 3)
        dist_moved = math.sqrt(math.pow(i.get_init_X() - i.get_X(), 2) +
                               math.pow(i.get_init_Y() - i.get_Y(), 2))
        if dist_moved > i.ATTACK_RANGE:
            Room_Data.CURRENT_ROOM.bullets.remove(i)
        if i in Room_Data.CURRENT_ROOM.bullets:
            for j in Room_Data.CURRENT_ROOM.walls:
                if j.get_X() < i.get_X() < j.get_X() + j.get_width():
                    if j.get_Y() < i.get_Y() < j.get_Y() + j.get_height():
                        Room_Data.CURRENT_ROOM.bullets.remove(i)
                        break
    for i in Room_Data.CURRENT_ROOM.doors:
        if i[1] == "one":
            if i[0].X_1 == 500:
                pygame.draw.rect(screen, (1, 1, 1), [i[0].X_1 - 40, i[0].Y_1 - 20, 80, 40])
                pygame.draw.rect(screen, (100, 100, 100), [i[0].X_1 - 35, i[0].Y_1 - 15, 70, 30])
                pygame.draw.rect(screen, (1, 1, 1), [i[0].X_1 - 51, i[0].Y_1 - 6, 102, 12])
                pygame.draw.rect(screen, (100, 65, 23), [i[0].X_1 - 50, i[0].Y_1 - 5, 100, 10])
            else:
                pygame.draw.rect(screen, (1, 1, 1), [i[0].X_1 - 20, i[0].Y_1 - 40, 40, 80])
                pygame.draw.rect(screen, (100, 100, 100), [i[0].X_1 - 15, i[0].Y_1 - 35, 30, 70])
                pygame.draw.rect(screen, (1, 1, 1), [i[0].X_1 - 6, i[0].Y_1 - 51, 12, 102])
                pygame.draw.rect(screen, (100, 65, 23), [i[0].X_1 - 5, i[0].Y_1 - 50, 10, 100])
            i[0].current_room = "one"
        if i[1] == "two":
            if i[0].X_1 == 500:
                pygame.draw.rect(screen, (1, 1, 1), [i[0].X_2 - 40, i[0].Y_2 - 20, 80, 40])
                pygame.draw.rect(screen, (100, 100, 100), [i[0].X_2 - 35, i[0].Y_2 - 15, 70, 30])
                pygame.draw.rect(screen, (1, 1, 1), [i[0].X_2 - 51, i[0].Y_2 - 6, 102, 12])
                pygame.draw.rect(screen, (100, 65, 23), [i[0].X_2 - 50, i[0].Y_2 - 5, 100, 10])
            else:
                pygame.draw.rect(screen, (1, 1, 1), [i[0].X_2 - 20, i[0].Y_2 - 40, 40, 80])
                pygame.draw.rect(screen, (100, 100, 100), [i[0].X_2 - 15, i[0].Y_2 - 35, 30, 70])
                pygame.draw.rect(screen, (1, 1, 1), [i[0].X_2 - 6, i[0].Y_2 - 51, 12, 102])
                pygame.draw.rect(screen, (100, 65, 23), [i[0].X_2 - 5, i[0].Y_2 - 50, 10, 100])
            i[0].current_room = "two"
