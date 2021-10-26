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
            t.left(20)
            t.bk(10)
            t.left(40)
            t.forward(10)
            t.bk(10)
            t.right(20)
            t.bk(20)
            t.left(40)
            t.forward(20)
            t.right(20)
            t.forward(10)
            t.bk(10)
            t.left(40)
            t.forward(10)
            t.bk(10)
            t.right(20)
            t.bk(20)
            t.right(20)
            t.bk(30)
            t.left(40)
            branchlen = branchlen + 30
            while branchlen > 1:
                t.forward(branchlen)
                t.left(20)
                branchlen = branchlen - 10
                if branchlen == 0:
                    t.right(20)
                    t.bk(10)
                    t.right(40)
                    t.forward(10)
                    t.bk(10)
                    t.left(20)
                    t.bk(20)
                    t.right(40)
                    t.forward(20)
                    t.right(20)
                    t.forward(10)
                    t.bk(10)
                    t.left(40)
                    t.forward(10)
                    
            
tree(40, t)
myWin.exitonclick()
        
        
        



