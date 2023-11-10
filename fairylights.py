# library to turn on fairy lights in different patterns
import machine
import utime


def set_on_off(led, brightness, period):
    led.duty_u16(brightness)
    utime.sleep(period)
    led.duty_u16(0)
    utime.sleep(period)


# def set_rise(led, max_brightness, period):


def set_decay(led, brightness, period):
    led.duty_u16(brightness)
    utime.sleep(period)
    led.duty_u16(0)
    utime.sleep(period)


def set_cycle(led, max_brightness, min_brightness, period):
    for duty in range(min_brightness, max_brightness, 1):
        led.freq(period)
        led.duty_u16(duty)
        utime.sleep(0.0001)
    for duty in range(max_brightness, min_brightness, -1):
        led.freq(period)
        led.duty_u16(duty)
        utime.sleep(0.0001)
