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


# interactive display with pygame
pygame.init()

# creation of a display window
screen = pygame.display.set_mode((600,600))

# table modelization

nb_lignes = 2
nb_colonnes = 3
ex_tabl = [[1, 2, 3], [4, 5, 6]]
click = 0


def tableau(obj):
    for x in range(0, len(obj)+1):
        pygame.draw.line(screen, (0, 0, 0), (x*200, 0), (x*200, 600))
    for y in range(0, len(obj[0]) + 1):
        pygame.draw.line(screen, (0, 0, 0), (0, y*200), (400, y*200))
    
    # affichage des chiffres
    font = pygame.font.SysFont(None, 45)
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            number = font.render(str(obj[i][j]), True, (0,0,0), background= None)
            numb_position = number.get_rect(center=(j*200+100, i*200+100))
            screen.blit(number, numb_position)


# boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # essai de construction d'une grille intéractive
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if click== 0:
                click = 1
                f_position = pygame.mouse.get_pos()
                case_f_i= f_position[1]//200
                case_f_j= f_position[0]//200
                case_f = obj[case_f_i][case_f_j]
            elif click==1:
                click=0
                s_position= pygame.mouse.get_pos()
                case_s_i= s_position[1]//200
                case_s_j= s_position[0]//200
                case_s = obj[case_s_i][case_s_j]
                swap(case_f,case_f)
                # ici je suis pas sûre que juste swaper suffit pour changer représentation mmm
            

            

# fond blanc
    screen.fill((255, 255, 255))

# affichage du tableau
    # tableau(ex_tabl)
    pygame.display.flip()


# fin pygame
pygame.quit()
sys.exit()


# ESSAI AVEC GRILLE 2/3

# interactive display with pygame
pygame.init()

# creation of a display window
screen = pygame.display.set_mode((600,600))

# table modelization

nb_lignes = 2
nb_colonnes = 3
ex_tabl = [[1, 2, 3], [4, 5, 6]]
click = 0

# fond blanc
screen.fill((255, 255, 255))
    
for x in range(0, len(ex_tabl[0])+1):#vérifier si je me suis pas trompée pour l'indice
    pygame.draw.line(screen, (0, 0, 0), (x*200, 0), (x*200, 400))
for y in range(0, len(ex_tabl) + 1):
     pygame.draw.line(screen, (0, 0, 0), (0, y*200), (600, y*200))
    
# affichage des chiffres
font = pygame.font.SysFont(None, 45)
for i in range(nb_lignes):
    for j in range(nb_colonnes):
        number = font.render(str(ex_tabl[i][j]), True, (0,0,0))
        numb_position = number.get_rect(center=(j*200+100, i*200+100))
        screen.blit(number, numb_position)


# boucle principale
running = True
while running:
    click=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # essai de construction d'une grille interactive
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button ==1:
                if click== 0:
                    click = 1
                    f_position = pygame.mouse.get_pos()
                    for i in range(nb_lignes):
                        if i*200<f_position[1] < (i+1)*200:
                            case_f_i= i
                    for j in range(nb_colonnes):
                        if j*200<f_position[0] < (j+1)*200:
                            case_f_j= j
                    case_f = ex_tabl[case_f_i][case_f_j]
                elif click==1:
                    click=0
                    s_position= pygame.mouse.get_pos()
                    for i in range(nb_lignes):
                        if i*200<s_position[1] < (i+1)*200:
                            case_s_i= i
                    for j in range(nb_colonnes):
                        if j*200<s_position[0] < (j+1)*200:
                            case_s_j= j
                    case_s_i= s_position[1]//200
                    case_s_j= s_position[0]//200
                    case_s = ex_tabl[case_s_i][case_s_j]
                    Grid.swap(case_f,case_s) #ici changer pour que ça modifie bien le tableau exemple
                    screen.fill((255, 255, 255),(case_f_j*200, case_f_i*200), ((case_f_j+1)*200, (case_f_i*200+1)*200))
                    screen.fill((255, 255, 255),(case_s_i*200, case_s_j*200), ((case_s_i+1)*200, (case_s_j+1)*200))
                    newcase_f = font.render(str(ex_tabl[case_f_i][case_f_j]), True, (0,0,0))
                    new_f_position = number.get_rect(center=(case_f_j*200+100, case_f_i*200+100))
                    screen.blit(newcase_f, new_f_position)
                    newcase_s = font.render(str(ex_tabl[case_s_i][case_s_j]), True, (0,0,0))
                    new_s_position = number.get_rect(center=(case_s_j*200+100, case_s_i*200+100))
                    screen.blit(newcase_s, new_s_position)
                    
                    
                
