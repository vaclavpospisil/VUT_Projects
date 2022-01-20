import pygame
import os
import math

WIDTH, HEIGHT = 1920, 1080 # Width and height of the window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT)) # Display the window
pygame.display.set_caption("Double Spring Pendulum") # Caption of the window
FPS = 60 # Frames per second

# Pygame Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 100)
GRAY = (127, 127, 127)

STARTING_POINT = (WIDTH/2, HEIGHT/4) # Anchor point of the pendulum
# Offsets must be introduced because pygame origin (0, 0) is in the right top corner
X_OFFSET = STARTING_POINT[0]
Y_OFFSET = STARTING_POINT[1]

SCATTER_LIMIT = 1000 # Limit of scatter points
SCATTER_1 = []       # List of scatter1 (For rendering path of bob 1)
SCATTER_2 = []       # List of scatter2 (For rendering path of bob 2)

# Function of drawing in pygame window
def draw_window(BOB_1_x, BOB_1_y, BOB_2_x, BOB_2_y):
    WINDOW.fill(BLACK) # Fill the window with black color

    # Render of the bob path
    SCATTER_1.insert(0, (int(BOB_1_x), int(BOB_1_y)))
    SCATTER_2.insert(0, (int(BOB_2_x), int(BOB_2_y)))

    if len(SCATTER_1) > 1:
        pygame.draw.lines(WINDOW, BLUE, False, SCATTER_1, 6)
    if len(SCATTER_2) > 1:
        pygame.draw.lines(WINDOW, RED, False, SCATTER_2, 6)

    if len(SCATTER_1) > SCATTER_LIMIT: # After exceeding the scatter limit, remove the first points in scatter1
        SCATTER_1.pop()
    if len(SCATTER_2) > SCATTER_LIMIT: # The same as for scatter1
        SCATTER_2.pop()

    pygame.draw.circle(WINDOW, GRAY, STARTING_POINT, 15)                                            # Draw the Anchor point
    pygame.draw.line(WINDOW, GRAY, (STARTING_POINT), (int(BOB_1_x), int(BOB_1_y)),10)               # Draw a spring between Anchor and first bob
    pygame.draw.line(WINDOW, GRAY, (int(BOB_1_x), int(BOB_1_y)), (int(BOB_2_x), int(BOB_2_y)), 10)  # Draw a spring between first and second bob
    pygame.draw.circle(WINDOW, BLUE, (int(BOB_1_x), int(BOB_1_y)), 25)                              # Draw the first bob
    pygame.draw.circle(WINDOW, RED, (int(BOB_2_x), int(BOB_2_y)), 25)                               # Draw the second bob

    pygame.display.update() # Update a window

# Function to calculate acceleration of the first bob
def calculate_a_2 (alpha_0, alpha_1, beta_0, beta_1, a_0, a_1, b_0, b_1, l1, l2, k1, k2, m1, m2, g):
    return ((k1*l1+g*m1*math.cos(alpha_0)-k2*l2*math.cos(alpha_0-beta_0)+k2*b_0*math.cos(alpha_0-beta_0)+a_0*(-k1+m1*(alpha_1**2)))/m1)

# Function to calculate acceleration of the second bob    
def calculate_b_2 (alpha_0, alpha_1, beta_0, beta_1, a_0, a_1, b_0, b_1, l1, l2, k1, k2, m1, m2, g):
    return ((k2*l2*m1+k2*l2*m2-k1*l1*m2*math.cos(alpha_0-beta_0)+k1*m2*a_0*math.cos(alpha_0-beta_0)-b_0*(k2*(m1+m2)-m1*m2*(beta_1**2)))/(m1*m2))

# Function to calculate angle acceleration of the first bob
def calculate_alpha_2 (alpha_0, alpha_1, beta_0, beta_1, a_0, a_1, b_0, b_1, l1, l2, k1, k2, m1, m2, g):
    return (-((g*m1*math.sin(alpha_0)-k2*l2*math.sin(alpha_0-beta_0)+k2*b_0*math.sin(alpha_0-beta_0)+2*m1*a_1*alpha_1)/(m1*a_0)))

