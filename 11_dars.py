satr = input('So`z kiriting: ')
if satr.isdigit() and int(satr) > 0 and int(summa) < 1000000000:
	print('Tashakkur')
else:
	print('Xatolik bor!')



for s in satr:
	if s.isdigit():
		continue
		print('Sinish jarayoni: ', s)
		break
	print(s)

from turtle import Turtle, Screen
oyna = Screen()
oyna.title('Ozodbekning oynasi')
chiziq = Turtle()
chiziq.color('blue')
chiziq.pensize(5)
chiziq.speed(0)
chiziq.hideturtle()
chiziq.up()
chiziq.goto(300, 300)
chiziq.down()
chiziq.goto(-300, -300)
chiziq.goto(-300, 300)
chiziq.goto(300, 300)
chiziq.goto(300, -300)
chiziq.goto(-300, 300)
chiziq.goto(300, 300)
chiziq.goto(300, -300)
chiziq.goto(-300, -300)

koptok = Turtle()
koptok.shape('circle')
koptok.color('green')
koptok.up()
koptok.goto(300, 300)
koptok.goto(300, 300)
koptok.goto(-300, -300)
koptok.goto(300, 300)

koptok.goto(0, 0)
chiziq.down()
koptok.goto(-300, 300)
koptok.goto(300, -300)
koptok.goto(-300, -300)
koptok.goto(300, 300)

koptok.goto(0, 0)

step_x = 3
step_y = 2
while True:
	x, y = koptok.position()
	if x + step_x >= 300 or x + step_x <= -300:
		step_x = -step_x

	if y + step_y >= 300 or y + step_y <= -300:
		step_y = -step_y
	koptok.goto(x+step_x, y+step_y)

	

oyna.mainloop()