import turtle
furnitureNames = ["One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten"]
gadget= []
gadget = furnitureNames
print(gadget)
gadget = ["OneRe","TwoRe","ThreeRe","FourRe","FiveRe","SixRe","SevenRe","EightRe","NineRe","TenRe"]
for i in gadget:
    print(i)

gadget.sort(reverse=True)
print(gadget)
gadget.sort()
print(gadget)
gadget.pop(4)
gadget.pop(4)
print(gadget)
collegeOntario = ['college1','college2','college3']
gadget += collegeOntario
print(gadget)
turtle.bgcolor('yellow')
turtle.pencolor("Brown")
turtle.pensize(2)
turtle.fillcolor('green')
turtle.begin_fill()
turtle.goto(0,40)
turtle.goto(100,40)
turtle.goto(0,80)
turtle.goto(-100,40)
turtle.goto(0,40)
turtle.end_fill()
turtle.fillcolor('green')
turtle.begin_fill()
turtle.goto(0,0)
turtle.goto(100,0)
turtle.goto(0,40)
turtle.goto(-100,0)
turtle.goto(0,0)
turtle.end_fill()
turtle.fillcolor('Brown')
turtle.begin_fill()
turtle.goto(0,0)
turtle.goto(-10,0)
turtle.goto(-10,-50)
turtle.goto(10,-50)
turtle.goto(10,0)
turtle.end_fill()
turtle.done
