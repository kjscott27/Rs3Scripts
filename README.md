# Description
This is a pack of scripts that can be run in certain places to maximise AFK-ability of certain skills while being away from the desktop entirely.

## Skills
- Agility (Ape Atoll ONLY so far)
- Cooking
- Fletching
- Herbing
- Mining
- Summoning
- Woodcutting

## Helper(s)
- `py main.py -p (or --position)` will help in retrieving the current mouse location

## Setup
You'll most likely need to manually change some of the values in these script(s) in order to get some of them to run. Especially the scripts that require pyautogui to interact with (x, y) co-ordinates on your screen (Agility). You can use the [pyautogui](https://pyautogui.readthedocs.io/en/latest/) documentation or worst case contact me on Discord for assistance (kJs-#2117).

There are easier to use scripts in the pack as well, such as:
- Fletching, where this just requires your mouse to hover over the banker with a preset of either logs or bow/bowstrings (ensure knife is selected from toolbelt for logs -> bows).
- Woodcutting, you can angle the camera downwards and ensure you click at the base of the tree. You will spam cut and create incense sticks with the logs you collect automatically (ensure you have picked incense sticks from the toolbelt and not knife or firepit)

While these scripts are simpler they still may require editing of the hotkeys assigned to pyautogui if you're not going to use the preassigned ones or are unable to.

## Usage
Either listed scenario below works, one is simply shorthand while the other is longhand.
- `py main.py --(fletching/woodcutting/summoning/cooking/mining/herbing/agility/position)`
- `py main.py -(f/w/s/c/m/h/a/p)`
