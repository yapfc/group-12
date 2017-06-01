from microbit import * 

while True:
    presses = button_a.get_presses()
    if presses > 5:
        display.show(Image.SNAKE)
    else:
        display.show(Image.ANGRY)