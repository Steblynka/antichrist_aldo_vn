default called_thomas = False
default yelled_at_children = False
default can_check_news = False
default show_call_thomas=True
default can_call_thomas = True
default can_call_cecretary = True
default calls_ctr = 0
default news_ctr = 0

label train_scene: 
    play music "audio/arunangshubanerjee-indian-train-sound-from-vestibule-realistic-interior-noise-314562.mp3"
    
    scene bg train with hpunch
    show vincent neutral at left
    with dissolve  
    v "You've been naughty, Y/N. Actually, realy naughty and not in a fun way"

    "The direct connection from Udine to Roma Termini takes little under six hours. You sit in the window seat, watching the fields glow in the sun of the early afternoon."
    scene bg window_view 
    "What a joy, to witness such glory of the Lord! Hosanna, Hosanna in the highest heaven! There is a pit in your stomach. You feel like throwing up."
    scene bg train with hpunch
    show vincent neutral at left
    with dissolve

    v "fuck my life"

    while calls_ctr < 4:
        call phone_call_1         

    "train scene end"
return    


label phone_call_1:
    menu:
        "You're staring at your phone screen."
        "Call Aldo":
            "The phone rings and rings, but there is no reply."
            "Your heart sinks further."
            $calls_ctr=calls_ctr+1
        "Call Tedesco":
            "The call goes into voicemail. Tedesco’s recorded voice is loud, jovial and full of energy."
            $calls_ctr=calls_ctr+1
        "Call Thomas" if show_call_thomas: 
            if can_call_thomas:
                jump call_thomas
            else:    
                "You scroll down to Thomas' contact. You're not sure what to ask."
                "You press 'back' and stare at your phone screen again."
        "Call secretary" if can_call_cecretary:    
            jump secretary_call
        "Check the news" if can_check_news:
            jump check_news
            
return

label check_news:
    "the pope got called 'antichrist' 15 times on twitter today"
    "there's funny video montage of cardinal Lawrence with a pink sparkly filter put over him. "
return    

label secretary_call:
    "The call connects after just a few rings." 
    show secretary neutral at right
    with dissolve
    "After your frantic inquiry, the voice on the other side informs you that his Eminence Tedesco had a medical emergency during the meeting with his Holiness, who took the rest of the day of to pray for him, but is alright himself."
    "You insist on the secretary checking in on Aldo, but they refuse to bother the Pope, who is currently praying in private and asked to not disturb."
    "Wave of joy and despair overflows you."
    "{cps=20}Breath in.{/cps}"
    "{cps=20}One.{/cps}"
    "{cps=20}Two.{/cps}"
    "{cps=20}Three.{/cps}"
    "{cps=20}Four.{/cps}" 
    "{cps=20}Breath out.{/cps}"
    v "Thank you, monsignor. Sorry for bothering you."
    "You hang up the call."
    $can_call_cecretary=False
    $calls_ctr=calls_ctr+1
    $can_check_news=True
    hide secretary
return

label phone_call:
    menu:
        "What should I do?"

        "Put the phone down.":
            "put the fucking phone down!!."

        "Call Aldo.":
            "there's no answer."
            $calls_ctr=calls_ctr+1
        
        "Call Thomas." if called_thomas == False:
            jump call_thomas
        "Yell at children" if calls_ctr >2 and yelled_at_children==False:
            jump yell_at_children    

    label after_menu:
        "bruhhhhhh."
return

label call_thomas:
    "You call Thomas. He answers almost immediately, sounding calm and normal, pleasantly surprized to hear you at first"
    show thomas neutral at right
    t "Vincent, hello! I wasn't expecting you to call"
    "You're trying to not sound desperate"
    v "(asks to check on aldo)"

    t "sure"

    t "he's sleeping"

    v "ok thx"

    hide thomas
    $called_thomas = True
    $show_call_thomas=False
    $can_call_thomas=False
return

label yell_at_children:
    v "TURN YOUR VOLUME OFF FOR CHRIST'S SAKE"
    "They look annoyed and slightly uneasy; their parents hurry tell them to "
    "You immediatelly regret this outburst. You could have asked nicely"
    $yelled_at_children = True
return    

label check_news2:
    "You're trying to check the news."

    if news_ctr == 0:
        "There's no news."
return    