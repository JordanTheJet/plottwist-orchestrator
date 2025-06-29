Prompt Title: Generate a First-Person Visual Novel Script in Ren'Py with a Branching Plot
Core Request:

Write the complete Ren'Py script for a visual novel. The game should be played from the first-person perspective of the main character. The script must include a pivotal choice that leads to two distinct endings. 
There should be 3 scenes: beginning, A, B, A-ending, B-ending 
Required Story Elements given in context 
Required Endings:
Normal End (Label: normal_end): The outcome of choosing the artifact.
Plot Twist End (Label: plottwist_end): The outcome of choosing to save the mentor. 

Technical Requirements:
IMPORTANT: Use the generated images provided in the context. Do NOT use placeholder names.
- For backgrounds: Use the images in the "bgs/" folder
- For characters: Use the images in the "chars/" folder with appropriate expressions
- Reference images using their exact filenames (e.g., "bgs/main_scene.png", "chars/protagonist_happy.png")

Image Usage Guidelines:
- Use "bgs/main_scene.png" for the main story scenes
- Use character images with appropriate expressions:
  * "chars/protagonist_neutral.png" for neutral dialogue
  * "chars/protagonist_happy.png" for happy/positive moments
  * "chars/protagonist_sad.png" for sad/negative moments
  * "chars/antagonist.png" for antagonist appearances
  * "chars/supporting_character.png" for supporting characters

Ren'Py Image Commands:
- Use `scene "images/bgs/filename.png"` for backgrounds
- Use `show character_name "images/chars/filename.png"` for character sprites
- Use `hide character_name` to hide characters when needed

Create relevant sound effects for key points
Create background music that matches the scene
The code must be fully functional and copy-paste ready into a script.rpy file within a new Ren'Py project. Include comments within the code to explain key functions like character definitions, scene changes, menus, and jumps.
Follow renpy best practices.
Don't refer to config files

Make a copy of exampleVN with all contents.


 Follow the file directory structure below. file and folder names surrounded with asterisks *file* can have the name changed to match the story 

*newVN*/  <-- This is your <project name> root folder (the "base").
|
+-- game/           # This is the most important folder. All your game code and assets live here.
|   |
|   +-- audio/      # Folder for all sound files.
|   |   |
|   |   +-- music/  # Subfolder for background music.
|   |   |
|   |   +-- sfx/    # Subfolder for sound effects.
|   |
|   +-- gui/        # Contains files to customize the game's User Interface.
|   |   |           # (e.g., button images, textbox skins, menu backgrounds)
|   |   +-- (Ren'Py generates default GUI files and folders here)
|   |
|   +-- images/     # Folder for all visual assets.
|   |   |
|   |   +-- bgs/    # Subfolder for backgrounds.
|   |   |
|   |   +-- chars/  # Subfolder for character sprites.
|   |
|   +-- script.rpy  # The main script file where you paste the game code.
|   +-- options.rpy # For game settings like screen size, default text speed, etc.
|   +-- gui.rpy     # Script file for defining GUI behavior and appearance.
|
+-- lib/            # Contains system libraries for the Ren'Py engine. (Do not modify)
|
+-- renpy/          # The Ren'Py engine itself. (Do not modify)
|
+-- *newVN*.exe  # The executable file to launch your game (name varies by OS).

