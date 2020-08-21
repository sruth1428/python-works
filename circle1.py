import turtle as t

t.speed(6)
t.pensize(5)

for i in ["red","green","blue","pink","violet","brown"]:
    print(i)
    t.color(i)
    t.circle(50)
    t.rt(60)
