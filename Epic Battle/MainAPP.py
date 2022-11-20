import pygame
import random
import time

import pygame as pygame
from pygame import mixer

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
# Menu

# Screen
screen_window = pygame.display.set_mode((1400, 788))
pygame.display.set_caption("Epic Battle by Propsowicz")
icon = pygame.image.load("pics/icon.png")
pygame.display.set_icon(icon)
game_background = pygame.image.load('pics/background.png')
game_background2 = pygame.image.load('pics/box.png')
menu = pygame.image.load("pics/menu.png")
options = pygame.image.load("pics/options.png")
credits = pygame.image.load("pics/credits.png")

sound_bg = pygame.mixer.music.load("sounds/bgmusic.wav")
pygame.mixer.music.play(-1)                                                                                                        # włączyć muzyczkę!
text_font = pygame.font.SysFont("Arial", 80)

#shooting = False
#shooting_extra = False

# Character definition:
    # statistics
    # character display image
    # character movement

class char():
    def __init__(self, hitbox_X, hitbox_Y, X, Y, velocity, shooting, shooting_extra, life_points):
        self.hitbox_X = hitbox_X
        self.hitbox_Y = hitbox_Y
        self.X = int(X)
        self.Y = int(Y)
        self.velocity = velocity
        self.stand = True
        self.right = False
        self.left = False
        self.top = False
        self.step_count = 0
        self.climb_count = 0
        self.jump_count = 10
        self.is_jumping = False
        self.is_hit = False
        self.shooting = shooting
        self.shooting_extra = shooting_extra
        self.life_points = life_points
        self.death_anim = 0
        self.is_dead = False

    def char_display(self, char_class):
        self.char_class = char_class

        self.img_stand = pygame.image.load("pics/" + char_class + "/stand.png")
        self.img_won = pygame.image.load("pics/" + char_class + "/won.png")
        self.img_hurt = pygame.image.load("pics/" + char_class + "/hurt.png")
        self.img_attack_right = pygame.image.load("pics/" + char_class + "/Rattack1.png")
        self.img_attack_left = pygame.image.load("pics/" + char_class + "/Lattack1.png")
        self.img_attack_extra_right = pygame.image.load("pics/" + char_class + "/Rattack_extra1.png")
        self.img_attack_extra_left = pygame.image.load("pics/" + char_class + "/Lattack_extra1.png")
        self.img_right = [pygame.image.load("pics/" + char_class + "/rightwalk1.png"),
                              pygame.image.load("pics/" + char_class + "/rightwalk2.png"),
                              pygame.image.load("pics/" + char_class + "/rightwalk3.png"),
                              pygame.image.load("pics/" + char_class + "/rightwalk4.png"),
                              pygame.image.load("pics/" + char_class + "/rightwalk5.png"),
                              pygame.image.load("pics/" + char_class + "/rightwalk6.png")]
        self.img_left = [pygame.image.load("pics/" + char_class + "/leftwalk1.png"),
                             pygame.image.load("pics/" + char_class + "/leftwalk2.png"),
                             pygame.image.load("pics/" + char_class + "/leftwalk3.png"),
                             pygame.image.load("pics/" + char_class + "/leftwalk4.png"),
                             pygame.image.load("pics/" + char_class + "/leftwalk5.png"),
                             pygame.image.load("pics/" + char_class + "/leftwalk6.png")]
        self.img_top = [pygame.image.load("pics/" + char_class + "/climb2.png"),
                        pygame.image.load("pics/" + char_class + "/climb3.png"),
                        pygame.image.load("pics/" + char_class + "/climb4.png")]
        self.death = [pygame.image.load("pics/" + char_class + "/death1.png"),
                          pygame.image.load("pics/" + char_class + "/death2.png"),
                          pygame.image.load("pics/" + char_class + "/death3.png"),
                          pygame.image.load("pics/" + char_class + "/death4.png"),
                          pygame.image.load("pics/" + char_class + "/death5.png")]

    def char_movement(self, screen_window):

        if self.step_count + 1 >= 18:
            self.step_count = 0

        if self.climb_count + 1 >= 9:
            self.climb_count = 0

        if self.death_anim + 1 >= 5:
            self.death_anim = 4

        if self.is_dead:
            screen_window.blit(self.death[self.death_anim // 1], (self.X, self.Y + self.hitbox_Y / 1.5))
            if self.death_anim <= 4:
                self.death_anim += 1


        else:

            if not (self.stand):
                if self.left:
                    if self.is_hit:
                        screen_window.blit(self.img_hurt, (self.X, self.Y))
                        self.is_hit = False
                    elif self.shooting:
                        screen_window.blit(self.img_attack_left, (self.X, self.Y))
                        self.climb_count += 1
                    elif self.shooting_extra:
                        screen_window.blit(self.img_attack_extra_left, (self.X, self.Y))
                        self.climb_count += 1
                    else:
                        screen_window.blit(self.img_left[self.step_count // 3], (self.X, self.Y))
                    self.step_count += 1

                elif self.right:
                    if self.is_hit:
                        screen_window.blit(self.img_hurt, (self.X, self.Y))
                        self.is_hit = False
                    elif self.shooting:
                        screen_window.blit(self.img_attack_right, (self.X, self.Y))
                        self.climb_count += 1
                    elif self.shooting_extra:
                        screen_window.blit(self.img_attack_extra_right, (self.X, self.Y))
                        self.climb_count += 1
                    else:
                        screen_window.blit(self.img_right[self.step_count // 3], (self.X, self.Y))
                    self.step_count += 1

                elif self.top:
                    if self.is_hit:
                        screen_window.blit(self.img_hurt, (self.X, self.Y))
                        self.is_hit = False
                    else:
                        screen_window.blit(self.img_top[self.climb_count // 3], (self.X, self.Y))
                        self.climb_count += 1

            else:
                if self.right:
                    if self.is_hit:
                        screen_window.blit(self.img_hurt, (self.X, self.Y))
                        self.is_hit = False
                    elif self.shooting:
                        screen_window.blit(self.img_attack_right, (self.X, self.Y))
                        self.climb_count += 1
                    elif self.shooting_extra:
                        screen_window.blit(self.img_attack_extra_right, (self.X, self.Y))
                        self.climb_count += 1
                    else:
                        screen_window.blit(self.img_right[0], (self.X, self.Y))
                elif self.left:
                    if self.is_hit:
                        screen_window.blit(self.img_hurt, (self.X, self.Y))
                        self.is_hit = False
                    elif self.shooting:
                        screen_window.blit(self.img_attack_left, (self.X, self.Y))
                        self.climb_count += 1
                    elif self.shooting_extra:
                        screen_window.blit(self.img_attack_extra_left, (self.X, self.Y))
                        self.climb_count += 1
                    else:
                        screen_window.blit(self.img_left[0], (self.X, self.Y))
                else:
                    if self.is_hit:
                        screen_window.blit(self.img_hurt, (self.X, self.Y))
                        self.is_hit = False
                    elif self.shooting:
                        screen_window.blit(self.img_attack_right, (self.X, self.Y))
                        self.climb_count += 1
                    elif self.shooting_extra:
                        screen_window.blit(self.img_attack_extra_right, (self.X, self.Y))
                        self.climb_count += 1
                    else:
                        screen_window.blit(self.img_stand, (self.X, self.Y))
                self.step_count = 0
                self.climb_count = 0

class projectile():
    def __init__(self, bullet_X, bullet_Y, facing, bullet_velocity, char_class, att_type):
        self.bullet_X = bullet_X
        self.bullet_Y = bullet_Y
        self.facing = facing
        self.bullet_velocity = bullet_velocity * facing
        self.char_class = char_class
        self.bullet_move = 0
        self.att_type = att_type

    def load_projectile(self, screen_window, rdelx, rdely, ldelx, ldely):
        self.rdelx = rdelx
        self.rdely = rdely
        self.ldelx = ldelx
        self.ldely = ldely

        self.bullet_right = [pygame.image.load("pics/" + self.char_class + "/R" + self.att_type + "1.png"),
                             pygame.image.load("pics/" + self.char_class + "/R" + self.att_type + "2.png"),
                             pygame.image.load("pics/" + self.char_class + "/R" + self.att_type + "3.png")]
        self.bullet_left = [pygame.image.load("pics/" + self.char_class + "/L" + self.att_type + "1.png"),
                             pygame.image.load("pics/" + self.char_class + "/L" + self.att_type + "2.png"),
                             pygame.image.load("pics/" + self.char_class + "/L" + self.att_type + "3.png")]

        if self.bullet_move + 1 >= 9:
            self.bullet_move = 0

        if facing == 1:
            screen_window.blit(self.bullet_right[self.bullet_move // 3], ((self.bullet_X + self.rdelx), (self.bullet_Y + self.rdely)))
            self.bullet_move += 1
        else:
            screen_window.blit(self.bullet_left[self.bullet_move // 3], ((self.bullet_X + self.ldelx), (self.bullet_Y + self.ldely)))
            self.bullet_move += 1

def dying_player_1(player_name ,life_points, is_hit):
    global player_1_life_points
    if is_hit:
        if player_1_life_points > 0:
            player_1_life_points -= 1
            is_hit = False
            #print(player_name + " otrzymał obrażenia")
        else:
            print(player_name + " został pokonany")
            global player_1_is_dead
            player_1.is_dead = True

def dying_player_2(player_name ,life_points, is_hit):
    global player_2_life_points

    if is_hit:
        if player_2_life_points > 0:
            player_2_life_points -= 1
            is_hit = False
            #print(player_name + " otrzymał obrażenia")
        else:
            print(player_name + " został pokonany")
            global player_2_is_dead
            player_2.is_dead = True

def p1_hp_bar(life, is_hit, X, Y):
    hp_bar = life * 17
    pygame.draw.line(screen_window, (156, 0, 0), (X, Y), (X + hp_bar, Y), 50)

def p2_hp_bar(life, is_hit, X, Y):
    hp_bar = life * 17
    pygame.draw.line(screen_window, (156, 0, 0), (X - hp_bar, Y), (X, Y), 50)

def game_is_over():
    if player_1_life_points <= 0 or player_2_life_points <= 0:
        print("Koniec gry")
        global game_running
        global game_over

        game_over = True
        game_running = False


# Screen updating Function

def screen_update():
    global player_1_step_count
    global player_1_climb_count
    global player_2_step_count
    global player_2_climb_count
    screen_window.blit(game_background, (0, 0))
    screen_window.blit(game_background2, (0, 0))
    player_1.char_movement(screen_window)
    player_2.char_movement(screen_window)

    p1_hp_bar(player_1_life_points, player_1.is_hit, 50, 100)
    p2_hp_bar(player_2_life_points, player_2.is_hit, 1355, 100)



    for bullet in bullets:
        bullet.load_projectile(screen_window, 30, 10, -40, 10)
    for ex_bullet in extra_bullet:
        ex_bullet.load_projectile(screen_window, 0, -50, -10, -50)
    for bullet in bullets2:
        bullet.load_projectile(screen_window, 30, 10, 40, 10)
    for ex_bullet in extra_bullet2:
        ex_bullet.load_projectile(screen_window, 0, -90, -10, -90)

    pygame.display.update()


# Main LOOP
# Game variables

player_1 = char(64, 64, 100, 600, 5, False, False, 20)
player_1.char_display("Char_1")
player_2 = char(128, 32, 600, 600, 7, False, False, 20)
player_2.char_display("Char_2")
facing = 1
facing_extra = 1
bullets = []
bullets2 = []
extra_bullet = []
extra_bullet2 = []
menu_running = True
p1_attack_loop = 0
p2_attack_loop = 0
player_1_life_points = player_1.life_points
player_2_life_points = player_2.life_points
player_1_is_dead = False
player_2_is_dead = False
click = False
game_over = False

reload_attack_char_1 = True
reload_exattack_char_1 = True
reload_attack_char_2 = True
reload_exattack_char_2 = True

while menu_running:
    key_pressed = pygame.key.get_pressed()
    screen_window.blit(menu, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or key_pressed[pygame.K_ESCAPE]:
            menu_running = False

    if game_over:
        while game_over:
            screen_window.blit(game_background, (0, 0))
            key_pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if key_pressed[pygame.K_ESCAPE]:
                    game_over = False
                if event.type == pygame.QUIT:
                    game_over = False
                    menu_running = False

            if player_2_life_points <= 0:
                screen_window.blit(player_1.img_won, (player_1.X, player_1.Y))
                screen_window.blit(player_2.death[4], (player_2.X, player_2.Y + player_2.hitbox_Y / 1.5))
                text_display = text_font.render("P L A Y E R  1  W O N!", False, (0,0,0))
                screen_window.blit(text_display, (350, 300))

            if player_1_life_points <= 0:
                screen_window.blit(player_2.img_won, (player_2.X, player_2.Y))
                screen_window.blit(player_1.death[4], (player_1.X, player_1.Y + player_1.hitbox_Y / 1.5))
                text_display = text_font.render("P L A Y E R  2  W O N!", False, (0, 0, 0))
                screen_window.blit(text_display, (350, 300))
            pygame.display.update()

    if key_pressed[pygame.K_c]:
        game_running = True
        while game_running:
            screen_window.blit(credits, (0, 0))
            key_pressed = pygame.key.get_pressed()

            for event in pygame.event.get():
                if key_pressed[pygame.K_ESCAPE]:
                    game_running = False
                if event.type == pygame.QUIT:
                    game_running = False
                    menu_running = False
            pygame.display.update()

    if key_pressed[pygame.K_k]:
        game_running = True
        while game_running:
            screen_window.blit(options, (0, 0))
            key_pressed = pygame.key.get_pressed()

            for event in pygame.event.get():
                if key_pressed[pygame.K_ESCAPE]:
                    game_running = False
                if event.type == pygame.QUIT:
                    game_running = False
                    menu_running = False
            pygame.display.update()

    elif key_pressed[pygame.K_p]:
        game_running = True
        player_1_life_points = 20


        ###     TO TU SIĘ ZMIENIA HP!!!!!!!!! (20 TO WARTOŚĆ DOMYŚLNA)

        player_2_life_points = 20
        player_1.X = 100
        player_1.Y = 600
        player_2.X = 600
        player_2.Y = 600

        while game_running:
            key_pressed = pygame.key.get_pressed()
            clock.tick(27)


            event_attack_char_1 = pygame.USEREVENT
            event_exattack_char_1 = pygame.USEREVENT
            event_attack_char_2 = pygame.USEREVENT
            event_exattack_char_2 = pygame.USEREVENT



            for event in pygame.event.get():
                if key_pressed[pygame.K_ESCAPE]:
                    game_running = False
                if event.type == pygame.QUIT:
                    game_running = False
                    menu_running = False


            # opóźnienie ataków postaci:

                if event.type == event_attack_char_1:
                    reload_attack_char_1 = True
                if event.type == event_exattack_char_1:
                    reload_exattack_char_1 = True
                if event.type == event_attack_char_2:
                    reload_attack_char_2 = True
                if event.type == event_exattack_char_2:
                    reload_exattack_char_2 = True


            # Player 1 shooting
            if p1_attack_loop > 0:
                p1_attack_loop += 1
            if p1_attack_loop > 3:
                p1_attack_loop = 0

            for bullet in bullets:
                # Collision detection:
                    # Y coords
                if player_2.Y - player_2.hitbox_Y / 2 <= bullet.bullet_Y <= player_2.Y + player_2.hitbox_Y / 2:
                        # X coords
                    if player_2.X - player_2.hitbox_X / 2 <= bullet.bullet_X <= player_2.X + player_2.hitbox_X / 2 + 48:
                        print("hit")
                        player_2.is_hit = True
                        bullets.pop(bullets.index(bullet))
                if bullet.bullet_X < 1400 and bullet.bullet_X > 0:
                    bullet.bullet_X += bullet.bullet_velocity
                    player_1.shooting = False
                else:
                    bullets.pop(bullets.index(bullet))

            for ex_bullet in extra_bullet:
                # Collision detection:
                # Y coords
                if player_2.Y - player_2.hitbox_Y <= ex_bullet.bullet_Y <= player_2.Y + player_2.hitbox_Y:
                    # X coords
                    if player_2.X - player_2.hitbox_X / 2 <= ex_bullet.bullet_X <= player_2.X + player_2.hitbox_X / 2 + 48:
                        print(" extra hit")
                        player_2.is_hit = True
                        extra_bullet.pop(extra_bullet.index(ex_bullet))
                if ex_bullet.bullet_X < 1400 and ex_bullet.bullet_X > 0:
                    ex_bullet.bullet_X += ex_bullet.bullet_velocity
                    player_1.shooting_extra = False
                else:
                    extra_bullet.pop(extra_bullet.index(ex_bullet))


            if key_pressed[pygame.K_h] and p1_attack_loop == 0 and reload_attack_char_1:
                player_1.shooting = True
                if player_1.left:
                    facing = -1
                if player_1.right:
                    facing = 1
                if len(bullets) < 4:
                    bullets.append(projectile(player_1.X, player_1.Y, facing, 20, "Char_1", "fire"))
                reload_attack_char_1 = False
                pygame.time.set_timer(event_attack_char_1, 250)

            if key_pressed[pygame.K_j] and reload_exattack_char_1:
                player_1.shooting_extra = True
                if player_1.left:
                    facing = -1
                if player_1.right:
                    facing = 1
                if len(extra_bullet) < 1:
                    extra_bullet.append(projectile(player_1.X, player_1.Y, facing, 20, "Char_1", "fire_extra"))
                reload_exattack_char_1 = False
                pygame.time.set_timer(event_exattack_char_1, 500)

            # Player 1 movement

            if key_pressed[pygame.K_a] and 0 < player_1.X - 0.5 * player_1.hitbox_X and key_pressed[pygame.K_w] and 575 < player_1.Y - 0.5 * player_1.hitbox_Y:
                player_1.X -= player_1.velocity
                player_1.Y -= player_1.velocity
                player_1.left = False
                player_1.right = False
                player_1.top = True
                player_1.stand = False

            elif key_pressed[pygame.K_a] and 0 < player_1.X - 0.5 * player_1.hitbox_X and key_pressed[pygame.K_s] and 675 > player_1.Y + 0.5 * player_1.hitbox_Y:
                player_1.X -= player_1.velocity
                player_1.Y += player_1.velocity
                player_1.left = False
                player_1.right = False
                player_1.top = True
                player_1.stand = False

            elif key_pressed[pygame.K_d] and 1370 > player_1.X + 0.5 * player_1.hitbox_X and key_pressed[pygame.K_w] and 575 < player_1.Y - 0.5 * player_1.hitbox_Y:
                player_1.X += player_1.velocity
                player_1.Y -= player_1.velocity
                player_1.left = False
                player_1.right = False
                player_1.top = True
                player_1.stand = False

            elif key_pressed[pygame.K_d] and 1370 > player_1.X + 0.5 * player_1.hitbox_X and key_pressed[pygame.K_s] and 675 > player_1.Y + 0.5 * player_1.hitbox_Y:
                player_1.X += player_1.velocity
                player_1.Y += player_1.velocity
                player_1.left = False
                player_1.right = False
                player_1.top = True
                player_1.stand = False

            elif key_pressed[pygame.K_a] and 0 < player_1.X - 0.5 * player_1.hitbox_X:
                player_1.X -= player_1.velocity
                player_1.left = True
                player_1.right = False
                player_1.top = False
                player_1.stand = False


            elif key_pressed[pygame.K_d] and 1370 > player_1.X + 0.5 * player_1.hitbox_X:
                player_1.X += player_1.velocity
                player_1.left = False
                player_1.right = True
                player_1.top = False
                player_1.stand = False


            elif key_pressed[pygame.K_w] and 575 < player_1.Y - 0.5 * player_1.hitbox_Y:
                player_1.Y -= player_1.velocity
                player_1.left = False
                player_1.right = False
                player_1.top = True
                player_1.stand = False

            elif key_pressed[pygame.K_s] and 675 > player_1.Y + 0.5 * player_1.hitbox_Y:
                player_1.Y += player_1.velocity
                player_1.left = False
                player_1.right = False
                player_1.top = True
                player_1.stand = False

            else:
                player_1.top = False
                player_1.stand = True
                player_1.step_count = 0

            if not (player_1.is_jumping):
                if key_pressed[pygame.K_SPACE]:
                    player_1.is_jumping = True
                    player_1.left = False
                    player_1.right = False
                    player_1.step_count = 0
            else:
                if player_1.jump_count >= -10:
                    neg = 1
                    if player_1.jump_count < 0:
                        neg = -1
                    player_1.Y -= (player_1.jump_count ** 2) * 0.4 * neg
                    if player_1.Y > 675:
                        player_1.Y = 650
                    player_1.jump_count += -1
                else:
                    player_1.is_jumping = False
                    player_1.jump_count = 10

            # Player 2 shooting

            if p2_attack_loop > 0:
                p2_attack_loop += 1
            if p2_attack_loop > 3:
                p2_attack_loop = 0

            for bullet in bullets2:
                bullet.bullet_Y = player_2.Y
                bullet.bullet_X = player_2.X

                # Collision detection:
                # Y coords
                if player_1.Y - player_1.hitbox_Y / 2 <= bullet.bullet_Y <= player_1.Y + player_1.hitbox_Y / 2:
                    # X coords
                    if player_1.X - player_1.hitbox_X / 2 <= bullet.bullet_X <= player_1.X + player_1.hitbox_X / 2 + 48:
                        print("player 2 hit")
                        player_1.is_hit = True
                        bullets2.pop(bullets2.index(bullet))
                        player_2.shooting = False
                else:
                    bullets2.pop(bullets2.index(bullet))
                player_2.shooting = False

            for ex_bullet in extra_bullet2:
                if player_1.Y - player_1.hitbox_Y <= ex_bullet.bullet_Y <= player_1.Y + player_1.hitbox_Y:
                    # X coords
                    if player_1.X - player_1.hitbox_X - 48 <= ex_bullet.bullet_X <= player_1.X + player_1.hitbox_X / 4:
                        print("Player 2 extra hit")
                        player_1.is_hit = True
                        extra_bullet2.pop(extra_bullet2.index(ex_bullet))
                if ex_bullet.bullet_X < 1400 and ex_bullet.bullet_X > 0:
                    ex_bullet.bullet_X += ex_bullet.bullet_velocity
                    player_2.shooting_extra = False
                else:
                    extra_bullet2.pop(extra_bullet2.index(ex_bullet))

            if key_pressed[pygame.K_END] and p2_attack_loop == 0 and reload_attack_char_2:
                player_2.shooting = True
                if player_2.left:
                    facing = -1
                if player_2.right:
                    facing = 1
                if len(bullets2) < 4:
                    bullets2.append(projectile(player_2.X, player_2.Y, facing, 20, "Char_2", "fire"))
                reload_attack_char_2 = False
                pygame.time.set_timer(event_attack_char_2, 200)


            if key_pressed[pygame.K_PAGEDOWN] and reload_exattack_char_2:
                player_2.shooting_extra = True
                if player_2.left:
                    facing = -1
                if player_2.right:
                    facing = 1
                if len(extra_bullet2) < 1:
                    extra_bullet2.append(projectile(player_2.X, player_2.Y, facing, 20, "Char_2", "fire_extra"))
                reload_exattack_char_2 = False
                pygame.time.set_timer(event_exattack_char_2, 250)

                # Player 2 movement

            if key_pressed[pygame.K_LEFT] and 0 < player_2.X - 0.5 * player_2.hitbox_X and key_pressed[pygame.K_UP] and 575 < player_2.Y - 0.5 * player_2.hitbox_Y:
                player_2.X -= player_2.velocity
                player_2.Y -= player_2.velocity
                player_2.left = False
                player_2.right = False
                player_2.top = True
                player_2.stand = False

            elif key_pressed[pygame.K_LEFT] and 0 < player_2.X - 0.5 * player_2.hitbox_X and key_pressed[pygame.K_DOWN] and 675 > player_2.Y + 0.5 * player_2.hitbox_Y:
                player_2.X -= player_2.velocity
                player_2.Y += player_2.velocity
                player_2.left = False
                player_2.right = False
                player_2.top = True
                player_2.stand = False

            elif key_pressed[pygame.K_RIGHT] and 1370 > player_2.X + 0.5 * player_2.hitbox_X and key_pressed[pygame.K_UP] and 575 < player_2.Y - 0.5 * player_2.hitbox_Y:
                player_2.X += player_2.velocity
                player_2.Y -= player_2.velocity
                player_2.left = False
                player_2.right = False
                player_2.top = True
                player_2.stand = False

            elif key_pressed[pygame.K_RIGHT] and 1370 > player_2.X + 0.5 * player_2.hitbox_X and key_pressed[pygame.K_DOWN] and 675 > player_2.Y + 0.5 * player_2.hitbox_Y:
                player_2.X += player_2.velocity
                player_2.Y += player_2.velocity
                player_2.left = False
                player_2.right = False
                player_2.top = True
                player_2.stand = False

            elif key_pressed[pygame.K_LEFT] and 0 < player_2.X - 0.5 * player_2.hitbox_X:
                player_2.X -= player_2.velocity
                player_2.left = True
                player_2.right = False
                player_2.top = False
                player_2.stand = False


            elif key_pressed[pygame.K_RIGHT] and 1370 > player_2.X + 0.5 * player_2.hitbox_X:
                player_2.X += player_2.velocity
                player_2.left = False
                player_2.right = True
                player_2.top = False
                player_2.stand = False


            elif key_pressed[pygame.K_UP] and 575 < player_2.Y - 0.5 * player_2.hitbox_Y:
                player_2.Y -= player_2.velocity
                player_2.left = False
                player_2.right = False
                player_2.top = True
                player_2.stand = False

            elif key_pressed[pygame.K_DOWN] and 675 > player_2.Y + 0.5 * player_2.hitbox_Y:
                player_2.Y += player_2.velocity
                player_2.left = False
                player_2.right = False
                player_2.top = True
                player_2.stand = False

            else:
                player_2.top = False
                player_2.stand = True
                player_2.step_count = 0

            if not (player_2.is_jumping):
                if key_pressed[pygame.K_DELETE]:
                    player_2.is_jumping = True
                    player_2.left = False
                    player_2.right = False
                    player_2.step_count = 0
            else:
                if player_2.jump_count >= -10:
                    neg = 1
                    if player_2.jump_count < 0:
                        neg = -1
                    player_2.Y -= (player_2.jump_count ** 2) * 0.4 * neg
                    if player_2.Y > 675:
                        player_2.Y = 650
                    player_2.jump_count += -1
                else:
                    player_2.is_jumping = False
                    player_2.jump_count = 10




            dying_player_1("Player_1", player_1.life_points, player_1.is_hit)
            dying_player_2("Player_2", player_2.life_points, player_2.is_hit)
            game_is_over()




            screen_update()

    pygame.display.update()



pygame.quit()
