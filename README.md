mcpi_calculator
============
A python script for use with mcpi to make a digital calculator in the minecraft world.

The calculator consists two main components:

- A keypad which allows the user to input digits and operation types.
    - Consists of 20 specific unique blocks with a sign attached to each one. When you it the sign with the sword it will lookup which key you pressed based on the unique block that is behind the sign.
- A digital display that uses mcpi_writing to display user input and output.
    - The display is 2 lines tall and each line can hold up to 16 characters.

[This project includes a copy of mcpi_writing module](https://github.com/FoamyGuy/mcpi_writing)

Short Video example: http://youtu.be/zY2VLrot1BI

![mcpi_calculator image](https://dl.dropboxusercontent.com/u/5724095/images/Githubpics/mcpi_calculator.png)