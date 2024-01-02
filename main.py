import pygame
import constants
import board
from connect4board import Connect4Board

gameboard = Connect4Board()

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
    pygame.display.set_caption("Connect 4")
    screen.fill(constants.WHITE)

    running = True
    winner = False
    print(f"Current Player: {gameboard.current_player}")

    font = pygame.font.SysFont(None, 55) #Initializes Font for Winner Message

    #Pygame Loop Shell
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and winner == False:
                x,y = pygame.mouse.get_pos()
                gx = x // 100
                gy = y // 100
                #Returns bool whether the player can place piece in column & lowest placeable row
                can_place, lowest = gameboard.can_place(gx, gy) 
                if can_place: 
                    gameboard.grid[lowest][gx]=gameboard.current_player #Sets corresponding matrix position with the player number
                    gameboard.place_circle(gx, lowest, screen) #Places piece in the lowest possible position in column
                    
                    winner = gameboard.check_winner() #Checks for winner
                    if winner is True:
                        text = font.render(f"Player {gameboard.current_player} Wins! Press R to RESET", True, constants.BLACK)
                        text_rect = text.get_rect(center=(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2))
                        screen.blit(text, text_rect) #Prints message in the middle of pygame GUI

                    gameboard.player_switch() #Switches player
                else: 
                    print("Invalid Row! Pick somewhere else!")
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: #Resetting the Game
                    print("Game Reset!")
                    screen.fill(constants.WHITE) 
                    board.drawGrid(screen)
                    gameboard.reset_board() #Resets the grid matrix and current player
                    winner = False

        board.drawGrid(screen)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()