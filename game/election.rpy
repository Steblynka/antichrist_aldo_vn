default francis = True
default clement = True
default ignatius = True

label election:
    scene bg election
    t "Quo nomine vic vocatis?"
    menu:
        "Choose a name"
        "Clement":
            $clement=False
        "Ignatius":
            $ignatius=False
        "Francis": 
            $francis=False
    "No, that is not the one. Choose different."
    menu:
        "Choose a name"
        "Clement" if clement:
            $clement=False
        "Ignatius" if ignatius:
            $ignatius=False
        "Francis" if francis: 
            $francis=False
    "Are you not listening? This is not who you are."
    menu:
        "Choose a name"
        "Clement" if clement:
            $clement=False
        "Ignatius" if ignatius:
            $ignatius=False
        "Francis" if francis: 
            $francis=False
    "{shader=jitter:u__jitter=1.0, 3.0}Oh my child, you thought you could change?{/shader}"
    menu:
        "Choose a name"
        "{color=#f00}Peter Elijah{/color}":
            play music "/audio/choose a name.mp3"
            "Here you are."
    "bla bla bla election end"        
return    