# Function to calculate angle acceleration of the second bob
def calculate_beta_2 (alpha_0, alpha_1, beta_0, beta_1, a_0, a_1, b_0, b_1, l1, l2, k1, k2, m1, m2, g):
    return ((-k1*l1*math.sin(alpha_0-beta_0)+k1*a_0*math.sin(alpha_0-beta_0)-2*m1*b_1*beta_1)/(m1*b_0))

# Starting parameters
alpha_0 = math.pi/6 # Starting angle of the first bob
beta_0 = math.pi/6  # Starting angle of the second bob
alpha_1 = 0         # Angle velocity of the first bob
beta_1 = 0          # Angle velocity of the second bob
alpha_2 = 0         # Angle acceleration of the first bob
beta_2 = 0          # Angle acceleration of the first bob

a_0 = 250   # Starting length of the first spring
b_0 = 250   # Starting length of the second spring
a_1 = 0     # Starting velocity of the first spring
b_1 = 0     # Starting velocity of the second spring
a_2 = 0     # Starting acceleration of the first spring
b_2 = 0     # Starting acceleration of the second spring

l1 = 75     # first spring free length
l2 = 75     # second spring free length
m1 = 10     # mass of the bob 1
m2 = 10     # mass of the bob 2
k1 = 2      # first spring constant 
k2 = 1      # second spring constant
g = 9.81    # gravitational constant

dt = 0.1    # time step
T_MAX = 300 # max time
T=0         # initial time

# MAIN LOOP
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(FPS) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If you click on the X button, simulation will end
            run = False
        if event.type == pygame.KEYDOWN: # If you press ESC, simulation will end
            if event.key == pygame.K_ESCAPE:
                run = False

    # Call a function to calculate angle acceleration of the first bob
    alpha_2 = calculate_alpha_2 (alpha_0, alpha_1, beta_0, beta_1, a_0, a_1, b_0, b_1, l1, l2, k1, k2, m1, m2, g)
    # Call a function to calculate angle acceleration of the second bob
    beta_2 = calculate_beta_2 (alpha_0, alpha_1, beta_0, beta_1, a_0, a_1, b_0, b_1, l1, l2, k1, k2, m1, m2, g) 
    # Call a function to calculte acceleration first bob
    a_2 = calculate_a_2 (alpha_0, alpha_1, beta_0, beta_1, a_0, a_1, b_0, b_1, l1, l2, k1, k2, m1, m2, g) 
    # Call a function to calculte acceleration first bob
    b_2 = calculate_b_2 (alpha_0, alpha_1, beta_0, beta_1, a_0, a_1, b_0, b_1, l1, l2, k1, k2, m1, m2, g)

    alpha_1 = alpha_1 + alpha_2*dt  # Calculate angle velocity of the first bob
    beta_1 = beta_1 + beta_2*dt     # Calculate angle velocity of the second bob
    a_1 = a_1 + a_2*dt              # Calculate velocity of the first bob
    b_1 = b_1 + b_2*dt              # Calculate velocity of the second bob

    alpha_0 = alpha_0 + alpha_1*dt  # Updating angle alpha
    beta_0 = beta_0 + beta_1*dt     # Updating angle beta
    a_0 = a_0 + a_1*dt              # Updating length of first spring
    b_0 = b_0 + b_1*dt              # Updating length of second spring

    alpha_0 = alpha_0%(2*math.pi) # Angle adjustment for one period (0, 2*pi)
    beta_0 = beta_0%(2*math.pi)   # Angle adjustment for one period (0, 2*pi)
        
    BOB_1_x = X_OFFSET + a_0*math.sin(alpha_0) # New x position of first bob
    BOB_1_y = Y_OFFSET +a_0*math.cos(alpha_0)  # new y position of first bob
        
    BOB_2_x = BOB_1_x + b_0*math.sin(beta_0) # New x position of second bob
    BOB_2_y = BOB_1_y + b_0*math.cos(beta_0) # New y position of first bob

    # Pausing after overrun the maximum time
    pause = False
    T += dt
    if T >= T_MAX:
        pause = True

    if pause == True:
        pygame.time.delay(3000)
        
    # Function call to drawing in pygame window    
    draw_window(BOB_1_x, BOB_1_y, BOB_2_x, BOB_2_y) 

    pygame.display.update() # Update the window

pygame.quit() # End of the simulation