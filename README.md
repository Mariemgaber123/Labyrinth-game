Maze Game (Python / Pygame)
Overview

A graphical maze game developed using Python and Pygame.
The player can select the difficulty, navigate through randomly generated mazes, and explore different game options like adjusting volume or muting sounds.

This project demonstrates understanding of:

Object-Oriented Programming (OOP) in Python

Event handling with Pygame

Custom GUI elements (Buttons & InputBoxes)

Algorithmic maze generation and pathfinding

Features

Main menu with PLAY, OPTIONS, and QUIT buttons

Difficulty selection via input box (1–100)

Randomly generated mazes with start (S) and end (E) points

BFS-based path marking to show possible routes

Custom Button and InputBox classes for interactive GUI

Dynamic volume control for background music

Real-time hover effects on buttons

Maze rendering with colored cells

Back navigation from maze or options screen

Technologies & Concepts

Python 3.x

Pygame library

Object-Oriented Programming (Classes, Methods)

BFS algorithm for maze pathfinding

Random maze generation with adjustable difficulty

Custom GUI components and event handling

Sound management with Pygame mixer

Project Structure

main.py → Main game loop, menu, and event handling

button.py → Custom Button class for clickable GUI elements

maze.py → Maze generation and BFS pathfinding logic

assets/ → Images and audio files used in the game

Fonts and sprites used for menus and buttons

How to Run

Clone the repository:

git clone <your-repo-url>


Install Pygame (if not installed):

pip install pygame


Run the main file:

python main.py


Navigate menus using the mouse and keyboard, enter difficulty level, and play the maze game.

Use Cases

Interactive maze game simulation

Demonstration of Python OOP and Pygame GUI

Academic or portfolio project showcasing game programming skills

Learning BFS and maze generation algorithms

Author
Mariem Gaber
