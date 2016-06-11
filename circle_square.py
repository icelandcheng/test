import turtle
        
def draw_circle():
    window = turtle.Screen()
    window.bgcolor("red")
    cir = turtle.Turtle()
    cir.shape("classic")
    cir.color("yellow")


    for i in range(0,36):
        num=1
        while(num<5):
            cir.forward(100)
            cir.right(90)
            num=num+1
        cir.right(10)
        
    window.exitonclick()

draw_circle()
