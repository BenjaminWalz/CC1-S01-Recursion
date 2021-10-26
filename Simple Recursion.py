#Ben Walz
#Simple Recursion


#imports turtle
import turtle
#renames turtle and screem
t = turtle.Turtle()
myWin = turtle.Screen()


#function
def shape(x, t):
   #Base Case - stops the code when false
   if x > 1:
        #moves turtle forward x
        t.forward(x)
        #moves 20 degrees to right
        t.right(20) 
        
        t.forward(x)
        
        t.left(50)
        
        shape(x-2,t)
        
           



shape(50, t)
myWin = exitonclick()