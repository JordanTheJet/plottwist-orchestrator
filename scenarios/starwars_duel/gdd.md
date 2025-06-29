# Game Design Document: Star Wars - The Mustafar Duel

## 1. Overview

This document outlines the design for *Star Wars: The Mustafar Duel*, a cinematic visual novel with action elements. The game will recreate the iconic duel between Anakin Skywalker and Obi-Wan Kenobi on Mustafar, with a unique art style inspired by Studio Ghibli to emphasize the emotional weight of the story.

- **Game Title:** Star Wars: The Mustafar Duel
- **Genre:** Action / Cinematic Visual Novel
- **Target Platform:** PC (using the Ren'Py engine)
- **Art Style:** Studio Ghibli inspired

## 2. Gameplay Mechanics

The game will be a linear narrative experience, but player engagement will be maintained through interactive elements.

### 2.1. Narrative Choices

Throughout the dialogue, the player will be presented with choices from the perspective of either Anakin or Obi-Wan. These choices will not alter the final outcome of the story but will provide different lines of dialogue and internal monologues, allowing the player to explore the characters' emotional states.

**Example:**

When Obi-Wan says, "I have failed you, Anakin," the player might be given a choice of internal thoughts:
1.  (Regret) "I should have seen the darkness in him sooner."
2.  (Resolve) "I must end this, no matter the cost."
3.  (Hope) "Perhaps there is still a glimmer of the man I knew."

### 2.2. Quick-Time Events (QTEs)

The lightsaber combat will be handled through QTEs. During action sequences, button prompts will appear on screen.

- **Success:** Successfully pressing the correct button will result in a fluid animation of a parry, dodge, or attack.
- **Failure:** Missing a prompt will result in a stumble, a loss of ground, or a non-fatal hit, with a corresponding animation that shows the character struggling. The story will continue, but the visual representation of the fight will change.

## 3. Art and Sound Direction

### 3.1. Art Style

The art will be heavily inspired by Studio Ghibli.

- **Characters:** Expressive, hand-drawn characters. The designs should be recognizable but softened, with a focus on conveying emotion through facial expressions and body language.
- **Environments:** Lush, painterly backgrounds. The volcanic landscape of Mustafar should be a key visual element, with flowing lava, ash-filled skies, and towering industrial structures.
- **UI:** The user interface (dialogue boxes, menus, etc.) should be clean and unobtrusive, with a design that complements the Ghibli aesthetic.

### 3.2. Sound Design

- **Music:** The score will be a mix of iconic Star Wars themes and new, more somber pieces that reflect the tragic nature of the story.
- **Sound Effects:** Lightsaber clashes, the roar of the lava, and the hum of machinery will be crucial for immersion.
- **Voice Acting:** The dialogue from the script will be fully voice-acted to enhance the emotional impact.

## 4. Scene Breakdown

The game will be divided into four main scenes, following the script.

### Scene 1: The Landing Platform
- **Objective:** Introduce the characters and the central conflict.
- **Gameplay:** Primarily dialogue-driven, with a few narrative choices. The scene ends with the ignition of the lightsabers, leading into the first QTE.

### Scene 2: The Duel in the Facility
- **Objective:** Showcase the intensity of the duel.
- **Gameplay:** A mix of dialogue and multiple QTE sequences. The environment will be a key factor, with QTEs involving interaction with the machinery.

### Scene 3: The Lava River
- **Objective:** Escalate the danger and the emotional stakes.
- **Gameplay:** A continuous, high-stakes QTE sequence as the characters battle on the mining droid. The background will be a dynamic, flowing river of lava.

### Scene 4: The Aftermath
- **Objective:** Conclude the story with the tragic separation of the two characters.
- **Gameplay:** No QTEs. This scene is purely narrative, focusing on the final lines of dialogue and the emotional weight of the moment.

## 5. Asset List

The following assets will be required:

- **Character Sprites:**
    - Anakin Skywalker (Sith attire)
    - Obi-Wan Kenobi (Jedi robes)
- **Backgrounds:**
    - Landing Platform (Exterior)
    - Mining Facility (Interior)
    - Lava River
    - Lava River Shore
- **CGs (Computer Graphics):**
    - Key moments in the duel (e.g., locked blades, Anakin's leap).
    - The final shot of Anakin on the shore.