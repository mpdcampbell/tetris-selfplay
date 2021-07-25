# tetris-selfplay
A self playing tetris game. <br/>
User can choose between watching the bot play, or playing a game themselves<br/>
Written in python, uses the pygame module, and text is displayed in the font [FairFax](https://github.com/kreativekorp/open-relay/tree/master/Fairfax).

## **Example Gameplay**
<p align="Left">
<img align="center" src="/examples/gameplay.gif" alt="Demo of game modes" title="Game Modes" width="500"><br \>
</p>

## **Controls** 
| Input         | Action               |
| ------------- | -------------------- |
| Left Arrow    | Move Left            |
| Right Arrow   | Move Right           |
| Down Arrow    | Move Down            |
| Up Arrow      | Rotate Clockwise     |
| CTRL          | Rotate Anticlockwise |
| SHIFT         | Hold / Swap Piece    |
| ENTER         | Hard Drop            |
| ESC           | Pause / Unpause      |
| N             | New Game             |

 ## How to Run
 
 ### Requirements To Run
  - Python 3 *(tested with version 3.9.2)*
  - Pygame module *(tested with version 2.0.1)*

  #### Windows
  The latest version of python can be found [here](https://www.python.org/downloads/windows/), last tested version [here](https://www.python.org/downloads/release/python-392/). Choose the *Windows Installer (64 bit)* to ensure the pip tool is also installed. Then, to install the pygame module, open command prompt and enter the following:
  ```
  pip install pygame
  ```
  With above installed, download this repo. Either by git clone or manually downloading the zip and extracting. Then open command prompt, navigate to the tetris-selfplay directory and enter the following:
  ```
  python main.py
  ```
 #### Ubuntu
  Python3 comes installed by default starting from Ubuntu 20.04. 
  To install the pygame module open terminal and enter the following:
  ```
  sudo apt install python3-pygame
  ```
  With above installed, download this repo. Either by git clone or manually downloading the zip and extracting. Then open terminal, navigate to the tetris-selfplay directory and enter the following:
  ```
  python3 main.py
  ```



