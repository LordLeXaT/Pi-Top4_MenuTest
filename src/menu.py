from PIL import Image, ImageDraw, ImageFont
from time import sleep
from pitop import Pitop
from subprocess import call
from menuhelp import menuPoint, menuPage

pitop = Pitop()
miniscreen = pitop.miniscreen
image = Image.new(
    miniscreen.mode,
    miniscreen.size,
)
canvas = ImageDraw.Draw(image)
miniscreen.set_max_fps(1)

myExit = False

# define buttons
up = miniscreen.up_button
down = miniscreen.down_button
can = miniscreen.cancel_button
sel = miniscreen.select_button

# Menu variables
cMenu = 0


# setting font and size
myFont = ImageFont.truetype("VeraMono.ttf", size=12)


# define Rows
mRow = [
   (1, 1, 126, 13),
   (1, 14, 126, 27),
   (1, 28, 126, 41),
   (1, 42, 126, 65),
]


# define function to clear OLED
def clear():
    canvas.rectangle(miniscreen.bounding_box, fill=0)


# defining button actions
def bDown():
    global cMenu
    global myMenus
    if cMenu < 3:
       cMenu = cMenu + 1
    else:
       cMenu = 0
    for p in myMenus:
       p.inv = 1
    myMenus[cMenu].inv = 0
    drawMenu()


def bUp():
    global cMenu
    global myMenus
    if cMenu > 0:
       cMenu = cMenu - 1
    else:
       cMenu = 3
    for p in myMenus:
       p.inv = 1
    myMenus[cMenu].inv = 0
    drawMenu()


def bSel():
    global cMenu
    global myExit
    print ("sel pressed")
    myMenus[cMenu].action()

def bCan():
    print ("Cancel Selected")
    drawMenu()

# defining menu functions
def doExit():
  global myExit
  myExit = True

def doReboot():
  call("sudo shutdown -r now", shell=True)

def doShutDown():
  call("sudo shutdown -h now", shell=True)

def doNothing():
  pass

# define buttone actions
up.when_pressed = bUp
down.when_pressed = bDown
can.when_pressed = bCan
sel.when_pressed = bSel

# initialize Menus
myMenus = [
  menuPoint("Exit",1,0,doExit),
  menuPoint("Reboot",14,1,doReboot),
  menuPoint("ShutDown",28,1,doShutDown),
  menuPoint("Nothing",42,1,doNothing),
]

# define function to draw Menu
def drawMenu():
    global myMenus
    rect1 = (0, 0, 127, 63)
    rect2 = (1, 1, 126, 62)
    canvas.rectangle(rect1, fill=1)
    canvas.rectangle(rect2, fill=0)
    canvas.rectangle(mRow[cMenu], fill=1)
    for mpoint in myMenus:
      canvas.text((1, mpoint.y), mpoint.name, font=myFont, fill=mpoint.inv)
    miniscreen.display_image(image)

# initial drawing the Menu
drawMenu()

# keep programm running
while not myExit:
    sleep(0.1)
