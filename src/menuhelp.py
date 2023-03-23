class menuPoint():
  def __init__ (a, name, y, inv, action):
    a.name = name
    a.y = y
    a.inv = inv
    a.action = action

class menuPage():
  def __init__ (b, index, menupoints, desc):
    b.index = index
    b.menupoints = menupoints
    b.desc = desc
