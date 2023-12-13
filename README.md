# Stick Figure Frame Animation Project

## Author
Swapnil Srivastava

## Description
This project is a Python application using Pygame to animate a stick figure. The animation is based on keyframe animation techniques, where a stick figure can perform various actions like jumping, waving, etc. The project aims to demonstrate the application of keyframes in animations, alongside the use of basic physics principles to create smooth and realistic movements.

## Features
- Stick figure animation using keyframe techniques.
- Ability to switch between different motions (e.g., jumping, waving).
- Smooth transitions and interpolation between keyframes.
- Visualization of axis markers to aid in development and positioning.

## Requirements
- Python 3.10.13
- Pygame 2.5.2

## Installation
To run this project, you need to install Python and Pygame. You can download Python from [python.org](https://www.python.org/downloads/) and install Pygame via pip:


## Usage
The project consists of three main Python files:

- `main.py`: The main script to run the application. It initializes the game, creates the screen, and manages the game loop.
- `Animation.py`: Contains the `Animation` class, responsible for managing the keyframe animations.
- `Keyframes.py`: Contains the `Keyframes` class, which generates keyframes for different motions.

To start the application, run the `main.py` file.
This will show a blank canvas. Press either `j` or `w` lo load up the stick figure onto this screen. 


## Controls
- Press `j` to load and view the jumping motion keyframes.
- Press `w` to load and view the waving motion keyframes.
- Press `a` to start the animation of the loaded keyframes.
- Use the left and right arrow keys to navigate through the keyframes. (Does not work when the animation is running. You can press the 'j' or 'w' key and then use this feature)

## Development
The application includes a helper function to draw x and y axes on the screen, which can be useful during development to understand the positioning of the stick figure.

The color scheme includes a purple torso and a brown head for the stick figure, providing a clear and distinct visual presentation.

## Future Enhancements
- Additional motions for the stick figure can be added by extending the `Keyframes` class.
- Implement more complex easing functions for smoother animations.
- Add user interaction features to control the speed and sequence of animations.