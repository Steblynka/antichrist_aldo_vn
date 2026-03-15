# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Vincent")
define t = Character("Thomas")
define a = Character("Aldo")



# The game starts here.

label start:

    jump sacrifice_dream
    jump train_scene
    jump make_a_choice_scene
    # This ends the game.
    
return


    
    