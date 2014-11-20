import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

NORTH = 2
SOUTH = 0

def fill(start_x, start_y, start_z, block=49, size=5, facing=NORTH):
    for x in range(0, size):
        for y in range(0, 5):
            mc.setBlock(start_x + (facing-1) * x, start_y + y, start_z, block)


def a(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        mc.setBlock(x, y + height, z, fg_block)
        mc.setBlock(x + (facing-1) * 4, y + height, z, fg_block)

    # horizontal lines
    for width in range(0, 5):
        mc.setBlock(x + (facing-1) * width, y + 4, z, fg_block)
        mc.setBlock(x + (facing-1) * width, y + 2, z, fg_block)


def b(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        mc.setBlock(x, y + height, z, fg_block)


    # horizontal lines
    for width in range(0, 4):
        mc.setBlock(x + (facing-1) * width, y + 4, z, fg_block)
        mc.setBlock(x + (facing-1) * width, y + 2, z, fg_block)
        mc.setBlock(x + (facing-1) * width, y + 0, z, fg_block)

    # right side dots
    mc.setBlock(x + (facing-1) * 4, y + 1, z, fg_block)
    mc.setBlock(x + (facing-1) * 4, y + 3, z, fg_block)


def c(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        mc.setBlock(x, y + height, z, fg_block)


    # horizontal lines
    for width in range(0, 5):
        mc.setBlock(x + (facing-1) * width, y + 4, z, fg_block)
        mc.setBlock(x + (facing-1) * width, y + 0, z, fg_block)


def d(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        mc.setBlock(x, y + height, z, fg_block)
        if (height < 4) and (height > 0):
            mc.setBlock(x + (facing-1) * 4, y + height, z, fg_block)

    # horizontal lines
    for width in range(0, 4):
        mc.setBlock(x + (facing-1) * width, y + 4, z, fg_block)
        mc.setBlock(x + (facing-1) * width, y + 0, z, fg_block)


def e(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        mc.setBlock(x, y + height, z, fg_block)


    # horizontal lines
    for width in range(0, 5):
        mc.setBlock(x + (facing-1) * width, y + 4, z, fg_block)
        mc.setBlock(x + (facing-1) * width, y + 2, z, fg_block)
        mc.setBlock(x + (facing-1) * width, y + 0, z, fg_block)


def f(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        mc.setBlock(x, y + height, z, fg_block)


    # horizontal lines
    for width in range(0, 5):
        mc.setBlock(x + (facing-1) * width, y + 4, z, fg_block)
        if (width < 4):
            mc.setBlock(x + (facing-1) * width, y + 2, z, fg_block)


def g(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        mc.setBlock(x, y + height, z, fg_block)
        if height < 3:
            mc.setBlock(x + (facing-1) * 4, y + height, z, fg_block)



    # horizontal lines
    for width in range(0, 5):
        mc.setBlock(x + (facing-1) * width, y + 0, z, fg_block)
        if (width > 1):
            mc.setBlock(x + (facing-1) * width, y + 2, z, fg_block)
        if (width < 4):
            mc.setBlock(x + (facing-1) * width, y + 4, z, fg_block)


def h(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        mc.setBlock(x, y + height, z, fg_block)
        mc.setBlock(x + (facing-1) * 4, y + height, z, fg_block)

    # horizontal lines
    for width in range(0, 5):
        mc.setBlock(x + (facing-1) * width, y + 2, z, fg_block)


def i(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        mc.setBlock(x + (facing-1) * 2, y + height, z, fg_block)


    # horizontal lines
    for width in range(0, 5):
        mc.setBlock(x + (facing-1) * width, y + 4, z, fg_block)
        mc.setBlock(x + (facing-1) * width, y + 0, z, fg_block)


def j(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        mc.setBlock(x + (facing-1) * 3, y + height, z, fg_block)
        if height < 2:
            mc.setBlock(x + (facing-1) * 0, y + height, z, fg_block)


    # horizontal lines
    for width in range(0, 5):
        if width < 4:
            mc.setBlock(x + (facing-1) * width, y + 0, z, fg_block)
        if width > 1:
            mc.setBlock(x + (facing-1) * width, y + 4, z, fg_block)


def k(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        mc.setBlock(x, y + height, z, fg_block)
        if height == 2:
            mc.setBlock(x + (facing-1) * 1, y + height, z, fg_block)


    # Diagnal lines
    mc.setBlock(x + (facing-1) * 2, y + 1, z, fg_block)
    mc.setBlock(x + (facing-1) * 2, y + 3, z, fg_block)
    mc.setBlock(x + (facing-1) * 3, y + 0, z, fg_block)
    mc.setBlock(x + (facing-1) * 3, y + 4, z, fg_block)


def l(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        mc.setBlock(x + (facing-1) * 0, y + height, z, fg_block)


    # horizontal lines
    for width in range(0, 5):
        mc.setBlock(x + (facing-1) * width, y + 0, z, fg_block)


def m(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 4):
        mc.setBlock(x + (facing-1) * 0, y + height, z, fg_block)
        mc.setBlock(x + (facing-1) * 4, y + height, z, fg_block)
        if (height > 1) and (height < 5):
            mc.setBlock(x + (facing-1) * 2, y + height, z, fg_block)
    # top dots
    mc.setBlock(x + (facing-1) * 1, y + 4, z, fg_block)
    mc.setBlock(x + (facing-1) * 3, y + 4, z, fg_block)


def n(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        mc.setBlock(x + (facing-1) * 0, y + height, z, fg_block)
        mc.setBlock(x + (facing-1) * 4, y + height, z, fg_block)
        if (height > 2):
            mc.setBlock(x + (facing-1) * 1, y + height, z, fg_block)

        if (height > 1) and (height < 4):
            mc.setBlock(x + (facing-1) * 2, y + height, z, fg_block)

        if (height > 0) and (height < 3):
            mc.setBlock(x + (facing-1) * 3, y + height, z, fg_block)


def o(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        if (height > 0) and (height < 4):
            mc.setBlock(x + (facing-1) * 0, y + height, z, fg_block)
            mc.setBlock(x + (facing-1) * 4, y + height, z, fg_block)

    # horizontal lines
    for width in range(0, 5):
        if (width > 0) and (width < 4):
            mc.setBlock(x + (facing-1) * width, y + 0, z, fg_block)
            mc.setBlock(x + (facing-1) * width, y + 4, z, fg_block)


def p(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        mc.setBlock(x, y + height, z, fg_block)
        if (height == 3):
            mc.setBlock(x + (facing-1) * 4, y + height, z, fg_block)


    # horizontal lines
    for width in range(0, 4):
        mc.setBlock(x + (facing-1) * width, y + 4, z, fg_block)
        mc.setBlock(x + (facing-1) * width, y + 2, z, fg_block)


def q(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        if (height > 0) and (height < 4):
            mc.setBlock(x + (facing-1) * 0, y + height, z, fg_block)
            if (height > 1):
                mc.setBlock(x + (facing-1) * 4, y + height, z, fg_block)

    # horizontal lines
    for width in range(0, 5):
        if (width > 0) and (width < 4):
            mc.setBlock(x + (facing-1) * width, y + 4, z, fg_block)
            if (width < 3):
                mc.setBlock(x + (facing-1) * width, y + 0, z, fg_block)
    # diagnal line
    mc.setBlock(x + (facing-1) * 4, y, z, fg_block)
    mc.setBlock(x + (facing-1) * 3, y + 1, z, fg_block)


def r(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        mc.setBlock(x, y + height, z, fg_block)
        if height > 2:
            mc.setBlock(x + (facing-1) * 4, y + height, z, fg_block)


    # horizontal lines
    for width in range(0, 5):
        mc.setBlock(x + (facing-1) * width, y + 4, z, fg_block)
        mc.setBlock(x + (facing-1) * width, y + 2, z, fg_block)

    mc.setBlock(x + (facing-1) * 4, y + 0, z, fg_block)
    mc.setBlock(x + (facing-1) * 3, y + 1, z, fg_block)


def s(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        if (height < 3):
            mc.setBlock(x + (facing-1) * 4, y + height, z, fg_block)
        if (height > 2):
            mc.setBlock(x + (facing-1) * 0, y + height, z, fg_block)

    # horizontal lines
    for width in range(0, 5):
        mc.setBlock(x + (facing-1) * width, y + 4, z, fg_block)
        mc.setBlock(x + (facing-1) * width, y + 2, z, fg_block)
        mc.setBlock(x + (facing-1) * width, y + 0, z, fg_block)


def t(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        mc.setBlock(x + (facing-1) * 2, y + height, z, fg_block)



    # horizontal lines
    for width in range(0, 5):
        mc.setBlock(x + (facing-1) * width, y + 4, z, fg_block)


def u(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(1, 5):
        mc.setBlock(x + (facing-1) * 0, y + height, z, fg_block)
        mc.setBlock(x + (facing-1) * 4, y + height, z, fg_block)



    # horizontal lines
    for width in range(1, 4):
        mc.setBlock(x + (facing-1) * width, y + 0, z, fg_block)


def v(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        if (height > 2):
            mc.setBlock(x + (facing-1) * 0, y + height, z, fg_block)
            mc.setBlock(x + (facing-1) * 4, y + height, z, fg_block)
        if (height < 3) and (height > 0):
            mc.setBlock(x + (facing-1) * 1, y + height, z, fg_block)
            mc.setBlock(x + (facing-1) * 3, y + height, z, fg_block)

    # bottom dot
    mc.setBlock(x + (facing-1) * 2, y + 0, z, fg_block)


def w(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(1, 5):
        mc.setBlock(x + (facing-1) * 0, y + height, z, fg_block)
        mc.setBlock(x + (facing-1) * 4, y + height, z, fg_block)
        if (height > 0) and (height < 3):
            mc.setBlock(x + (facing-1) * 2, y + height, z, fg_block)
    # bottom dots
    mc.setBlock(x + (facing-1) * 1, y + 0, z, fg_block)
    mc.setBlock(x + (facing-1) * 3, y + 0, z, fg_block)


def eks(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        if (height == 0) or (height == 4):
            mc.setBlock(x + (facing-1) * 0, y + height, z, fg_block)
            mc.setBlock(x + (facing-1) * 4, y + height, z, fg_block)
        if (height == 1) or (height == 3):
            mc.setBlock(x + (facing-1) * 1, y + height, z, fg_block)
            mc.setBlock(x + (facing-1) * 3, y + height, z, fg_block)
    mc.setBlock(x + (facing-1) * 2, y + 2, z, fg_block)


def why(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        if height == 4:
            mc.setBlock(x + (facing-1) * 0, y + height, z, fg_block)
            mc.setBlock(x + (facing-1) * 4, y + height, z, fg_block)
        if height == 3:
            mc.setBlock(x + (facing-1) * 1, y + height, z, fg_block)
            mc.setBlock(x + (facing-1) * 3, y + height, z, fg_block)
        if (height < 3):
            mc.setBlock(x + (facing-1) * 2, y + height, z, fg_block)


def zee(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)

    # horizontal lines
    for width in range(0, 5):
        if (width < 4):
            mc.setBlock(x + (facing-1) * width, y + 0, z, fg_block)
        if (width > 0):
            mc.setBlock(x + (facing-1) * width, y + 4, z, fg_block)

    # center diagonal
    mc.setBlock(x + (facing-1) * 1, y + 3, z, fg_block)
    mc.setBlock(x + (facing-1) * 2, y + 2, z, fg_block)
    mc.setBlock(x + (facing-1) * 3, y + 1, z, fg_block)


def one(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        mc.setBlock(x + (facing-1) * 2, y + height, z, fg_block)

    # horizontal lines
    for width in range(0, 5):
        mc.setBlock(x + (facing-1) * width, y + 0, z, fg_block)
        if (width > 0) and (width < 3):
            mc.setBlock(x + (facing-1) * width, y + 4, z, fg_block)


def two(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    mc.setBlock(x, y + 1, z, fg_block)
    mc.setBlock(x + (facing-1) * 4, y + 3, z, fg_block)


    # horizontal lines
    for width in range(0, 5):
        mc.setBlock(x + (facing-1) * width, y + 0, z, fg_block)
        mc.setBlock(x + (facing-1) * width, y + 2, z, fg_block)
        mc.setBlock(x + (facing-1) * width, y + 4, z, fg_block)


def three(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(1, 4):
        mc.setBlock(x + (facing-1) * 4, y + height, z, fg_block)

    # horizontal lines
    for width in range(0, 5):
        if (width < 4):
            mc.setBlock(x + (facing-1) * width, y + 0, z, fg_block)
            mc.setBlock(x + (facing-1) * width, y + 4, z, fg_block)
        if (width > 0):
            mc.setBlock(x + (facing-1) * width, y + 2, z, fg_block)


def four(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        mc.setBlock(x + (facing-1) * 4, y + height, z, fg_block)
        if (height > 1):
            mc.setBlock(x + (facing-1) * 0, y + height, z, fg_block)

    # horizontal lines
    for width in range(0, 5):
        mc.setBlock(x + (facing-1) * width, y + 2, z, fg_block)


def five(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    s(x, y, z, fg_block, bg_block)


def six(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        mc.setBlock(x + (facing-1) * 0, y + height, z, fg_block)
        if (height < 3):
            mc.setBlock(x + (facing-1) * 4, y + height, z, fg_block)

    # horizontal lines
    for width in range(0, 5):
        mc.setBlock(x + (facing-1) * width, y + 0, z, fg_block)
        mc.setBlock(x + (facing-1) * width, y + 2, z, fg_block)
        mc.setBlock(x + (facing-1) * width, y + 4, z, fg_block)


def seven(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 2):
        mc.setBlock(x + (facing-1) * 2, y + height, z, fg_block)
    mc.setBlock(x + (facing-1) * 3, y + 2, z, fg_block)
    mc.setBlock(x + (facing-1) * 4, y + 3, z, fg_block)


    # horizontal lines
    for width in range(0, 5):
        mc.setBlock(x + (facing-1) * width, y + 4, z, fg_block)


def eight(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical dots
    mc.setBlock(x + (facing-1) * 4, y + 1, z, fg_block)
    mc.setBlock(x + (facing-1) * 4, y + 3, z, fg_block)
    mc.setBlock(x + (facing-1) * 0, y + 1, z, fg_block)
    mc.setBlock(x + (facing-1) * 0, y + 3, z, fg_block)

    # horizontal lines
    for width in range(1, 4):
        mc.setBlock(x + (facing-1) * width, y + 0, z, fg_block)
        mc.setBlock(x + (facing-1) * width, y + 2, z, fg_block)
        mc.setBlock(x + (facing-1) * width, y + 4, z, fg_block)


def nine(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)

    # horizontal lines
    for height in range(1, 4):
        mc.setBlock(x + (facing-1) * 4, y + height, z, fg_block)

    # vertical dots
    mc.setBlock(x + (facing-1) * 0, y + 0, z, fg_block)
    mc.setBlock(x + (facing-1) * 0, y + 3, z, fg_block)

    # horizontal lines
    for width in range(1, 4):
        mc.setBlock(x + (facing-1) * width, y + 0, z, fg_block)
        mc.setBlock(x + (facing-1) * width, y + 2, z, fg_block)
        mc.setBlock(x + (facing-1) * width, y + 4, z, fg_block)


def zero(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    o(x, y, z, fg_block, bg_block)


def period(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, size=1)

    mc.setBlock(x + (facing-1) * 0, y + 0, z, fg_block)


def comma(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, size=2)
    mc.setBlock(x + (facing-1) * 0, y + 0, z, fg_block)
    mc.setBlock(x + (facing-1) * 1, y + 1, z, fg_block)


def colon(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, size=1)
    mc.setBlock(x + (facing-1) * 0, y + 1, z, fg_block)
    mc.setBlock(x + (facing-1) * 0, y + 3, z, fg_block)


def semicolon(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, size=2)
    mc.setBlock(x + (facing-1) * 0, y + 0, z, fg_block)
    mc.setBlock(x + (facing-1) * 1, y + 1, z, fg_block)
    mc.setBlock(x + (facing-1) * 1, y + 3, z, fg_block)


def plus(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    for height in range(0, 5):
        mc.setBlock(x + (facing-1) * 2, y + height, z, fg_block)

    # horizontal lines
    for width in range(0, 5):
        mc.setBlock(x + (facing-1) * width, y + 2, z, fg_block)


def minus(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # horizontal lines
    for width in range(0, 5):
        mc.setBlock(x + (facing-1) * width, y + 2, z, fg_block)


def equals(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # horizontal lines
    for width in range(0, 5):
        mc.setBlock(x + (facing-1) * width, y + 1, z, fg_block)
        mc.setBlock(x + (facing-1) * width, y + 3, z, fg_block)


def times(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    eks(x, y, z, fg_block=57, bg_block=49)


def divide(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # vertical lines
    mc.setBlock(x + (facing-1) * 0, y + 0, z, fg_block)
    mc.setBlock(x + (facing-1) * 1, y + 1, z, fg_block)
    mc.setBlock(x + (facing-1) * 2, y + 2, z, fg_block)
    mc.setBlock(x + (facing-1) * 3, y + 3, z, fg_block)
    mc.setBlock(x + (facing-1) * 4, y + 4, z, fg_block)


def underscore(x, y, z, fg_block=57, bg_block=49, facing=NORTH):
    fill(x, y, z, bg_block, facing=facing)
    # horizontal lines
    for width in range(0, 5):
        mc.setBlock(x + (facing-1) * width, y + 0, z, fg_block)


def letter_space(x, y, z, block=49):
    # vertical lines
    for height in range(0, 5):
        mc.setBlock(x, y + height, z, block)


def draw_str(x, y, z, str, fg_block=57, bg_block=49, border=False, facing=NORTH):
    lines = str.split("\n")
    cur_y = ((len(lines) - 1) * 6) + y
    last_line = len(lines) - 1
    for j, line in enumerate(lines):
        last = len(line) - 1
        cur_x = x
        line_width = 0

        for i, letter in enumerate(line):
            if letter == ' ':
                alphabet[letter](cur_x, cur_y, z, bg_block, facing=facing)
                letter_width = 5
            elif (letter == ','):
                alphabet[letter](cur_x, cur_y, z, fg_block, bg_block, facing=facing)
                letter_width = 2
            elif (letter == ':') or (letter == '.'):
                alphabet[letter](cur_x, cur_y, z, fg_block, bg_block, facing=facing)
                letter_width = 1
            else:
                alphabet[letter](cur_x, cur_y, z, fg_block, bg_block, facing=facing)
                letter_width = 5

            if i != last:
                letter_space(cur_x + (facing-1) * letter_width, cur_y, z, bg_block)
            cur_x += (facing-1) * (letter_width + 1)
            line_width += letter_width + 1

        if border:
            # border on top
            for width in range(0, line_width - 1):
                mc.setBlock(x + (facing-1) * width, cur_y + 5, z, bg_block)

            # left border
            for height in range(-1, 6):
                mc.setBlock(x - (facing-1) * 1, cur_y + height, z, bg_block)

            # right border
            for height in range(-1, 6):
                mc.setBlock(x + (facing-1) * (line_width - 1), cur_y + height, z, bg_block)

        # fill empty line
        for width in range(0, line_width - 1):
            mc.setBlock(x + (facing-1) * width, cur_y - 1, z, bg_block)
        cur_y -= 6


alphabet = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e,
            'f': f, 'g': g, 'h': h, 'i': i, 'j': j,
            'k': k, 'l': l, 'm': m, 'n': n, 'o': o,
            'p': p, 'q': q, 'r': r, 's': s, 't': t,
            'u': u, 'v': v, 'w': w, 'x': eks,
            'y': why, 'z': zee, ' ': fill,
            '1': one, '2': two, '3': three, '4': four,
            '5': five, '6': six, '7': seven, '8': eight,
            '9': nine, '0': zero,
            '.': period, ',': comma, ':': colon,
            '+': plus, '-': minus, '=': equals,
            '*': times, '/': divide, '_': underscore}

if __name__ == "__main__":
    pos = mc.player.getPos()
    draw_str(pos.x, pos.y + 1, pos.z - 1, "hello\nworld", fg_block=74, bg_block=49, border=True, facing=SOUTH)
