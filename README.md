# tetris-selfplay
A self playing tetris game. <br/>
User can choose between watching the bot play, or playing a game themselves<br/>
Written in python, uses the pygame module, and text is displayed in the font [FairFax](https://github.com/kreativekorp/open-relay/tree/master/Fairfax).

## **Example Gameplay**
<p align="Left">
<img align="center" src="/examples/gameplay.gif" alt="Demo of game modes" title="Game Modes" width="380"><br \>
</p>

## **Controls and Scoring** 
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

| Lines Cleared | Score |
| ------------- | ----- |
| 1             | 1     |
| 2             | 3     |
| 3             | 5     |
| 4             | 8     |

 ## How to Run
 
 ### Requirements To Run
  - Python 3 *(tested with version 3.9.2)*
  - Pygame module *(tested with version 2.0.1)*

  #### Windows
  The latest version of python can be found [here](https://www.python.org/downloads/windows/). Choose the *Windows Installer (64 bit)*  and make sure to tick *Add Python to path*. Then to install the pygame module, open command prompt and enter the following:
  ```
  pip install pygame
  ```
  With above installed, download this repo. Either by git clone or manually downloading the zip and extracting. Then open command prompt, navigate to the tetris-selfplay directory and enter the following:
  ```
  python main.py
  ```
  #### Ubuntu 20.04
  Python 3.8.2 comes installed by default starting from Ubuntu 20.04.<br/> 
  To install the pygame module open terminal and enter the following in turn:
  ```
  sudo apt update
  sudo apt install python3-pygame
  ```
  With above installed, download this repo. Either by git clone or manually downloading the zip and extracting.<br/>
  Then open terminal, navigate to the tetris-selfplay directory and enter the following:
  ```
  python3 main.py
  ```
  #### Ubuntu 16.04 or 18.04
  The latest version of python available in the official Ubuntu repositories is older than the 3.7.7 version required for the pygame module.<br/>
  But you can install the latest python versions by adding the [deadsnakes PPA](https://launchpad.net/~deadsnakes).<br/>
  Open terminal and enter the following in turn:
  ```
  sudo apt install software-properties-common
  sudo add-apt-repository ppa:deadsnakes/ppa
  sudo apt update 
  sudo apt install python3.9
  ```
  Now python 3.9 is installed, you can install pygame using pip.
  ```
  sudo apt install python3-pip
  sudo pip install pygame
  ```
  With above installed, download this repo. Either by git clone or manually downloading the zip and extracting.<br/>
  Then open terminal, navigate to the tetris-selfplay directory and enter the following:
  ```
  python3.9 main.py
  ```
