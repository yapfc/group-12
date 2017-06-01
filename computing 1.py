from microbit import*

DELAY=20
FRAMES_PER_WALL_SHIFT=20
FRAMES_PER_NEW_WALL=100
FRAMES_PER_SCORE=50

y=50
speed=0
score=0
frame=0

def make_pipe():
    pipe=Image("00003:00003:000003:00003:00003")
    """00003
       00003
       00003
       00003
       00003
       
       result:
       00003
       00003
       00000
       00003
       00003
       """
    gap=random.randint(0,3)
    
    pipe.set_pixel(4,gap,0)
    pipe.set_pixel(4,gap+1,0)
    return pipe
    
pipe = make_pipe()

while True:
    display.show(pipe)
    
    if button_a.is_pressed():
        speed=-8
        
    speed=+=1
    if speed > 2:
        speed = 2
        
    y += speed
    
    if y>99:
        y=99
    if y<0:
        y=0
        
    bird_y=int(y/20)
    display.set_pixel(1,bird_y,9)
    
    if pipe.get_pixel(1,bird_y) != 0:
        display.show(Image.SAD)
        sleep(500)
        display.scroll("score:" + str(score))
        break
        
    if frame % FRAMES_PER_WALL_SHIFT ==0:
        pipe=pipe.shift_left()
        
    if frame % FRAMES_PER_NEW_WALL == 0:
        pipe=make_pipe()
        
    if frame % FRAMES_PER_SCORE == 0:
        score += 1 :
            
    sleep(DELAY)
    frame += 1
         