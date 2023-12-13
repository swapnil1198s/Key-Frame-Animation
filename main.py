import pygame
import math
from Keyframes import Keyframes
from Animation import Animation

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stick Figure Frame Animation")

#Colors
PURPLE = (75, 0, 130)
BROWN = (218, 160, 109)
MAROON = (128, 0, 0)
BLACK = (0, 0, 0)

# Create a bold font object for the title
title_font = pygame.font.SysFont(None, 40, bold=True)
title_text = title_font.render("Stick Figure Frame Animation", True, MAROON)
title_text_rect = title_text.get_rect(center=(WIDTH // 2, 20))

# Create a regular font object for the controls
controls_font = pygame.font.SysFont(None, 24)

# Text for controls, each line as a separate string
controls_texts = [
    "Controls:",
    "j : Load jumping motion",
    "w : Load waving motion",
    "R-arrow: If motion loaded, navigate to next key frame",
    "L-arrow: If motion loaded, navigate to previous key frame",
    "a : Animate the loaded motion"
]

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Font for labels
font = pygame.font.SysFont(None, 24)

#Helper function to guide positioning of stickman during development
def draw_axes(screen):
    # Colors
    BLACK = (0, 0, 0)

    # Draw x-axis and markings
    pygame.draw.line(screen, BLACK, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2))
    for x in range(0, WIDTH, 10):  # Adjust step for different intervals
        pygame.draw.line(screen, BLACK, (x, HEIGHT // 2 - 5), (x, HEIGHT // 2 + 5))
        if x % 50 == 0:  # Label every 50 pixels
            label = font.render(str(x), True, BLACK)
            screen.blit(label, (x, HEIGHT // 2 + 10))

    # Draw y-axis and markings
    pygame.draw.line(screen, BLACK, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    for y in range(0, HEIGHT, 10):  # Adjust step for different intervals
        pygame.draw.line(screen, BLACK, (WIDTH // 2 - 5, y), (WIDTH // 2 + 5, y))
        if y % 50 == 0:  # Label every 50 pixels
            label = font.render(str(y), True, BLACK)
            screen.blit(label, (WIDTH // 2 + 10, y))

# Method for drawing the stick figure 
def draw_stick_figure(screen, position, arm_angles, leg_angles):
    """
    Draw a stick figure on the screen.

    Parameters:
    - screen: Pygame surface where the stick figure will be drawn.
    - position: Tuple (x, y) for the base position of the torso.
    - arm_angles: Dictionary with 'left_upper', 'left_lower', 'right_upper', 'right_lower' angles for arms.
    - leg_angles: Dictionary with 'left_upper', 'left_lower', 'right_upper', 'right_lower' angles for legs.
    """
    # Constants for body parts
    HEAD_RADIUS = 20
    TORSO_HEIGHT = 100
    TORSO_WIDTH = 50
    UPPER_ARM_LENGTH = 40
    LOWER_ARM_LENGTH = 30
    UPPER_LEG_LENGTH = 50
    LOWER_LEG_LENGTH = 40

    # Convert angles from degrees to radians
    arm_angles_rad = {k: math.radians(v) for k, v in arm_angles.items()}
    leg_angles_rad = {k: math.radians(v) for k, v in leg_angles.items()}

    # Calculate torso position
    torso_top = (position[0], position[1] - TORSO_HEIGHT/2)
    torso_bottom = (position[0], position[1] + TORSO_HEIGHT/2)

    # Head position
    head_center = (position[0], torso_top[1] - HEAD_RADIUS)

    # Draw head
    pygame.draw.circle(screen, BROWN, head_center, HEAD_RADIUS)

    # Draw torso
    pygame.draw.rect(screen, PURPLE, pygame.Rect(position[0]-TORSO_WIDTH/2, torso_top[1], TORSO_WIDTH, TORSO_HEIGHT), border_radius=10)

    # Calculate and draw arms
    shoulder_left = (position[0] - TORSO_WIDTH / 2, position[1] - TORSO_HEIGHT / 3)
    shoulder_right = (position[0] + TORSO_WIDTH / 2, position[1] - TORSO_HEIGHT / 3)


    left_upper_arm_angle = arm_angles_rad['left_upper']
    left_lower_arm_angle = arm_angles_rad['left_lower']

    left_upper_arm_end_x = shoulder_left[0] + UPPER_ARM_LENGTH * math.cos(left_upper_arm_angle)
    left_upper_arm_end_y = shoulder_left[1] + UPPER_ARM_LENGTH * math.sin(left_upper_arm_angle)
    left_upper_arm_end = (left_upper_arm_end_x, left_upper_arm_end_y)

    left_lower_arm_end_x = left_upper_arm_end_x + LOWER_ARM_LENGTH * math.cos(left_lower_arm_angle)
    left_lower_arm_end_y = left_upper_arm_end_y + LOWER_ARM_LENGTH * math.sin(left_lower_arm_angle)

    pygame.draw.line(screen, (0, 0, 0), shoulder_left, left_upper_arm_end, 4)
    pygame.draw.line(screen, (0, 0, 0), left_upper_arm_end, (left_lower_arm_end_x, left_lower_arm_end_y), 4)

    # Calculate and draw right arm
    right_upper_arm_angle = arm_angles_rad['right_upper']
    right_lower_arm_angle = arm_angles_rad['right_lower']

    right_upper_arm_end_x = shoulder_right[0] + UPPER_ARM_LENGTH * math.cos(right_upper_arm_angle)
    right_upper_arm_end_y = shoulder_right[1] + UPPER_ARM_LENGTH * math.sin(right_upper_arm_angle)
    right_upper_arm_end = (right_upper_arm_end_x, right_upper_arm_end_y)

    right_lower_arm_end_x = right_upper_arm_end_x + LOWER_ARM_LENGTH * math.cos(right_lower_arm_angle)
    right_lower_arm_end_y = right_upper_arm_end_y + LOWER_ARM_LENGTH * math.sin(right_lower_arm_angle)

    pygame.draw.line(screen, (0, 0, 0), shoulder_right, right_upper_arm_end, 4)
    pygame.draw.line(screen, (0, 0, 0), right_upper_arm_end, (right_lower_arm_end_x, right_lower_arm_end_y), 4)

    # Leg start
    left_leg_start = torso_bottom[0]-TORSO_WIDTH/4 , torso_bottom[1]
    right_leg_start = torso_bottom[0]+TORSO_WIDTH/4, torso_bottom[1]
    
    # Calculate and draw left leg
    left_upper_leg_angle = leg_angles_rad['left_upper']
    left_lower_leg_angle = leg_angles_rad['left_lower']

    left_upper_leg_end_x = torso_bottom[0] + UPPER_LEG_LENGTH * math.cos(left_upper_leg_angle)
    left_upper_leg_end_y = torso_bottom[1] + UPPER_LEG_LENGTH * math.sin(left_upper_leg_angle)
    left_upper_leg_end = (left_upper_leg_end_x, left_upper_leg_end_y)

    left_lower_leg_end_x = left_upper_leg_end_x + LOWER_LEG_LENGTH * math.cos(left_lower_leg_angle)
    left_lower_leg_end_y = left_upper_leg_end_y + LOWER_LEG_LENGTH * math.sin(left_lower_leg_angle)

    pygame.draw.line(screen, (0, 0, 0), left_leg_start, left_upper_leg_end, 4)
    pygame.draw.line(screen, (0, 0, 0), left_upper_leg_end, (left_lower_leg_end_x, left_lower_leg_end_y), 4)

    # Calculate and draw right leg
    right_upper_leg_angle = leg_angles_rad['right_upper']
    right_lower_leg_angle = leg_angles_rad['right_lower']

    right_upper_leg_end_x = torso_bottom[0] + UPPER_LEG_LENGTH * math.cos(right_upper_leg_angle)
    right_upper_leg_end_y = torso_bottom[1] + UPPER_LEG_LENGTH * math.sin(right_upper_leg_angle)
    right_upper_leg_end = (right_upper_leg_end_x, right_upper_leg_end_y)

    right_lower_leg_end_x = right_upper_leg_end_x + LOWER_LEG_LENGTH * math.cos(right_lower_leg_angle)
    right_lower_leg_end_y = right_upper_leg_end_y + LOWER_LEG_LENGTH * math.sin(right_lower_leg_angle)

    pygame.draw.line(screen, (0, 0, 0), right_leg_start, right_upper_leg_end, 4)
    pygame.draw.line(screen, (0, 0, 0), right_upper_leg_end, (right_lower_leg_end_x, right_lower_leg_end_y), 4)


# Main function
def main():
    current_frame = 0 #Current frame index
    #Array to hold keyframes
    keyframes = []
    animation = Animation(keyframes, 0.1) #This will be our Animation class' object
    running = True
    state = 0 # Can be 0, 1, 2 and corresponds to start_state, keyframe_view_state, and animation_state
    motion = ''
    # Starting y position for controls text 
    y = 10
    while running:
        # Clear the screen at the start of each frame
        screen.fill((255, 255, 224))  # Fill with light yellow color

        #Uncomment this if you want to see the axes
        #draw_axes(screen)  # Draw the x and y axes

        # Blit the title and controls text
        screen.blit(title_text, title_text_rect)
        
        # Blit each line of the controls text
        for line in controls_texts:
            text_surface = controls_font.render(line, True, BLACK)
            screen.blit(text_surface, (10, y))
            y += 30  # Increment y position for each line

        y = 10 #Reset y for next iteration
        
        dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    print("~Generating the jumping motion keyframes~")
                    keyframes = Keyframes('j').get_keyframes() #Get keyframes for the jumping motion
                    state = 1
                    motion = 'j'
                if event.key == pygame.K_w:
                    print("~Generating the waving motion keyframes~")
                    keyframes = Keyframes('w').get_keyframes() #Get keyframes for the jumping motion
                    state = 1
                    motion = 'w'
                if event.key == pygame.K_a:
                    print("~Animating Keyframes~")
                    state = 2
                    animation = Animation(keyframes, 0.12) #0.12 seconds per frame
                if state == 1 and event.key == pygame.K_RIGHT:
                    current_frame += 1
                    print(current_frame) #See the frame number
                    if current_frame >= len(keyframes):  # Loop back to the first frame
                        current_frame = 0
                elif state == 1 and event.key == pygame.K_LEFT:
                    current_frame -= 1
                    print(current_frame) #See the frame number
                    if current_frame < 0:  # Loop back to the last frame
                        current_frame = len(keyframes) - 1

        # Draw the current frame during the Keyframe viewing state
        if(state==1):
            keyframe = keyframes[current_frame]
            draw_stick_figure(screen, keyframe['position'], keyframe['arm_angles'], keyframe['leg_angles'])
        if(state==2):
            #animate using the keyframes array
            animation.update(dt)
            keyframe = animation.get_current_keyframe()
            draw_stick_figure(screen, keyframe['position'], keyframe['arm_angles'], keyframe['leg_angles'])
            if(motion=='j'):
                animation.pause_at_last_frame() #Pause for 3 seconds at the end of jump

        # # Test drawing the stick figure
        # draw_stick_figure(screen, (400, 300), 
        #               {'left_upper': 115, 'left_lower': 120, 'right_upper': -80, 'right_lower': -100},
        #               {'left_upper': 110, 'left_lower': 90, 'right_upper': 70, 'right_lower': 90})


        # Update display
        pygame.display.flip()

        # Control frame rate
        clock.tick(60)  # 60 frames per second

    pygame.quit()

if __name__ == "__main__":
    main()
