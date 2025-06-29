# -- Character Definitions -----------------------------------------------------------
# Defines the characters that will appear in the game. The narrator is set to
# Anakin's perspective, so any text not assigned to a character will be his thoughts.
define narrator = Character(None, kind=nvl)
define obi = Character("Obi-Wan Kenobi", color="#66a3ff")
define ana = Character("Anakin Skywalker", color="#ff4d4d")
define pad = Character("Padmé Amidala", color="#ffffff")
define pal = Character("Darth Sidious", color="#cc0000")


# -- Image Placeholders --------------------------------------------------------------
# Defines placeholder images for backgrounds and characters.
# In a real project, these would be replaced with actual image files.
image bg mustafar = "images/mustafar_bg.jpg"
image obiwan_injured = "images/obiwan_injured.png"
image padme_worried = "images/padme_worried.png"
image palpatine_smug = "images/palpatine_smug.png"


# -- The Game Starts Here ------------------------------------------------------------

label start:
    # -- Scene Setup -----------------------------------------------------------------
    # Establishes the initial scene with a background, music, and NVL mode for
    # first-person narration.
    scene bg mustafar
    play music "audio/tense_music.ogg" loop
    window show
    nvl clear

    # -- Introduction from Anakin's POV ----------------------------------------------
    "The air tasted of ash and failure. My master, my friend, lay defeated on the black sand, his robes charred, his body broken by my hand."
    "He had the high ground, just as he always preached. But he underestimated my pain. My power."

    # -- Display Obi-Wan -------------------------------------------------------------
    show obiwan_injured at center
    
    obi "It's over, Anakin! I have the high ground!"
    
    "His words were a faint echo of a lesson I had long since unlearned. I didn't hesitate."
    "A feint, a roll, a surge of motion under his leap. Steel met flesh. His lightsaber flew from his grasp, and he tumbled to the ground."

    show obiwan_injured at center with dissolve

    ana "You taught me to trust my instincts. Bad lesson."
    obi "(gasping) Anakin... please. Let this end."
    ana "No. It *begins* now. I see it all clearly. The Jedi lied. The Sith used me. But I’ll burn them *all* down."

    "My blade hummed inches from his throat. The heat, the rage... it was all I had left. But then..."

    # -- Padmé's Arrival -------------------------------------------------------------
    hide obiwan_injured
    show padme_worried at center
    
    "A voice. Her voice. Cutting through the haze of my fury."
    
    pad "Anakin!"

    "I deactivated my saber with a hiss. She stood at the edge of the platform, her face a mask of horror and disbelief."

    pad "(shaking) Is this what we fought for? Is this who you are now?"
    ana "I did it for *you*. For us. To protect what we—"
    pad "(interrupting) You *killed* children, Anakin!"

    "Her words were a physical blow. Before I could answer, the air boomed. A ship descended, flooding the ridge in a sinister red light."

    # -- Palpatine's Arrival ---------------------------------------------------------
    hide padme_worried
    show palpatine_smug at center

    ana "He followed you here?"
    pad "(softly) He followed *you*."

    "A blast wave knocked her from her feet. I turned, my eyes blazing, as Sidious descended the ramp, a grotesque grin plastered on his face."

    pal "My apprentice. You’ve done well. Now finish it. Kill the Jedi — and the woman — and rise as Lord Vader."

    "His words hung in the sulfurous air. Kill Obi-Wan. Kill... Padmé. My wife. The mother of my child."
    "My lightsaber ignited, its blue flame a stark contrast to the hellscape around us. My destiny stood before me. But which one?"

    # -- The Pivotal Choice ----------------------------------------------------------
    # This menu presents the player with a critical choice that determines the ending.
    menu:
        "Embrace my destiny as Vader.":
            jump normal_end

        "I will not be a pawn. Not anymore.":
            jump plottwist_end


# -- Normal Ending -------------------------------------------------------------------
# This is the outcome if the player chooses to obey Palpatine.
label normal_end:
    "A cold clarity washed over me. The Jedi were weak. Padmé did not understand. Only power mattered."
    "I turned to Obi-Wan. There was no malice in the movement, only a grim finality."
    
    show obiwan_injured at center
    
    ana "Goodbye, Master."
    
    "The blue blade swung. He didn't even try to resist."
    
    hide obiwan_injured
    
    "Then, I faced Padmé. Her eyes, wide with terror, would haunt me forever. But the future of the galaxy required sacrifice."
    
    show padme_worried at center
    
    ana "I am sorry."
    
    "Another swing. Silence fell upon Mustafar, broken only by the roar of the lava and the satisfied chuckle of my new master."
    
    hide padme_worried
    show palpatine_smug at center
    
    pal "Rise, Lord Vader."
    
    "And I did. Over the ashes of my past, I rose. The galaxy would learn to fear my name."
    
    nvl clear
    return


# -- Plot Twist Ending ---------------------------------------------------------------
# This is the outcome if the player chooses to defy Palpatine.
label plottwist_end:
    "His words echoed in my mind. Kill the Jedi... and the woman. My master... and my wife."
    "He saw them as obstacles. Pawns to be swept from the board. But he was wrong."
    "Padmé was everything. The Jedi... the Sith... they were the illusion."
    
    "My blade was ignited. But this time, I turned it on Palpatine."

    show palpatine_smug at center
    
    ana "(roaring) I’m *no one’s* pawn!"

    "I lunged, not as a Jedi, not as a Sith, but as a man with nothing left to lose but the woman he loved."
    "Sidious recoiled, his grin replaced by a snarl of surprise. He was powerful, but my rage was a fire he had stoked for too long."
    "I grabbed Padmé, pulling her toward her ship as I deflected the lightning from his fingertips."
    
    "We escaped into the shadows of the galaxy, leaving Mustafar and the broken bodies of my past behind."
    "The galaxy would think Anakin Skywalker was dead. Let them. A new path lay before me, one forged in fire and fury, with only one law: protect her."
    
    nvl clear
    return