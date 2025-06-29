# Ren'Py Script for Star Wars: The Mustafar Duel

# Define Characters
define a = Character("Anakin Skywalker", color="#ff4500")
define o = Character("Obi-Wan Kenobi", color="#00bfff")

# Declare Images
image bg landing_platform = "images/bg_landing_platform.jpg"
image bg mining_facility = "images/bg_mining_facility.jpg"
image bg lava_river = "images/bg_lava_river.jpg"
image bg lava_shore = "images/bg_lava_shore.jpg"

image anakin normal = "images/anakin_normal.png"
image obiwan normal = "images/obiwan_normal.png"

image cg locked_blades = "images/cg_locked_blades.jpg"
image cg anakin_leap = "images/cg_anakin_leap.jpg"
image cg aftermath = "images/cg_aftermath.jpg"

# The game starts here.
label start:
    # Scene 1: The Landing Platform
    scene bg landing_platform
    show obiwan normal at left
    show anakin normal at right

    o "Anakin!"

    a "I see through the lies of the Jedi. I do not fear the dark side as you do."

    o "Anakin, my allegiance is to the Republic, to democracy!"

    menu:
        "If you're not with me, then you're my enemy.":
            a "If you're not with me, then you're my enemy."
        "(Internally) He's too far gone.":
            a "If you're not with me, then you're my enemy."
            o "(I can't reach him.)"

    o "Only a Sith deals in absolutes. I will do what I must."

    # Quick-Time Event
    label qte_1:
        "QTE: Block Anakin's attack!"
        $ qte_result = renpy.random.choice(['success', 'fail'])
        if qte_result == 'success':
            "You successfully block Anakin's furious assault."
        else:
            "You stumble, but quickly regain your footing."

    # Scene 2: The Duel in the Facility
    scene bg mining_facility
    show obiwan normal at left
    show anakin normal at right

    o "I have failed you, Anakin. I have failed you."

    a "I should have known the Jedi were plotting to take over!"

    o "Anakin, Chancellor Palpatine is evil!"

    a "From my point of view, the Jedi are evil!"

    scene cg locked_blades

    o "Well, then you are lost!"

    # Scene 3: The Lava River
    scene bg lava_river
    show obiwan normal at left
    show anakin normal at right

    a "This is the end for you, Master."

    o "It's over, Anakin! I have the high ground!"

    a "You underestimate my power!"

    o "Don't try it."

    # Final QTE
    label qte_2:
        "QTE: Counter Anakin's leap!"
        $ qte_result = renpy.random.choice(['success']) # This one is scripted to succeed
        if qte_result == 'success':
            scene cg anakin_leap
            "You strike true, and Anakin falls."
        else:
            # This path won't be taken in this version
            pass

    # Scene 4: The Aftermath
    scene bg lava_shore
    show cg aftermath

    o "You were the chosen one! It was said that you would destroy the Sith, not join them! Bring balance to the force, not leave it in darkness!"

    "You take Anakin's lightsaber and walk away, leaving your former apprentice to his fate."

    return