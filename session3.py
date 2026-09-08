from turtle import* 

#گلبرگ ها
for i in range (6): 
    fillcolor("yellow")
    begin_fill()
    pencolor("brown")
    pensize(5)
    circle(60)
    end_fill()
    left(60)

#وسط گل
fillcolor("purple")
begin_fill()
pencolor("brown")
circle(35)
end_fill()

#پایین گل
penup()
right(90)
forward(35)
pendown()

#ساقه
pencolor("barkred")
pensize(10)
forward(250)

#برگ
left(45)
fillcolor("yellow")
begin_fill()
circle(50, 90)
end_fill()

hideturtle()
done()









