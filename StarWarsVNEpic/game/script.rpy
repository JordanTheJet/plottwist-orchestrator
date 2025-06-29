# script.rpy

#-- Character Definitions --
# Defines the characters that will appear in the game.
# The 'me' character is used for the first-person narration from Anakin's perspective.
define me = Character("[config.name!t]")
define obi = Character("Obi-Wan Kenobi")
define padme = Character("Padmé Amidala")
define palpatine = Character("Darth Sidious")

#-- Image Placeholders --
# These lines define placeholder images that will be used for backgrounds and characters.
# In a full game, you would replace these with actual image file paths.
image bg mustafar_bridge = "images/bgs/mustafar_bridge.jpg"
image bg black_screen = "images/bgs/black_screen.png"
image palpatine_ship = "images/bgs/palpatine_ship.jpg"

# Since this is a first-person game, we don't need a sprite for the player (Anakin).
# We also don't see character sprites in this specific scene description, but we define them for good practice.
image obi_wan_defeated = "images/chars/obi_wan_defeated.png"
image padme_worried = "images/chars/padme_worried.png"
image palpatine_smug = "images/chars/palpatine_smug.png"


#-- Audio Placeholders --
# Defines placeholder audio files for music and sound effects.
define audio.battle_music = "audio/music/battle_of_the_heroes.ogg"
define audio.saber_clash = "audio/sfx/saber_clash.ogg"
define audio.saber_ignite = "audio/sfx/saber_ignite.ogg"
define audio.saber_deactivate = "audio/sfx/saber_deactivate.ogg"
define audio.ship_landing = "audio/sfx/ship_landing.ogg"


# The game starts here.
label start:

    #-- Scene Setup --
    # Set the scene with the background and start the music.
    scene bg mustafar_bridge
    play music audio.battle_music

    # Narration from Anakin's perspective
    me "He was the Chosen One. He was meant to destroy the Sith… not join them. But destiny burns hotter than lava."
    me "On the volcanic world of Mustafar, the fate of the galaxy teetered on the edge of my blade."

    # The duel's climax, as described in the test scenario.
    # We use narration and dialogue to build the scene.
    obi "It’s over, Anakin! Don’t try it!"

    me "But this time, I didn't hesitate."
    me "I feinted left, rolled through the ash, and surged under his leap with an upward slash."

    play sound audio.saber_clash

    me "Steel met flesh."

    # Show Obi-Wan defeated.
    show obi_wan_defeated at center
    
    me "His lightsaber flew from his hand. He tumbled to the ground, clutching a burned shoulder, coughing through the sulfur."

    # Dialogue from the script
    me "(low, savage) You taught me to trust my instincts. Bad lesson."
    obi "Anakin… please. Let this end."
    me "(stepping closer, saber lit) No. It *begins* now. I see it all clearly. The Jedi lied. The Sith used me. But I’ll burn them *all* down."

    me "I held the blade inches from his throat—but stopped. A flicker of pain, of memory, stayed my hand."

    # Padmé arrives.
    show padme_worried at right with dissolve

    padme "Anakin!"

    play sound audio.saber_deactivate
    me "My saber deactivated with a hiss. I turned to face her."

    padme "Is this what we fought for? Is this who you are now?"
    me "I did it for *you*. For us. To protect what we—"
    padme "You *killed* children, Anakin!"

    me "Her words struck me harder than any lightsaber."

    # Palpatine arrives.
    scene palpatine_ship
    play sound audio.ship_landing

    me "Suddenly, the air boomed as Palpatine’s ship descended behind us. Red light flooded the ridge."
    me "(to Padmé, eyes wide) He followed you here?"
    padme "(softly) He followed *you*."

    # Hide other characters, show Palpatine
    hide padme_worried
    hide obi_wan_defeated
    show palpatine_smug at center

    palpatine "(grinning) My apprentice. You’ve done well. Now finish it. Kill the Jedi — and the woman — and rise as Lord Vader."

    me "I stared at Obi-Wan's broken form. At Padmé's heartbroken face. At the twisted smile of the Sith Lord."
    me "I ignited my blade."
    play sound audio.saber_ignite

    #-- The Pivotal Choice --
    # This menu presents the player with the two branching paths.
    menu:
        "Finish it. Rise as Lord Vader.":
            jump normal_end

        "I'm no one's pawn!":
            jump plottwist_end


#-- Normal Ending --
# This is the path where Anakin embraces the Dark Side fully.
label normal_end:

    me "He was right. The past had to die. For the Empire. For Padmé."
    me "I turned back to Obi-Wan."

    obi "Anakin..."

    me "Goodbye, Master."
    
    # A black screen implies the deed is done without showing it.
    scene bg black_screen with fade
    play sound audio.saber_clash

    me "I did not hesitate. I struck down my former master. When I turned, Padmé had collapsed."
    me "Sidious placed a hand on my shoulder."

    palpatine "You have done well, Lord Vader. She will be taken care of. Now, let us bring peace to our new Empire."

    me "I felt nothing. Not grief. Not anger. Only the cold, hollow certainty of power."
    me "The galaxy would learn to fear the name Vader."

    # End of the game.
    return


#-- Plot Twist Ending --
# This is the path where Anakin rejects both Jedi and Sith.
label plottwist_end:

    me "A rage, pure and absolute, burned away all my fear. All my doubt."
    me "This time, I turned my blade on Palpatine."

    me "(roaring) I’m *no one’s* pawn!"

    palpatine "So, you have chosen treason."
    
    # A black screen implies a chaotic escape.
    scene bg black_screen with fade

    me "The fight was a blur of red and blue. I grabbed Padmé, pulling her back towards our ship as the platform crumbled around us."
    me "We escaped into the shadows of the galaxy, leaving Mustafar and our old lives to burn."

    me "The galaxy believes both Vader and Anakin are dead. But Palpatine knows better."
    me "In the Outer Rim, whispers begin: of a warrior in black who fights both Jedi and Empire — and whose fury burns hotter than any Sith."
    me "The war for my soul is not over. It has only gone rogue."

    # End of the game.
    return