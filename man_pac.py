import pygame  # Imports a game library that lets you use specific functions in your program.
import random  # Import to generate random numbers.

# This Initializes the pygame modules to get everything started.
pygame.init()

# The screen that will be created needs a width and a height.
screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))
# This creates the screen and gives it the width and
# height specified as a 2 item sequence.

# This creates the player and other objects, and gives them the images found in this folder. 
player = pygame.image.load("player.png")
enemy = pygame.image.load("enemy.png")
monster = pygame.image.load("monster.png")
avenger = pygame.image.load("avenger.png")
prize = pygame.image.load("prize.jpg")

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within
# screen boundaries or know when the image is off the screen).
player_height = player.get_height()
player_width = player.get_width()

enemy_height = enemy.get_height()
enemy_width = enemy.get_width()

monster_height = monster.get_height()
monster_width = monster.get_width()

avenger_height = avenger.get_height()
avenger_width = avenger.get_width()

prize_height = prize.get_height()
prize_width = prize.get_height()

print("This is the height of the player image: " + str(player_height))
print("This is the width of the player image: " + str(player_width))

# Store the positions of the player and enemy as variables so that you can change them later. 
playerXPosition = 100
playerYPosition = 100

# Make the enemy start off screen and at a random y position.
enemyXPosition = random.randint(0, screen_height + enemy_width)
enemyYPosition = random.randint(0, screen_height - enemy_height)

monsterXPosition = random.randint(0, screen_width)
monsterYPosition = random.randint(0, screen_height - monster_height)

avengerXPosition = screen_width
avengerYPosition = random.randint(0, screen_height - avenger_height)

prizeXPosition = random.randint(0, screen_height - prize_width)
prizeYPosition = screen_height

# This checks if the up or down key is pressed. Right now they are not so make them equal to the boolean value (True
# or False) of False. Boolean values are True or False values that can be used to test conditions and test states
# that are binary, i.e. either one way or the other.

keyUp = False
keyDown = False
keyRight = False
keyLeft = False

# This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit
# the program by quitting).
while 1:

    screen.fill(0)  # Clears the screen.
    # This draws the player and other object images to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(monster, (monsterXPosition, monsterYPosition))
    screen.blit(avenger, (avengerXPosition, avengerYPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

    pygame.display.flip()  # This updates the screen.

    # This loops through events in the game.
    for event in pygame.event.get():
        # This event checks if the user quits the program, then if so it exits the program. 

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # This event checks if the user press a key down.

        if event.type == pygame.KEYDOWN:
            # Test if the key pressed is the one we want.
            if event.key == pygame.K_UP:  # pygame.K_UP represents a keyboard key constant.
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
            if event.key == pygame.K_LEFT:
                keyLeft = True

        # This event checks if the key is up(i.e. not pressed by the user).

        if event.type == pygame.KEYUP:
            # Test if the key released is the one we want.
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            if event.key == pygame.K_LEFT:
                keyLeft = False

    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.

    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 
    if keyUp == True:
        if playerYPosition > 0:  # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - player_height:  # This makes sure that the user does not move the player below the window.
            playerYPosition += 1

    if keyRight == True:
        if playerXPosition > 0:
            playerXPosition += 1

    if keyLeft == True:
        if playerXPosition < screen_width + player_width:
            playerXPosition -= 1

    # The code below will check for collision between the player and the other objects
    # We set bounding boxes around the images of the player and the other objects so that if they intersect that will count as a collision

    # Bounding box for the player:
    playerBox = pygame.Rect(player.get_rect())

    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image.
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    # Bounding box for the enemy and update to the enemy's position
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    # Bounding box for the monster and update to the monster's position
    monsterBox = pygame.Rect(monster.get_rect())
    monsterBox.top = monsterYPosition
    monsterBox.left = monsterXPosition

    # Bounding box for the avenger and update to the avenger's position
    avengerBox = pygame.Rect(avenger.get_rect())
    avengerBox.top = avengerYPosition
    avengerBox.left = avengerXPosition

    # Bounding box for the prize:
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    # To Test collision of the boxes and if the user collides with the prize then they win
    if playerBox.colliderect(enemyBox):
        print("You lose!")
        pygame.quit()
        exit(0)

    if playerBox.colliderect(monsterBox):
        print("You lose")
        pygame.quit()
        exit(0)

    if playerBox.colliderect(avengerBox):
        print("You lose")
        pygame.quit()
        exit(0)

    if playerBox.colliderect(prizeBox):
        print("You Found the Prize, YOU WIN! ")
        pygame.quit()
        exit(0)

    # This will make the enemy approach the player from different parts of the screen
    enemyYPosition += 0.15

    monsterXPosition += 0.15

    avengerXPosition -= 0.15

    prizeYPosition -= 0.15
    # ================The game loop logic ends here. =============
