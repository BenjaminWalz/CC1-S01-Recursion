# CC1-S01-Recursion
#Summitve and to make it more effecient
#working code

import turtle



t = turtle.Turtle()
myWin = turtle.Screen()
backwards = 0
turn = 0


def tree(branchlen, t):
    t.left(90)
    while branchlen > 1:
        t.forward(branchlen)
        t.right(20)
        branchlen = branchlen - 10
        
        if branchlen == 0:
            #right side
            t.left(20)
            t.backward(10)
            t.left(40)
            t.forward(10)
            t.backward(10)
            t.right(20)
            t.backward(20)
            t.left(40)
            t.forward(20)
            t.right(20)
            t.forward(10)
            t.backward(10)
            t.left(40)
            t.forward(10)
            t.backward(10)
            t.right(20)
            t.backward(20)
            t.right(20)
            t.backward(30)
            t.left(20)
            #left side
            t.left(20)
            t.forward(30)
            t.left(20)
            t.forward(20)
            t.left(20)
            t.forward(10)
            t.backward(10)
            t.right(40)
            t.forward(10)
            t.backward(10)
            t.left(20)
            t.backward(20)
            t.right(40)
            t.forward(20)
            t.left(20)
            t.forward(10)
            t.backward(10)
            t.right(40)
            t.forward(10)
            t.backward(10)
            t.left(20)
            t.backward(20)
            t.left(20)
            t.backward(30)
            t.right(20)
            t.backward(40)
        
        
                
                
                
             
            
        
                
                
                    

            
        
        
        
        
tree(40, t)
myWin.exitonclick()
        
        
        



