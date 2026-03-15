label sacrifice_dream: 
    # play music "audio/arunangshubanerjee-indian-train-sound-from-vestibule-realistic-interior-noise-314562.mp3"
    
    scene bg altar overgrown
    show vincent ancient at right
    with dissolve  
    "You are dreaming of the Binding of Isaac."
    "You are at the top of the mountain, near the altar. Everything is covered in green."
    "Down there on the slope you see Abraham and Isaac slowly climbing a rocky path. There are some crumbling steps here and there, almost devoured by overgrown plants, to make their path easier."

    hide vincent ancient
    scene sacrifice scene
    "You're standing on top of pyramid, wearing catholic prelate robe, surrounded by men in white tiaras and red and gold mantles. This is not their place. This is not the place for latin chants."
    "This is not a place for you. You never held an obsidian dagger in you hand and you don't know the rite, but you make a step closer."
    menu:
        "Make a sacrifice.":
            "You rise the dagger. There is a lump in your throat. You're trying to stop yoursefl but you can't."
    menu:
        "Make a sacrifice.":
            "You fell completely powerless. Thomas is standing next to you with a blank face, waiting when you will stab Aldo with a dagger."
    v "Thomas! Help me, Thomas!"
    v "Please, please help me, stop this, I can't, we cant..."
    "Thomas does nothing."
    menu:
        "Make a sacrifice.":
            "Your body isn't obeying you, and the dagger falls down."
    scene bg black
    "You wake up."
    "{cps=20}Breath in.{/cps}"
    "You feel a body lying near you, warm, breathing."
    "{cps=20}Breath out.{/cps}"
    "sacrifice_dream scene end"
return