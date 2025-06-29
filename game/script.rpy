# script.rpy
# This script was generated based on the story context of an alternate ending
# to the duel on Mustafar between Anakin and Obi-Wan.

# -- Character Definitions ------------------------------------------------------
# Define the characters that will appear in the game.
# The narrator is "me", representing Anakin's first-person perspective.
# In Ren'Py, it's good practice to define characters and images in an init block.
init:
    # Define placeholder assets for backgrounds and character sprites.
    image bg mustafar_bridge = "placeholder_bg_mustafar.jpg"
    image obiwan_defeated = "placeholder_obiwan_defeated.png"
    image padme_arrives = "placeholder_padme_arriving.png"
    image sidious_arrives = "placeholder_sidious_arriving.png"

    # Define the characters that will appear in the game.
    define me = Character("[povname]", color="#e0ac28")
    define o = Character("Obi-Wan Kenobi", color="#6aadd3")
    define p = Character("Padmé Amidala", color="#c8a2c8")
    define s = Character("Darth Sidious", color="#c83232")

# -- Game Start -----------------------------------------------------------------
label start:
    # Set a default name for the player character.
    $ povname = "Anakin"

    # Play placeholder music and sound effects
    play music "placeholder_tense_music.ogg" loop
    play sound "placeholder_lava_rumble.ogg" loop

    # -- Scene Setup ------------------------------------------------------------
    # Set the scene on the volcanic world of Mustafar.
    scene bg mustafar_bridge
    show obiwan_defeated at center

    "My lightsaber hums, its heat a familiar comfort against the searing air of Mustafar."
    "He lies before me, defeated. My master. My brother."
    "I should feel triumphant, but all I feel is the burning rage that brought me here."

    o "Anakin... please. Let this end."

    me "No. It *begins* now. I see it all clearly. The Jedi lied. The Sith used me. But I’ll burn them *all* down."

    "I hold the blade inches from Obi-Wan’s throat. A flicker of pain, not my own, stops me."

    # Padmé arrives on the scene.
    show padme_arrives at right with dissolve
    p "Anakin!"

    "Padmé. Her voice cuts through the haze of my anger."
    "I deactivate my saber with a hiss."

    p "Is this what we fought for? Is this who you are now?"
    me "I did it for *you*. For us. To protect what we have."
    p "You *killed* children, Anakin!"

    "Her words are a physical blow. Before I can answer, the air booms."

    # Palpatine's ship arrives.
    hide padme_arrives
    show sidious_arrives at right with dissolve
    
    "His ship. He followed her. Or..."

    me "He followed you here?"
    p "He followed *you*."

    "A blast wave knocks Padmé from her feet. And then he is there, descending the ramp, his grin a mask of evil."

    s "My apprentice. You’ve done well. Now finish it. Kill the Jedi — and the woman — and rise as Lord Vader."

    "His words echo in my mind. Kill Obi-Wan. Kill Padmé. Rise."
    "My blade ignites once more. This is the moment of choice. The galaxy holds its breath."

    # -- The Pivotal Choice -----------------------------------------------------
    # A menu presents the player with a critical decision that will lead to
    # one of two different endings.
    menu:
        "I am the master of my own destiny.":
            me "I’m *no one’s* pawn!"
            jump plottwist_end

        "This is my destiny. I will have peace.":
            me "Yes, my master."
            jump normal_end


# -- Endings --------------------------------------------------------------------

# -- Plot Twist Ending ----------------------------------------------------------
# This is the outcome if the player chooses to defy Darth Sidious.
label plottwist_end:
    "I turn my blade on Sidious, the true enemy."
    "His smile vanishes, replaced by a snarl of fury."

    s "So be it... traitor."

    "He raises his hands, and lightning arcs between them. But I am ready."
    "I leap, not away, but towards him. Towards my true fate."
    "The war for my soul is not over. It has just gone rogue."

    scene black
    "To be continued..."
    return


# -- Normal Ending --------------------------------------------------------------
# This is the outcome if the player chooses to obey Darth Sidious.
label normal_end:
    "I turn back to Obi-Wan. His eyes are filled with a sorrow that mirrors my own."
    "But sorrow is a weakness. The Jedi are weak. I am not."

    me "Goodbye, Master."

    "The blue blade falls. There is no sound but the sizzle of energy and the end of a friendship."
    "I turn to Padmé, her face a portrait of horror."

    me "He turned you against me."
    p "You have done that yourself."

    "I raise my hand, and she crumples to the ground, unconscious. She will learn. They will all learn."
    "I kneel before my true master."

    me "The Jedi are no more. I am yours, Lord Vader."
    s "Rise, my friend. Rise and bring order to my galaxy."

    scene black
    "The galaxy falls to darkness..."
    return