import pygame
import random

def draw_grid(screen, cell_size, rows, cols, color):
    for x in range(0, cols * cell_size, cell_size):
        pygame.draw.line(screen, color, (x, 0), (x, rows * cell_size))
    for y in range(0, rows * cell_size, cell_size):
        pygame.draw.line(screen, color, (0, y), (cols * cell_size, y))


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        #GRID COORDINATES
        cell_size = 32
        rows = 16
        cols = 20

        #MOLE COORDINATES
        mole_x = 0
        mole_y = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:

                    mole_x = random.randrange(0, cols) * cell_size
                    mole_y = random.randrange(0, rows) * cell_size

            screen.fill("light green")
            draw_grid(screen, cell_size, rows, cols, "black")
            screen.blit(mole_image, (mole_x,mole_y))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
