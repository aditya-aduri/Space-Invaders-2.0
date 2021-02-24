import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800,600))#screen
bg_surface = pygame.image.load('space.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

#title
pygame.display.set_caption("Space Invaders 2.0")
tumbnail = pygame.image.load('UFO-icon.png')
pygame.display.set_icon(tumbnail)

#ship
shipImage = pygame.image.load('Spaceship.png')
shipImageX = 370
shipImageY = 480
ship_moveX = 0

#enemyship
enemyImage = []
enemyImageX = []
enemyImageY = []
enemy_moveX = []
enemy_moveY = []
no_enimies = 8

for i in range(no_enimies):
    enemyImage.append(pygame.image.load('Enemy-Spaceship.png'))
    enemyImageX.append(random.randint(0,800))
    enemyImageY.append (random.randint(40,150))
    enemy_moveX.append(3)
    enemy_moveY.append(40)

#bullet
bulletImage = pygame.image.load('laser.png')
bulletImageX = 0
bulletImageY = 480
bullet_moveX = 0
bullet_moveY = 10
bullet_status = "ready"

#score
scores = 0
font = pygame.font.Font("04B_19.TTF",40)
scoreX = 10
scoreY = 10
game_over_font = pygame.font.Font("04B_19.TTF",70)

def scores_in_game(x,y) :
    scorevalues = font.render("SCORE : " + str(scores), True, (255, 255, 255))
    screen.blit(scorevalues, (x, y))

def over():
    over_value = font.render("GAME OVER LOSER!", True, (255, 255, 255))
    screen.blit(over_value, (230, 250))

def ship(x,y):
    screen.blit(shipImage, (x,y))

def enemyship(x,y,i):
    screen.blit(enemyImage[i], (x, y))

def shoot(x,y):
    global bullet_status
    bullet_status = "fire"
    screen.blit(bulletImage, (x+28,y+10))

def collision_ship_enemyship(enemyImageX,enemyImageY,bulletImageX,bulletImageY):
    dist = math.sqrt(math.pow(enemyImageX-bulletImageX,2))+(math.pow(enemyImageY-bulletImageY,2))#we calculated by using {distance = sqrt od (x2 - x1)square and (y2 - y1)square
    if dist < 27:#dist between enemyship and our ship
        return True
    else:
        return False


#gamepaly
run = True
while run:

    screen.blit(bg_surface, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = True


        #keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship_moveX = -3
            if event.key == pygame.K_RIGHT:
                ship_moveX = 3
            if event.key == pygame.K_SPACE:
                if bullet_status is "ready":
                    bulletImageX = shipImageX
                    shoot(shipImageX,bulletImageY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ship_moveX = 0

    shipImageX += ship_moveX
    if shipImageX <= 0:
        shipImageX = 0
    elif shipImageX >= 736:
        shipImageX = 736

    for i in range(no_enimies):
        if enemyImageY[i] > 440:
            for j in range(no_enimies):
                enemyImageY[j] = 2000
            over()
            break

        enemyImageX[i] += enemy_moveX[i]
        if enemyImageX[i] <= 0:
            enemy_moveX[i] = 3
            enemyImageY[i] += enemy_moveY[i]
        elif enemyImageX[i] >= 736:
            enemy_moveX[i] = -3
            enemyImageY[i] += enemy_moveY[i]
        # collision
        collide = collision_ship_enemyship(enemyImageX[i], enemyImageY[i], bulletImageX, bulletImageY)
        if collide:
            bulletImageY = 480
            bullet_status = "ready"
            scores += 1
            enemyImageX[i] = random.randint(0, 800)
            enemyImageY[i] = random.randint(40, 150)

        enemyship(enemyImageX[i],enemyImageY[i],i)


    #bullet:
    if bulletImageY <= 0:
        bulletImageY = 480
        bullet_status = "ready"

    if bullet_status is "fire":
        shoot(bulletImageX,bulletImageY)
        bulletImageY -= bullet_moveY


    ship(shipImageX,shipImageY)
    scores_in_game(scoreX,scoreY)
    pygame.display.update()#updates


