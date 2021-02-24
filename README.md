# Import required modules

    import pygame 
    import random

# Initialize pygame

    pygame.init()

# Create screen by giving proper height and width

    screen = pygame.display.set_mode((800, 600))

# Background surface

    bg_surface = pygame.image.load('space.png').convert()
    bg_surface = pygame.transform.scale2x(bg_surface)

# Title 

    pygame.display.set_caption('Space Invaders')

# Tumbnail

    icon = pygame.image.load('ufo.png')
    pygame.display.set_icon(icon)

# Spaceship

    shipImage = pygame.image.load('space-ship-icon.png')
    shipImageX = 370
    shipImageY = 480
    ship_moveX = 0

# Ememy Spaceship

    enemyImage = []
    enemyImageX = []
    enemyImageY = []
    enemy_moveX = []
    enemy_moveY = []
    no_enimies = 8
    for i in range(no_enimies):
        enemyImage.append(pygame.image.load('space-invader-icon.png'))
        enemyImageX.append(random.randint(0,800))
        enemyImageY.append (random.randint(40,150))
        enemy_moveX.append(3)
        enemy_moveY.append(40)

# Bullet

    bulletImage = pygame.image.load('enemylaser.png')
    bulletImageX = 0
    bulletImageY = 480
    bullet_moveX = 0
    bullet_moveY = 10
    bullet_status = "ready"

# Scores

    scores = 0
    font = pygame.font.Font("04B_19.TTF",40)
    scoreX = 10
    scoreY = 10
    game_over_font = pygame.font.Font("04B_19.TTF",70)

# Spaceship Function

    def ship(x,y):
        screen.blit(shipImage, (x,y))

# Enemy Spaceship Function

    def enemyship(x,y,i):
        screen.blit(enemyImage[i], (x, y))

# Function to Shoot bullet
    def shoot(x,y):
        global bullet_status
        bullet_status = "fire"
        screen.blit(bulletImage, (x+28,y+10))

# Collision between Spaceship and Enemy Spaceship

Use distance formula = √(x2 - x1)2 and (y2 - y1)2

    def collision_ship_enemyship(enemyImageX,enemyImageY,bulletImageX,bulletImageY):
    dist = math.sqrt(math.pow(enemyImageX-bulletImageX,2))+(math.pow(enemyImageY-bulletImageY,2))
    if dist < 27:#dist between enemyship and our ship
        return True
    else:
        return False

# Setting the Scores

    def scores_in_game(x,y) :
        scorevalues = font.render("SCORE : " + str(scores), True, (255, 255, 255))
        screen.blit(scorevalues, (x, y))

# Function for setting Game Over

    def over():
        over_value = font.render("GAME OVER LOSER!", True, (255, 255, 255))
        screen.blit(over_value, (230, 250))

# Main Gameplay

    run = True
    while run:

# Background Image

    screen.blit(bg_surface, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = True

# keystrokes

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

# Checking for boundaries of spaceship 

    shipImageX += ship_moveX
        if shipImageX <= 0:
            shipImageX = 0
        elif shipImageX >= 736:
            shipImageX = 736

# Enemy Spaceship Movement

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

 # Collision

        collide = collision_ship_enemyship(enemyImageX[i], enemyImageY[i], bulletImageX, bulletImageY)
        if collide:
            bulletImageY = 480
            bullet_status = "ready"
            scores += 1
            enemyImageX[i] = random.randint(0, 800)
            enemyImageY[i] = random.randint(40, 150)

        enemyship(enemyImageX[i],enemyImageY[i],i)

# Bullet Movement

    if bulletImageY <= 0:
        bulletImageY = 480
        bullet_status = "ready"

    if bullet_status is "fire":
        shoot(bulletImageX,bulletImageY)
        bulletImageY -= bullet_moveY


    ship(shipImageX,shipImageY)
    scores_in_game(scoreX,scoreY)

# Updates

    pygame.display.update()
