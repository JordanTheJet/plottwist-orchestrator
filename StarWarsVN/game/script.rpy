# Character definitions
define a = Character("Anakin Skywalker")
define o = Character("Obi-Wan Kenobi")
define p = Character("Padmé Amidala")
define s = Character("Darth Sidious")

# The game starts here.
label start:

    # Scene: Mustafar. Bridge above the lava river.
    scene bg mustafar
    with fade

    "The structure quakes with heat and tremors. Fire dances below. A final blow is imminent."

    o "It's over, Anakin! Don't try it!"

    "But this time, I don't hesitate."

    "I feint left, roll through the ash, and surge under the leap with an upward slash."

    "Steel meets flesh."

    "Obi-Wan's lightsaber flies from his hand. He tumbles to the ground, clutching a burned shoulder, coughing through the sulfur."

    a "You taught me to trust my instincts. Bad lesson."

    o "Anakin... please. Let this end."

    a "No. It *begins* now. I see it all clearly. The Jedi lied. The Sith used me. But I’ll burn them *all* down."

    "I hold the blade inches from Obi-Wan’s throat — but stop."

    "A flicker of pain flashes across my face."

    "Padmé appears at the far end of the platform, coughing from the smoke."

    p "Anakin!"

    "I turn, and my saber deactivates with a hiss. Obi-Wan watches, helpless."

    p "Is this what we fought for? Is this who you are now?"

    a "I did it for *you*. For us. To protect what we—"

    p "You *killed* children, Anakin!"

    "I flinch."

    "Suddenly — the air *booms* as Palpatine’s ship descends behind us. Red light floods the ridge."

    a "He followed you here?"

    p "He followed *you*."

    "A blast wave knocks her off her feet. I turn, eyes blazing, as Sidious descends the ramp."

    s "My apprentice. You’ve done well. Now finish it. Kill the Jedi — and the woman — and rise as Lord Vader."

    "I stare at Obi-Wan. Then at Padmé. Then at Sidious."

    "I ignite my blade."

    menu:
        "Turn the blade on Palpatine.":
            jump plottwist_end
        "Finish Obi-Wan.":
            jump normal_end

label normal_end:
    a "I am your pawn no longer."
    "I turn and strike down Obi-Wan."
    "Sidious laughs."
    s "Good. Good! Lord Vader, you have done well."
    "I have embraced my destiny. The galaxy will be mine."
    return

label plottwist_end:
    a "I’m *no one’s* pawn!"
    "I turn my blade on Palpatine."
    "He is surprised, but quickly recovers, his own crimson blade appearing in his hand."
    s "So, you have chosen death."
    "We clash in a flurry of blows. But I am fueled by a rage he cannot comprehend. I drive him back, and with a final, desperate push, I end him."
    "I stand victorious, but alone. Padmé is gone. Obi-Wan is gone. I am all that is left."
    "The galaxy believes both Vader and Anakin are dead. But I know better."
    "In the Outer Rim, whispers begin: of a warrior in black who fights both Jedi and Empire — and whose fury burns hotter than any Sith."
    "The war for the soul of the galaxy is not over."
    "It’s only gone rogue."
    return
