import mcpi.minecraft as minecraft
import mcpi.vec3 as vec3
import mcpi_writing
import time

"""
mcpi_calculator.py

script for use with mcpi to make a digital calculator in the minecraft world.
"""

# The location where the bottom left of the display will get drawn.
display_pos = vec3.Vec3(-148, 20, -63) # <-- YOU MUST SET ThESE VALUES TO A POSITION FROM YOUR OWN WORLD.

# Max number of blocks (pixels). Divide by 5 to get max characters.
DISPLAY_MAX_WIDTH = 80

# Create an list to hold the display
display = []

# We want two blank lines to start with.
display.append("")
display.append("")

# Dictionary that represents the keypad.
# This maps the id of the block to the character on the keypad that represents it.
input_pad = {14: '1', 16: '2', 22: '3',
              7: '4', 12: '5', 13: '6',
             24: '7', 35: '8', 17: '9',
             45: '0', 19: '+', 48: '-',
             57: '=', 98: 'c', 87: '/',
             121:'*'}


# Set all the pixels in the display to dark. Empty the display list.
def clear_display():
    for x in range(-1, DISPLAY_MAX_WIDTH):
        for y in range(-1, 12):
            mc.setBlock(display_pos.x + x, display_pos.y + y, display_pos.z, 49)
    
    for row in range(0, 2):
        display[row] = ""


# Push text to the right if need be.
def right_align():
    longest = -1
    # find the longest line
    longest = max(len(display[0]), len(display[1]))
    while len(display[0]) < longest:
        display[0] = " " + display[0]
        
    while len(display[1]) < longest:
        display[1] = " " + display[1]
        

# Gets called when you press '=' on the keypard.
# Evaluates the equation.
def solve(equation):
    # Check for the type of operation and solve acordingly.
    if("+" in equation):
        operands = equation.split("+")
        display[1] = str(int(operands[0]) + int(operands[1]))
    elif("-" in equation):    
        operands = equation.split("-")
        display[1] = str(int(operands[0]) - int(operands[1]))
    elif("*" in equation):
        operands = equation.split("*")
        display[1] = str(int(operands[0]) * int(operands[1]))
    elif("/" in equation):
        operands = equation.split("/")
        display[1] = str(float(float(operands[0]) / float(operands[1])))

    right_align()
    draw_display()

# Draw the display based on what is stored in the display list.
def draw_display():
    str = "%s\n%s" % (display[0], display[1])
    mcpi_writing.draw_str(display_pos.x, display_pos.y, display_pos.z, str)


# When the user runs the script do this.
if __name__ == "__main__":
    mc = minecraft.Minecraft.create()
    clear_display()

    # variable to hold the string being typed by the user.
    input_str = ""
    try:
        # Wait until block hit events happen.
        while True:
            #Get the block hit events
            blockHits = mc.events.pollBlockHits()
            # if a block has been hit
            if blockHits:
                # for each block that has been hit
                for blockHit in blockHits:
                    #print (blockHit)

                    # Get the bock that was hit
                    block = mc.getBlock(blockHit.pos.x, blockHit.pos.y, blockHit.pos.z)

                    # Check to see if it was a sign (id=68)
                    if block == 68:
                        # get the block behind the sign
                        block_behind = mc.getBlock(blockHit.pos.x, blockHit.pos.y, blockHit.pos.z - 1)
                        
                        #print(block_behind)

                        # use the input_pad dictionary to determine which character was typed.
                        this_char = input_pad[block_behind]
                        print("pressed: " + this_char)


                        # Take correct action based on which key was pressed.
                        if(this_char == '='):
                            solve(display[0])
                        elif(this_char == 'c'):
                            clear_display()
                        elif(this_char == '+' and len(display[0]) < DISPLAY_MAX_WIDTH / 6):
                            display[0] += this_char
                        elif(this_char == '-' and len(display[0]) < DISPLAY_MAX_WIDTH / 6):
                            display[0] += this_char
                        else:
                            if len(display[0]) < DISPLAY_MAX_WIDTH / 6:
                                display[0] += this_char


                        # Once we are done adding the new digit we need to re-draw the screen.
                        draw_display()
                        
            #sleep for a short time        
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("stopped")
