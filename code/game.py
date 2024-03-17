import pygame
import sys

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Evolution of Life on Earth")

# Load species images and resize them to a consistent size
species_images = [
    pygame.transform.scale(pygame.image.load("prokaryotic_cell.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("cyanobacteria.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("eukaryote.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("choanoflagellate.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("flatworms.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("pikaia.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("haikouichthys.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("agnatha.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("placodermi.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("cephalaspis.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("coelacanth.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("panderichthys.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("tiktaalik.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("acanthostega.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("ichthyostega.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("hynerpeton.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("tulerpeton.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("pederpes.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("westlothiana.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("archaeothyris.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("hylonomus.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("dimetrodon.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("phthinosuchus.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("gorgonops.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("thrinaxodon.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("cynognathus.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("megazostrodon.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("juramaia.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("repenomamus.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("plesiadapis.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("carpolestes.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("aegyptopithecus.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("proconsul.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("sivapithecus.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("ouranopithecus.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("orrorin.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("ardipithecus.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("homo_erectus.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("neanderthal.png"), (200, 200)),
    pygame.transform.scale(pygame.image.load("homo_sapiens.png"), (200, 200)),
    # Load more species images here...
]

# Define species names
species_names = [
    "Prokaryotic Cell",
    "Cyanobacteria",
    "Eukaryote",
    "Choanoflagellate",
    "Flatworms",
    "Pikaia",
    "Haikouichthys",
    "Agnatha",
    "Placodermi",
    "Cephalaspis",
    "Coelacanth",
    "Panderichthys",
    "Tiktaalik",
    "Acanthostega",
    "Ichthyostega",
    "Hynerpeton",
    "Tulerpeton",
    "Pederpes",
    "Westlothiana",
    "Archaeothyris",
    "Hylonomus",
    "Dimetrodon",
    "Phthinosuchus",
    "Gorgonops",
    "Thrinaxodon",
    "Cynognathus",
    "Megazostrodon",
    "Juramaia",
    "Repenomamus",
    "Plesiadapis",
    "Carpolestes",
    "Aegyptopithecus",
    "Proconsul",
    "Sivapithecus",
    "Ouranopithecus",
    "Orrorin",
    "Ardipithecus",
    "Homo Erectus",
    "Neanderthal",
    "Homo Sapiens",
    # Add more species names here...
]

# Initialize variables
current_species_index = 0
evolved = False

# Font initialization
font = pygame.font.Font(None, 48)


# Function to display text on screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Main game loop
running = True
while running:
    screen.fill(BLACK)  # Changed background color to black

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RETURN:
                evolved = True
               
            elif event.key == pygame.K_r:  # For testing purposes, reload the game
                current_species_index = 0
                evolved = False
                

        # Check if mouse click event occurred
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if not evolved:
                # Check if Enter button clicked
                enter_button_rect = pygame.Rect(0, 0, 200, 50)
                enter_button_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                if enter_button_rect.collidepoint(mouse_pos):
                    evolved = True
                    
            else:
                # Check if Evolve button clicked
                evolve_button_rect = pygame.Rect(0, 0, 200, 50)
                evolve_button_rect.center = (SCREEN_WIDTH // 2, 500)
                if evolve_button_rect.collidepoint(mouse_pos):
                    current_species_index += 1
                    if current_species_index >= len(species_images):
                        # Reached the end, reset
                        current_species_index = 0
                        evolved = False
                    

                # Check if Exit button clicked
                exit_button_rect = pygame.Rect(20, SCREEN_HEIGHT - 70, 100, 50)
                if exit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
                    

                # Check if Again button clicked
                again_button_rect = pygame.Rect(SCREEN_WIDTH - 120, SCREEN_HEIGHT - 70, 150, 40)  # Adjusted size
                if again_button_rect.collidepoint(mouse_pos):
                    current_species_index = 0
                    evolved = False
                    

    if not evolved:
        # Display title
        draw_text("Evolution of Life on Earth", font, WHITE, SCREEN_WIDTH // 2, 100)

        # Display Enter button
        enter_button_rect = pygame.Rect(0, 0, 200, 50)
        enter_button_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        pygame.draw.rect(screen, WHITE, enter_button_rect)
        draw_text("ENTER", font, BLACK, *enter_button_rect.center)

    else:
        # Display species image and name
        species_image = species_images[current_species_index]
        screen.blit(species_image, (SCREEN_WIDTH // 2 - species_image.get_width() // 2, 100))
        draw_text(species_names[current_species_index].upper(), font, WHITE, SCREEN_WIDTH // 2, 350)

        # Display Evolve button
        evolve_button_rect = pygame.Rect(0, 0, 200, 50)
        evolve_button_rect.center = (SCREEN_WIDTH // 2, 500)
        pygame.draw.rect(screen, WHITE, evolve_button_rect)
        draw_text("EVOLVE", font, BLACK, *evolve_button_rect.center)

        # Display Exit button
        exit_button_rect = pygame.Rect(20, SCREEN_HEIGHT - 70, 100, 50)
        pygame.draw.rect(screen, WHITE, exit_button_rect)
        draw_text("EXIT", font, BLACK, exit_button_rect.centerx, exit_button_rect.centery)

       # Display Again button
        again_button_rect = pygame.Rect(SCREEN_WIDTH - 200, SCREEN_HEIGHT - 70, 180, 40)  # Adjusted size
        pygame.draw.rect(screen, WHITE, again_button_rect)
        draw_text("AGAIN", font, BLACK, again_button_rect.centerx, again_button_rect.centery)

    pygame.display.flip()

pygame.quit()
sys.exit()




