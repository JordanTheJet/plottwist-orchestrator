# Character definitions
# We define the characters that will appear in our game.
# The color codes are for the character names in the dialogue.
define a = Character("Anakin", color="#c8c8ff")
define o = Character("Obi-Wan", color="#add8e6")
define p = Character("Padmé", color="#f0e68c")
define s = Character("Sidious", color="#ff0000")
define narrator = Character(None, kind=nvl, what_prefix='"', what_suffix='"')

# Image definitions
# Placeholder images for backgrounds and characters.
# In a real project, you would replace these with actual image file paths.
image bg mustafar_bridge = "images/bgs/mustafar_bridge.png"
image bg palpatine_ship = "images/bgs/palpatine_ship.png"
image bg outer_rim = "images/bgs/outer_rim.png"

image anakin normal = "images/chars/anakin_normal.png"
image anakin angry = "images/chars/anakin_angry.png"
image anakin conflicted = "images/chars/anakin_conflicted.png"

image obiwan normal = "images/chars/obiwan_normal.png"
image obiwan defeated = "images/chars/obiwan_defeated.png"

image padme normal = "images/chars/padme_normal.png"
image padme scared = "images/chars/padme_scared.png"

image sidious grinning = "images/chars/sidious_grinning.png"

# Audio definitions
# Placeholder audio files for music and sound effects.
define audio.music_duel = "audio/music/duel_of_fates.ogg"
define audio.music_imperial = "audio/music/imperial_march.ogg"
define audio.music_rogue = "audio/music/rogue_theme.ogg"
define audio.sfx_lightsaber = "audio/sfx/lightsaber_clash.ogg"
define audio.sfx_ship_landing = "audio/sfx/ship_landing.ogg"

# The game starts here.
label start:

    # Scene 1: The Duel's End
    # The story begins on Mustafar, at the climax of the duel.
    scene bg mustafar_bridge
    play music audio.music_duel

    show anakin angry at center
    show obiwan normal at left

    o "It's over, Anakin! I have the high ground!"

    narrator "He was wrong. I saw the leap, the turn, the overconfidence of a master who believed his own teachings."
    narrator "But he taught me to trust my instincts. And my instincts screamed, 'Strike!'"

    # Sound effect for the lightsaber clash
    play sound audio.sfx_lightsaber

    # Character sprites are updated to reflect the action.
    hide obiwan
    show obiwan defeated at left

    o "(gasping) Anakin... please. Let this end."

    show anakin angry at center

    a "No. It *begins* now. I see it all clearly. The Jedi lied. The Sith used me. But I’ll burn them *all* down."

    narrator "My blade was inches from his throat. My former master, defeated. But then..."

    # Padmé arrives, changing the dynamic.
    show padme scared at right

    p "Anakin!"

    # Anakin's expression changes.
    hide anakin angry
    show anakin conflicted at center

    p "Is this what we fought for? Is this who you are now?"

    a "I did it for *you*. For us. To protect what we—"

    p "You *killed* children, Anakin!"

    narrator "Her words were a physical blow. Before I could answer, the air boomed."

    # Scene 2: The Confrontation
    # Palpatine arrives, forcing a choice.
    scene bg palpatine_ship
    play sound audio.sfx_ship_landing

    show sidious grinning at right

    s "My apprentice. You’ve done well. Now finish it. Kill the Jedi — and the woman — and rise as Lord Vader."

    narrator "His words hung in the air, thick with the promise of power and the stench of betrayal. I looked at Obi-Wan, broken. At Padmé, heartbroken. At Sidious, triumphant."
    narrator "My path forked here. His pawn, or my own master?"

    # The pivotal choice for the player.
    menu:
        "Pledge loyalty to Sidious.":
            jump normal_end

        "Betray the Sith.":
            jump plottwist_end

# Ending A: Normal End
# This path follows a darker, more tragic outcome.
label normal_end:

    scene bg palpatine_ship
    play music audio.music_imperial

    show anakin angry at center
    show sidious grinning at right

    a "I will do as you command, my Master."

    s "Good. Good! The galaxy is ours, Lord Vader."

    narrator "I ignited my blade. Obi-Wan closed his eyes. Padmé let out a single, broken sob. I did not hesitate. I was the Emperor's wrath. I was his instrument. And I was lost."

    # Fade to black and end the game.
    scene black
    with fade

    "And so, the shadow of the Empire consumed the galaxy, with Darth Vader at its heart. The hope that was Anakin Skywalker was extinguished forever."

    return

# Ending B: Plot Twist End
# This path follows the "rogue" outcome from the script.
label plottwist_end:

    scene bg palpatine_ship
    play music audio.music_rogue

    show anakin angry at center
    show sidious grinning at right

    a "I’m *no one’s* pawn!"

    narrator "My blade turned not on the fallen Jedi, but on the grinning Sith Lord. His surprise was fleeting, replaced by a snarl of fury."

    play sound audio.sfx_lightsaber

    s "Traitor!"

    narrator "A battle of lightning and steel erupted. But I had Padmé. I had a reason. I fought my way through his guards, grabbed her, and fled to our ship."

    # Final scene in the Outer Rim.
    scene bg outer_rim
    show anakin conflicted at center
    show padme normal at right

    narrator "We escaped into the shadows of the galaxy. The Empire believes Anakin Skywalker is dead. They hunt for a ghost. They are right to be afraid."
    narrator "I am not Jedi. I am not Sith. I am something new. And my war has just begun."

    # Fade to black and end the game.
    scene black
    with fade

    "In the Outer Rim, whispers begin of a warrior in black who fights both Jedi and Empire. The war for the soul of the galaxy is not over. It’s only gone rogue."

    return
