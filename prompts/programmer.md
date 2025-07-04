Prompt Title: Generate a First-Person Visual Novel Script in Ren'Py with a Branching Plot
Core Request:

Write the complete Ren'Py script for a visual novel. he game should be played from the first-person perspective of the main character. The script must include a pivotal choice that leads to two distinct endings. 
There should be 3 scenes: beginning, A, B, A-ending, B-ending 
Required Story Elements given in context 
Required Endings:
Normal End (Label: normal_end): The outcome of choosing the artifact.
Plot Twist End (Label: plottwist_end): The outcome of choosing to save the mentor. 
Technical Requirements:
Use placeholder names for all assets (backgrounds, character sprites, music, and sound effects). 

Optionally have a different background for each scene. Link to background path
Optionally have different character emotional states depending on the context. Link to image path
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

