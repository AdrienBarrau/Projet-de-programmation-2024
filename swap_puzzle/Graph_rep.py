#imports
import matplotlib.pyplot as plt 
import matplotlib.axes as ax
import pygame
import sys

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
def construction_ex(lignes, colonnes):
    example=[]
    new= []
    for i in range(lignes):
        for j in range(colonnes):
            new = new + [i*colonnes + j + 1]
        example = example + [new]
        new= []
    return example

#application
app= construction_ex(7,12)
display_plt(app)


# interactive display with pygame
pygame.init()

# creation of a display window
screen = pygame.display.set_mode((400,600))

# table modelization

nb_lignes = 2
nb_colonnes = 3
ex_tabl = [[1, 2, 3], [4, 5, 6]]
click = 0

"""
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
"""

for x in range(0, len(ex_tabl)+1):
    pygame.draw.line(screen, (0, 0, 0), (x*200, 0), (x*200, 600))
for y in range(0, len(ex_tabl[0]) + 1):
    pygame.draw.line(screen, (0, 0, 0), (0, y*200), (400, y*200))
    
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
