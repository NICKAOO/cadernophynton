# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("naruto")

define o = Character("orochimaru")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene fundo 1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show naruto1 
    n "Ei viajante me ajude a derrotar o inimigo!."
    n "ele é muito forte."
    hide naruto1

    show orochimaru2
    o "esta preparado para morrer?"
    hide orochimaru2
    show orochimarus
    o "aaaaaaah"
    hide orochimarus
    show naruto
    n "sucumba"


    # These display lines of dialogue.

    # This ends the game.

    return
