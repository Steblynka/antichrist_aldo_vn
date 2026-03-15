default can_make_choice = False
default leave_ctr = 0

label make_a_choice_scene:
    scene bg bedroom
    show vincent neutral at left
    "Something is wrong. You feel both dread and happiness reaching their highest points as you passed the threashold. The room is dimly lit, and the windows is open. The wind gently rustles papers on the desk"
    "You see Aldo laying on his bed motionless"
    "You know what happened. There are empty blisters from the sleeping pills in the trash bin near the desk."
    menu:
        "Come closer.":
            jump go_to_bed
    
    hide vincent

    label go_to_bed:
        scene bg bed

    "He is still breathing"
    label choice1:
        menu:
            "You know what you need to do."
            "Look closer":
                jump look_closer
            "Pray":
                jump pray
            "Leave":
                jump leave
            "Make a choice" if can_make_choice:
                jump choice_final


return

label look_closer:
    scene bg aldos_face
    "You leaned closer. He looks tired. So, so tired. His eyelids are red like he was crying recently. Last time you've seen him this close, you've called him \"My love\". You need to make a choice."
    $can_make_choice=True
    scene bg bed
    jump choice1
return

label pray:
    "You're trying to pray. This time, there is no answer.
    Eloi, Eloi, lama sabachthani?"
    $can_make_choice=True
    jump choice1
return

label leave:  
    if leave_ctr==0:
        "You're not moving."
    else:
        if leave_ctr==1: 
            "You can't leave."
        else:
            if leave_ctr>=2:     
                "Dont you understand? You can't leave."     
    $leave_ctr=leave_ctr+1   
    jump choice1  
return

label choice_final:
    scene bg aldos_face
    "The wind slowly falls down through the window, pooling at the foot of the bed before flowing through the darkened room, flitting over your legs and then flooding into the shadows, The night is silent, still, and you have a choice to make."
    "It has been over three hours, enough time for the barbiturates to reach full toxicity, but if you have something, it is time. The world is still and silent outside of the sanctuary, and will stay so for as long as needed."
    "The wind whispers from the corners of the room, picking up loose letters before putting them back down and moving to the notes, the homilies, the diary, the ideas and memories. But they are not the firstborn the mashhit had came to take today."
    "You gently trail your fingers down the face of the old man laying in the bed, unmooving. There is a choice to be made, and until it's done the world will hold its breath, waiting for its absolution."
    menu:
        "It's him, or the world. What do you choose?"
        "Choose love":
            jump choice_end
        "Choose love":
            jump choice_end
    label choice_end:
        "scene final"

return