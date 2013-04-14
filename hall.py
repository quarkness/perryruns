import RPi.GPIO as GPIO
import time
import math

pimpampet_diameter = 8
hamster_wheel_diameter = 13

hall = 3
passes = []
distance = 0
rotation_distance = hamster_wheel_diameter * math.pi / 100
# rotation_distance = pimpampet_diam    eter * math.pi / 100
run_timeout = 10
rotation = 0


def setup_pins():
    # Use physical pin numbers
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(hall, GPIO.IN)


def rotations_per_second(start, end):
    p = [t for t in passes if t > start and t < end]
    return len(p)


def track(t):
    passes.append(t)
    rotation = len(passes)
    et = t - passes[0]
    # if rotation == 1:
    #     print 'Perry rent!'
    try:
        dt = passes[-1] - passes[-2]
        speed = rotation_distance / dt * 3.6
        # rps = rotations_per_second()
    except:
        dt = 0
        speed = 0
    print "%-4s] %-15s | %-15s | %-15s " % (rotation, et, dt, speed)
    # print '{:>4} {:.2}'.format(len(passes), dt)


setup_pins()

start_time = 0
previous = 1
is_running = False
last_time = time.time()

print '1 omwenteling is %2f meter' % rotation_distance

while 1 == 1:
    current = GPIO.input(hall)
    if is_running and (time.time() - last_time > run_timeout):
        is_running = False
        print 'Perry is gestopt'
    if current and current != previous:
        last_time = time.time()
        if not is_running:
            is_running = True
            print 'Perry rent!'
        track(last_time)

    previous = current




