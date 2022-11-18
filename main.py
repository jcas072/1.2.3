import turtle as trtl
import random as rand
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

wn.bgpic("background.gif")

letters = ["A", "S", "D", "F"] #list of letters

appleList = []
appleLetters = []

for i in range(5):
  appleList.append(trtl.Turtle())
  appleLetters.append(rand.choice(letters))

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(index):
  appleList[index].penup()
  appleList[index].shape(apple_image)
  wn.tracer(False)

  appleList[index].setx(rand.randint(-175,175)) #rest apple position
  appleList[index].sety(rand.randint(-25,100)) #rest apple position

  appleList[index].sety(appleList[index].ycor()-38)
  appleList[index].color("white")
  appleList[index].write(appleLetters[index], align="center", font=("Arial", 40, "bold"))
  appleList[index].sety(appleList[index].ycor()+38) 
  appleList[index].showturtle()
  wn.tracer(True)
  wn.update()

def drop_apple(index):
  appleList[index].penup()
  appleList[index].clear()
  appleList[index].sety(-150)
  appleList[index].hideturtle()
  appleLetters[index] = rand.choice(letters)
  draw_apple(index)

def typedA():
  for i in range(5):
    if appleLetters[i] == 'A':
      drop_apple(i)

def typedS():
  for i in range(5):
    if appleLetters[i] == 'S':
      drop_apple(i)

def typedD():
  for i in range(5):
    if appleLetters[i] == 'D':
      drop_apple(i)

def typedF():
  for i in range(5):
    if appleLetters[i] == 'F':
      drop_apple(i)

#-----function calls-----
for i in range(5):
  draw_apple(i)

wn.onkeypress(typedA, 'a')
wn.onkeypress(typedS, 's')
wn.onkeypress(typedD, 'd')
wn.onkeypress(typedF, 'f')

wn.listen()

wn.mainloop()
