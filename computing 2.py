from microbit import * 
while True:
    reading_x = accelerometer.get_x()
    reading_y = accelerometer.get_y()
    
    if reading_x > 20:
        display.show("L")
    elif reading_y <-20 :
        display.show("B")
    else:
        display.show("-")