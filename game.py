#pong game

#this is a graphics module
import turtle
import winsound

#get the interface
win = turtle.Screen()
#title of the game
win.title('pong by kendo')
#backgroundcolour
win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(0)

time = 0

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 0.3
ball.dy = -0.3

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('playerA: 0  PlayerB: 0', align='center', font=('Courier',24,'normal'))

score_a = 0
score_b = 0

#functions for the game
#up for paddle a
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
#down for paddle a
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
# up for paddle b
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
# down for paddle b
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)



#keyboard binding(creating key listeners)
win.listen()
#make the paddle a go up
win.onkeypress(paddle_a_up,'w')
#make the paddle a go down
win.onkeypress(paddle_a_down,'s')
#make paddle b go up
win.onkeypress(paddle_b_up,'Up')
#make paddle b go down
win.onkeypress(paddle_b_down,'Down')    

kendo = True
#loop of the game
while kendo:
    win.update()
    time +=1
    

    # move ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy) 

    #border checking
    if ball.ycor()> 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write('playerA: {}  PlayerB: {}'.format(score_a,score_b), align='center', font=('Courier',24,'normal'))
        

    if ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('playerA: {}  PlayerB: {}'.format(score_a,score_b), align='center', font=('Courier',24,'normal'))

    

    
    


    #paddle bounce with ball
    if (ball.xcor() > 330 and ball.xcor()<350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(330)
        ball.dx *= -1

    if (ball.xcor() < -330 and ball.xcor()> -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-330)
        ball.dx *= -1

    #try to end game 
    if score_a==8 :
        win.update()
        win.bgcolor('white')
        wining = turtle.Turtle()
        wining.hideturtle()
        wining.penup()
        wining.speed(0)
        wining.goto(0,0)
        
        wining.write('playerA Wins',align='center', font=('Courier',24,'normal'))
        length_of_play = turtle.Turtle()
        length_of_play.speed(0)
        length_of_play.hideturtle()
        length_of_play.penup()
        length_of_play.goto(-250,-50)
        length_of_play.write('you played for {} seconds'.format(time),font=('Courier',24,'normal')) 
    if score_b==8:
        win.update()
        win.bgcolor('white')
        winingB = turtle.Turtle()
        winingB.hideturtle()
        winingB.penup()
        winingB.speed(0)
        winingB.goto(0,0)
        
        winingB.write('playerB Wins',align='center', font=('Courier',24,'normal'))
        length_of_play = turtle.Turtle()
        length_of_play.speed(0)
        length_of_play.hideturtle()
        length_of_play.penup()
        length_of_play.goto(-50,-50)
        length_of_play.write('you played for {} seconds'.format(time),font=('Courier',24,'normal'))
        

        