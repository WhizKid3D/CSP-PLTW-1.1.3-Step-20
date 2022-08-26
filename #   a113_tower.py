#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the 
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150
color_1 = ("gray")
color_2 = ("blue")
color_3 = ("orange")
Tower_Number = 1
# height of tower and a counter for each floor
num_floors = 63
current_floor=0
# iterate
for floor in range(num_floors):
  current_floor+=1
  if Tower_Number == 1:
    color_1 = ("gray")
    color_2 = ("blue")
    color_3 = ("orange")
  elif Tower_Number == 2:
    color_1 = ("pink")
    color_2 = ("yellow")
    color_3 = ("green")
  elif Tower_Number == 3:
    color_1 = ("purple")
    color_2 = ("red")
    color_3 = ("black")
  # set placement and color of turtle
  painter.penup()
  painter.color(color_1)
  rem = floor % 3
  if (rem == 0):
    painter.color(color_2)
  elif (rem == 1):
    painter.color(color_3)
     # location of next floor
  
   
  #draw the floor
  for floor in range(3):
    painter.goto(x, y)
    painter.pendown()
    painter.forward(50)
    y = y + 5
    

  if (current_floor % 21 == 0):
    x +=75
    y =-150   
    Tower_Number += 1
wn = trtl.Screen()
wn.mainloop()