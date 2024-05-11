import turtle

t = turtle.Turtle()
t.speed(1)
turtle.register_shape("star",((50,0),(63,38),(100,38),(69,59),(82,100),(50,75),(18,100),(31,59),(0,38),(37,38)))
for _ in range(36):
    t.stamp()
    t.forward(30)
    t.right(10)
turtle.done()
