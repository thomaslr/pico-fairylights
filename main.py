import machine
import utime
import fairylights

"""
led1 = machine.Pin(8, machine.Pin.OUT)

try:
    while True:
        led1.toggle()
        utime.sleep(1)
finally:
    led1.off()
"""

led1 = machine.PWM(machine.Pin(8))


while True:
    fairylights.set_cycle(led1, 65000, 10000, 1000)

while True:
    fairylights.set_on_off(led1, 60000, 1)


pwm = machine.PWM(machine.Pin(8))

pwm.freq(1000)


while True:
    pwm.duty_u16(60000)
    utime.sleep(1)
    pwm.duty_u16(0)
    utime.sleep(1)


while True:
    # sleep time controls period/frequency of pulse
    for duty in range(65025):
        pwm.duty_u16(duty)
        utime.sleep(0.0001)
    for duty in range(65025, 0, -1):
        pwm.duty_u16(duty)
        utime.sleep(0.0001)
