# This is the main script file for the Ren'Py visual novel.
# It contains the story, character definitions, and game logic.

# -- Character Definitions -----------------------------------------------------
# Define the characters that will appear in the game.
# The color codes are for the character names in the dialogue box.

define a = Character("Anakin", color="#c8c8ff")
define o = Character("Obi-Wan", color="#add8e6")
define p = Character("Padmé", color="#ffc0cb")
define s = Character("Sidious", color="#ff0000")
define narrator = Character(None, kind=nvl, what_prefix='"', what_suffix='"')


# -- Image and Asset Definitions -----------------------------------------------
# Define placeholder images for backgrounds and characters.
# In a real project, you would replace these with your actual image files.

image bg mustafar = "images/bgs/mustafar_bridge.jpg"
image bg black = "images/bgs/black_screen.png"

image anakin neutral = "images/chars/anakin_neutral.png"
image anakin angry = "images/chars/anakin_angry.png"
image anakin conflicted = "images/chars/anakin_conflicted.png"

image obiwan neutral = "images/chars/obiwan_neutral.png"
image obiwan injured = "images/chars/obiwan_injured.png"

image padme worried = "images/chars/padme_worried.png"
image padme horrified = "images/chars/padme_horrified.png"

image sidious smiling = "images/chars/sidious_smiling.png"


# -- The Game Starts Here ------------------------------------------------------

label start:

    # -- Scene Setup -----------------------------------------------------------
    # Set the initial scene with background, music, and character sprites.

    scene bg mustafar
    play music "audio/music/epic_battle.ogg" fadein 1.0

    show anakin angry at center
    show obiwan neutral at left

    # -- Introduction Dialogue -------------------------------------------------

    o "It's over, Anakin! I have the high ground!"

    a "You underestimate my power!"

    o "Don't try it."

    # -- The Duel's Climax -----------------------------------------------------
    # The script follows the divergent path from the test_scenario.md.

    narrator nvl "But this time, Anakin doesn't hesitate. He feints left, rolls through the ash, and surges under the leap with an upward slash."

    play sound "audio/sfx/lightsaber_clash.ogg"
    
    hide obiwan neutral
    show obiwan injured at left
    
    o "Argh!"

    narrator nvl "Obi-Wan's lightsaber flies from his hand. He tumbles to the ground, clutching a burned shoulder, coughing through the sulfur."

    show anakin angry at center
    
    a "You taught me to trust my instincts. Bad lesson."

    o "Anakin… please. Let this end."

    a "No. It *begins* now. I see it all clearly. The Jedi lied. The Sith used me. But I’ll burn them *all* down."

    narrator nvl "He holds the blade inches from Obi-Wan’s throat — but stops. A flicker of pain flashes across his face."

    # -- Padmé's Arrival -------------------------------------------------------

    show padme worried at right
    
    p "Anakin!"

    hide anakin angry
    show anakin conflicted at center

    narrator nvl "Anakin turns, and his saber deactivates with a hiss. Obi-Wan watches, helpless."

    p "Is this what we fought for? Is this who you are now?"

    a "I did it for *you*. For us. To protect what we—"

    p "You *killed* children, Anakin!"

    narrator nvl "Anakin flinches. Suddenly — the air *booms* as Palpatine’s ship descends behind them. Red light floods the ridge."

    # -- Palpatine's Arrival and the Pivotal Choice ----------------------------
    
    play sound "audio/sfx/ship_landing.ogg"
    
    show sidious smiling at right
    hide padme worried
    show padme horrified at farright

    a "He followed you here?"

    p "He followed *you*."

    s "My apprentice. You’ve done well. Now finish it. Kill the Jedi — and the woman — and rise as Lord Vader."

    narrator nvl "Anakin stares at Obi-Wan. Then at Padmé. Then at Sidious. He ignites his blade."

    # -- The Menu: Player's Choice ---------------------------------------------
    # This is the pivotal choice that determines the ending.

    menu:
        "\"I am no one's pawn!\"":
            jump plottwist_end

        "\"I will do what I must.\"":
            jump normal_end


# -- Endings -------------------------------------------------------------------

label plottwist_end:

    # -- Plot Twist Ending -----------------------------------------------------
    # Anakin turns on Palpatine, choosing his own path.

    show anakin angry at center
    
    a "I’m *no one’s* pawn!"

    narrator nvl "He turns his blade on Palpatine, who recoils in shock. A furious battle erupts, not of Jedi versus Sith, but of pure, untamed rage against calculated evil."
    
    play sound "audio/sfx/lightsaber_ignite.ogg"
    
    narrator nvl "Anakin, fueled by betrayal, forces Sidious back. He grabs Padmé, pulling her toward his ship."

    a "We're leaving. Now!"

    narrator nvl "They escape into the shadows of the galaxy, leaving both Jedi and Sith behind. The galaxy believes Anakin Skywalker is dead. But in the Outer Rim, whispers begin of a warrior in black who fights both sides, his fury burning hotter than any star."

    scene bg black
    "The war for the soul of the galaxy is not over. It’s only gone rogue."

    return


label normal_end:

    # -- Normal Ending ---------------------------------------------------------
    # Anakin embraces the dark side and becomes Darth Vader.

    show anakin angry at center
    
    a "I will do what I must."

    narrator nvl "Anakin turns to Obi-Wan, his eyes burning with cold fire. There is no hesitation."
    
    play sound "audio/sfx/lightsaber_ignite.ogg"
    play sound "audio/sfx/final_blow.ogg"

    hide obiwan injured
    
    p "Anakin, no!"

    narrator nvl "He strikes down his former master. He then turns to Padmé, a single tear falling down his cheek before his expression hardens into a mask of pure darkness."

    s "Excellent, Lord Vader. Rise."

    narrator nvl "Anakin Skywalker is dead. In his place stands Darth Vader, the Emperor's new fist. The hope of the galaxy dies with him on the black sands of Mustafar."

    scene bg black
    "The future is now set. The Empire will reign. There is no one left to stop it."

    return