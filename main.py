import pygame, sys
import mysql.connector
from button import Button

pygame.init()                                                       # Inizializza la finestra

SCREEN = pygame.display.set_mode((1280, 720))                       # Main Menu
pygame.display.set_caption("Hangman Game")                          # Titolo della finestra

BACKGROUND = pygame.image.load("img.png")                           # Carica il background
FONT = pygame.font.SysFont("Arial", 80, bold=True)                  # Imposta il font



def playMenu() -> None:                                             # Funzione per il Menu di Gioco
    while True:
        SCREEN.fill("black")

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_TEXT = FONT.render("PLAY SCREEN", True, "white")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=FONT, 
                            base_color="white", 
                            hovering_color="green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    mainMenu()

        pygame.display.update()

def statsMenu() -> None:                                            # Funzione per il Menu delle Statistiche
    while True:
        SCREEN.fill("black")

        STATS_MOUSE_POS = pygame.mouse.get_pos()

        STATS_TEXT = FONT.render("STATS SCREEN", True, "white")
        STATS_RECT = STATS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(STATS_TEXT, STATS_RECT)

        STATS_BACK = Button(image=None, pos=(640, 460),
                            text_input="BACK", font=FONT,
                            base_color="white", 
                            hovering_color="green")

        STATS_BACK.changeColor(STATS_MOUSE_POS)
        STATS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if STATS_BACK.checkForInput(STATS_MOUSE_POS):
                    mainMenu()
        
        pygame.display.update()

def mainMenu() -> None:                                             # Funzione per il Menu Principale
    while True:
        SCREEN.blit(BACKGROUND, (0, 0))                             # Imposta il background

        MOUSE_POS = pygame.mouse.get_pos()                          # Posizione del mouse

        PLAY_BUT = Button(image=pygame.image.load("rect.png"),      # Bottone per giocare
                    pos=(1050, 80), text_input="PLAY", font=FONT,
                    base_color="black", hovering_color="red")

        STATS_BUT = Button(image=pygame.image.load("rect.png"),     # Bottone per le statistiche
                    pos=(1050, 190), text_input="STATS", font=FONT,
                    base_color="black", hovering_color="red")

        QUIT_BUT = Button(image=pygame.image.load("rect.png"),      # Bottone per uscire dal gioco
                    pos=(1050, 300), text_input="QUIT", font=FONT, 
                    base_color="black", hovering_color="red")

        for button in [PLAY_BUT, STATS_BUT, QUIT_BUT]:                                   
            button.changeColor(MOUSE_POS)                           # Cambia il colore del bottone
            button.update(SCREEN)                                   # Aggiorna il bottone

        for event in pygame.event.get():                            # Eventi
            if event.type == pygame.QUIT:                           # Se si preme il tasto X chiude la finestra
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:                
                if QUIT_BUT.checkForInput(MOUSE_POS):               
                    pygame.quit()
                    sys.exit()                                      # Se si preme il bottone QUIT chiude la finestra
                if STATS_BUT.checkForInput(MOUSE_POS):
                    statsMenu()                                     # Se si preme il bottone STATS apre il menu delle statistiche
                if PLAY_BUT.checkForInput(MOUSE_POS):
                    playMenu()                                      # Se si preme il bottone PLAY apre il menu di gioco

        pygame.display.update()                                     # Aggiorna lo schermo

if __name__ == "__main__":
    mainMenu()