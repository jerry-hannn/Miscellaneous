import board
import digitalio
import array
import time

print(board.board_id)
# motorPWM = pulseio.PulseOut(board.GP0, frequency=38000, duty_cycle=32768)

# pulses = array.array('H', [10000])

# motorPWM.send(pulses)

pwm = digitalio.DigitalInOut(board.GP0) #Power
dir = digitalio.DigitalInOut(board.GP3) #Direction
pwm.direction = digitalio.Direction.OUTPUT
dir.direction = digitalio.Direction.OUTPUT

pwm.value = False 
dir.value = False

#change pin numbers if needed
top_button = digitalio.DigitalInOut(board.GP5) 
bottom_button = digitalio.DigitalInOut(board.GP6)
button = digitalio.DigitalInOut(board.GP7)

top_button.direction = digitalio.Direction.INPUT
bottom_button.direction = digitalio.Direction.INPUT
button.direction = digitalio.Direction.INPUT

top_button.pull = digitalio.Pull.UP
bottom_button.pull = digitalio.Pull.UP
button.pull = digitalio.Pull.UP

state = 0 #0 = stop, 1 = up, 2 = down
next_state = 1 
old_top = 1
old_bottom = 1
old_button = 1



while True:
    print(next_state)
    #print(state)
    #print("loop running")
    if state == 0:
        pwm.value = False
        dir.value = False
    elif state == 1:
        pwm.value = True
        dir.value = True
        next_state = 0
    elif state == 2:
        pwm.value = True
        dir.value = False
        next_state = 0
    # print(button.value)
    # if (button.value == 0 and old_button == True):
    #     print("button pressed")
    if (state == 0) and (button.value == 0 and old_button == 1):
        state = next_state
    # if (state == 1) and (button.value == 0 and old_button == 1):
    #     state = next_state
    # if (state == 2) and (button.value == 0 and old_button == 1):
    #     state = next_state
    if (top_button.value == 0 and old_top == 1):
        state = next_state
        next_state = 2
    if (bottom_button.value == 0 and old_bottom == 1):
        state = next_state
        next_state = 1
    if ((top_button.value == 0 and old_top == 1) or (bottom_button.value == 0 and old_bottom == 1)) and (button.value == 0 and old_button == 1):
        state = next_state

    old_top = top_button.value
    old_bottom = bottom_button.value
    old_button = button.value
