#imports
import matplotlib.pyplot as plt
import pygame
import sys

class Graphics:
#function to display the grid with plt
    def display_plt(grid):
        #initialisation des paramètre
        fig, ax = plt.subplots()
        # inversion of the order of the elements in order for the display not to be reversed
        grid.reverse()
    #creation of compartments with text
        ax.set_xticks(range(len(grid[0]) + 1))
        ax.set_yticks(range(len(grid)+1))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        for i in range(len(grid[0])):
            for j in range (len(grid)):
                ax.text( i+0.5, j+0.5, str(grid[j][i]), fontdict=None)
        # display
        plt.grid(True,linewidth=2)
        plt.show()

    #construction exemple
    def construction_ex():
        lignes= int(input("Saisir le nombre de lignes: "))
        colonnes= int(input("Saisir le nombre de colonnes: "))
        example=[]
        new= []
        for i in range(lignes):
            for j in range(colonnes):
                new = new + [i*colonnes + j + 1]
            example = example + [new]
            new= []
        return example
"""
#application

app= construction_ex()
display_plt(app)

"""

    # FONCTION PYGAME POUR TOUTES LES GRILLES
    def display_pygame(tableau, to_do):

    # interactive display with pygame
        pygame.init()

    # creation of a display window
        screen = pygame.display.set_mode((1000,1000)) #à adapter selon taille de l'écran, jcp combien ça représente

    # table modelization
        click = 0
        swaps = 0
    #rajouter ici les variables pas def pour après si ça marche pas

    #lecture du nombre de lignes et colonnes du tableau
        lines= len(tableau)
        columns= len(tableau[0])
        grille= Grid(lines,columns,tableau)

    # fond blanc
        screen.fill((255, 255, 255))
    
        for x in range(0, columns+1): #vérifier que je me suis pas trompée
            pygame.draw.line(screen, (0, 0, 0), (x*1000/columns, 0), (x*1000/columns, 1000)) #voir si je mets des moins pour aller vers le bas ? voir orientation
        for y in range(0, lines + 1):
             pygame.draw.line(screen, (0, 0, 0), (0, y*1000/lines), (1000, y*1000/lines))
    
    # affichage des chiffres
        font = pygame.font.SysFont(None, 45) # vérifier que police est ok pur l'affichage
        for i in range(lines):
            for j in range(columns):
                number = font.render(str(tableau[i][j]), True, (0,0,0))
                numb_position = number.get_rect(center=(j*1000/columns+500/columns, i*1000/lines+500/lines))
                screen.blit(number, numb_position)


    # boucle principale
        running = True
        success = grille.is_sorted
        while running:
            if swaps == to_do and success == True: #vérifier que swap change bien tableau mais aussi que on peut faire égalité
                screen.fill((255, 255, 255))
                text= font.render("YOU WIN", True, (0,0,0))
                place= text.get_rect(center=(500,500))
                screen.blit(text,place)
            elif swaps == to_do and success == False:
                screen.fill((0, 0, 0))
                text= font.render("YOU LOSE", True, (255,255,255))
                place= text.get_rect(center=(500,500))
                screen.blit(text,place)
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
            # essai de construction d'une grille interactive
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button ==1:
                            if click== 0:
                                click = 1
                                f_position = pygame.mouse.get_pos()
                                for i in range(lines):
                                    if i*1000/lines<f_position[1] < (i+1)*1000/lines:
                                        case_f_i= i
                                for j in range(columns):
                                    if j*1000/columns<f_position[0] < (j+1)*1000/columns:
                                        case_f_j= j
                            elif click==1:
                                click=0
                                s_position= pygame.mouse.get_pos()
                                for i in range(lines):
                                    if i*1000/lines<s_position[1] < (i+1)*1000/lines:
                                        case_s_i= i
                                for j in range(columns):
                                    if j*1000/columns <s_position[0] < (j+1)*1000/columns:
                                        case_s_j= j
                                grille.swap((case_f_i,case_f_j),(case_s_i,case_s_j)) #ici changer pour que ça modifie bien le tableau exemple
                                screen.fill((255, 255, 255),(int(case_f_j*1000/columns) + 1, int(case_f_i*1000/lines) + 1, int((case_f_j+1)*1000/columns)- 1, int((case_f_i*+1)*1000/lines)- 1))
                                screen.fill((255, 255, 255),(int(case_s_j*1000/columns) + 1, int(case_s_i*1000/lines) + 1, int((case_s_j+1)*1000/columns)-1, int((case_s_i*+1)*1000/lines)- 1))
                                newcase_f = font.render(str(grille.state[case_f_i][case_f_j]), True, (0,0,0))
                                new_f_position = number.get_rect(center=(case_f_j*1000/columns+500/columns, case_f_i*1000/lines+500/lines))
                                screen.blit(newcase_f, new_f_position)
                                newcase_s = font.render(str(grille.state[case_s_i][case_s_j]), True, (0,0,0))
                                new_s_position = number.get_rect(center=(case_s_j*1000/columns+500/columns, case_s_i*1000/lines+500/lines))
                                screen.blit(newcase_s, new_s_position)
                                swaps= swaps +1
                    
            pygame.display.flip()


    # fin pygame
        pygame.quit()
        sys.exit()