# affichage du tableau
    # tableau(ex_tabl)
    pygame.display.flip()


# fin pygame
pygame.quit()
sys.exit()

"""
    # FONCTION PYGAME POUR TOUTES LES GRILLES
    def display_pygame(tableau, to_do):

    # interactive display with pygame
        pygame.init()

    # creation of a display window
        screen = pygame.display.set_mode((1000,1000)) #à adapter selon taille de l'écran, jcp combien ça représente

    # table modelization
        click = 0
    #rajouter ici les variables pas def pour après si ça marche pas

    #lecture du nombre de lignes et colonnes du tableau
        lines= len(tableau)
        columns= len(tableau[0])
        grille= Grid(lines,columns,tableau)

    # fond blanc
        screen.fill((255, 255, 255))
    
        for x in range(0, len(columns)+1): #vérifier que je me suis pas trompée
            pygame.draw.line(screen, (0, 0, 0), (x*1000/columns, 0), (x*1000/columns, 1000)) #voir si je mets des moins pour aller vers le bas ? voir orientation
        for y in range(0, len(lines) + 1):
             pygame.draw.line(screen, (0, 0, 0), (0, y*1000/lines), (1000, y*600/lines))
    
    # affichage des chiffres
        font = pygame.font.SysFont(None, 45) # vérifier que police est ok pur l'affichage
        for i in range(lines):
            for j in range(columns):
                number = font.render(str(tableau[i][j]), True, (0,0,0))
                numb_position = number.get_rect(center=(j*600/columns+300/columns, i*600/lines+300/lines))
                screen.blit(number, numb_position)


    # boucle principale
        running = True
        swaps= 0
        while running:
            click=0
            if swaps == to_do and grille.Grid.is_sorted == True: #vérifier que swap change bien tableau mais aussi que on peut faire égalité
                screen.fill((255, 255, 255))
                text= font.render("YOU WIN", True, (0,0,0))
                # running = False : je pense pas que ce soit necessaire
            elif swaps == to_do and grille.Grid.is_sorted == False:
                screen.fill((0, 0, 0))
                text= font.render("YOU LOSE", True, (255,255,255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # essai de construction d'une grille interactive
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button ==1:
                        if click== 0:
                            click = 1
                            f_position = pygame.mouse.get_pos()
                            for i in range(nb_lignes):
                                if i*600/lines<f_position[1] < (i+1)*600/lines:
                                    case_f_i= i
                            for j in range(nb_colonnes):
                                if j*600/columns<f_position[0] < (j+1)*600/columns:
                                    case_f_j= j
                        elif click==1:
                            click=0
                            s_position= pygame.mouse.get_pos()
                            for i in range(nb_lignes):
                                if i*600/lines<s_position[1] < (i+1)*600/lines:
                                    case_s_i= i
                            for j in range(nb_colonnes):
                                if j*600/columns <s_position[0] < (j+1)*600/columns:
                                    case_s_j= j
                            grille.Grid.swap((case_f_i,case_f_j),(case_s_i,case_s_j)) #ici changer pour que ça modifie bien le tableau exemple
                            screen.fill((255, 255, 255),(case_f_j*600/columns, case_f_i*600/lines), ((case_f_j+1)*600/columns, (case_f_i*+1)*600/lines))
                            screen.fill((255, 255, 255),(case_s_j*600/columns, case_s_i*600/lines), ((case_s_j+1)*600/columns, (case_s_i+1)*600/lines))
                            newcase_f = font.render(str(grille[case_f_i][case_f_j]), True, (0,0,0))
                            new_f_position = number.get_rect(center=(case_f_j*600/columns+300/columns, case_f_i*600/lines+300/lines))
                            screen.blit(newcase_f, new_f_position)
                            newcase_s = font.render(str(grille[case_s_i][case_s_j]), True, (0,0,0))
                            new_s_position = number.get_rect(center=(case_s_j*600/columns+300/columns, case_s_i*600/lines+300/lines))
                            screen.blit(newcase_s, new_s_position)
                            swaps= swaps +1
                    
                    
                
    # affichage du tableau
        # tableau(ex_tabl)
            pygame.display.flip()


    # fin pygame
        pygame.quit()
        sys.exit()

