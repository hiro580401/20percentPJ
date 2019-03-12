# coding=<UTF-8>

from datetime import datetime
import time
import RPi.GPIO as GPIO

# Interval
INTERVAL = 3
# Sleeptime
SLEEPTIME = 20
# Used GPIO
GPIO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN)

if __name__ == '__main__':
    try:
        print ("Cancel the operation: Ctrl + C")
        cnt = 1
        while True:
            # Censing
            if(GPIO.input(GPIO_PIN) == GPIO.HIGH):
                print(datetime.now().strftime('%Y/%m/%d %H:%M:%S') +
                ":" + str"{0:05d}".format(cnt)) + "times")
                cnt = cnt + 1
                time.sleep(SLEEPTIME)
            else:
                print(GPIO.input(GPIO_PIN))
                time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("Finishing...")
    finally:
        GPIO.cleanup()
        print("GPIO clean is done")
