import RPi.GPIO as GPIO
from time import sleep


class Prototype:
    def __init__(self):
        # Hardware PWM available on GPIO12, GPIO13, GPIO18, GPIO19
        self.enableA = 0  # Phisycal pin 12
        self.input1 = 0
        self.input2 = 0

        self.enableB = 0  # Phisycal pin 35
        self.input3 = 0
        self.input4 = 0

        GPIO.setmode(GPIO.BOARD)

        channel_list = (self.enableA, self.input1, self.input2,
                        self.enableB, self.input3, self.input4)

        GPIO.setup(channel_list, GPIO.OUT)

        frequency = 0

        self.pwm_a = GPIO.PWM(self.enableA, frequency)
        self.pwm_b = GPIO.PWM(self.enableB, frequency)

        self.pwm_a.start(0)
        self.pwm_b.start(0)

    # m = True -> Motor A
    # m = False -> Motor B
    def signals(self, inputs, signal, m, sp):
        GPIO.output(inputs, signal)
        if m:
            self.pwm_a.ChangeDutyCycle(sp)
        else:
            self.pwm_b.ChangeDutyCycle(sp)

    def ForwardMotorA(self, tm=0):
        # self.signals((self.input1,self.input2), (GPIO.LOW, GPIO.HIGH), True, 50)
        if tm == 0:
            GPIO.output(self.input1, GPIO.LOW)
            GPIO.output(self.input2, GPIO.HIGH)
            self.pwm_a.ChangeDutyCycle(50)
        else:
            GPIO.output(self.input1, GPIO.LOW)
            GPIO.output(self.input2, GPIO.HIGH)
            self.pwm_a.ChangeDutyCycle(50)
            sleep(tm)
            GPIO.cleanup((self.input1, self.input2))


    def ForwardMotorB(self, tm=0):
        # self.signals((self.input3,self.input4), (GPIO.HIGH, GPIO.LOW), False, 50)
        if tm == 0:
            GPIO.output(self.input3, GPIO.HIGH)
            GPIO.output(self.input4, GPIO.LOW)
            self.pwm_b.ChangeDutyCycle(50)
        else:
            GPIO.output(self.input3, GPIO.HIGH)
            GPIO.output(self.input4, GPIO.LOW)
            self.pwm_b.ChangeDutyCycle(50)
            sleep(tm)
            GPIO.cleanup((self.input3, self.input4))

    def ReverseMotorA(self, tm=0):
        # self.signals((self.input1,self.input2), (GPIO.HIGH, GPIO.LOW), True, 50)
        if tm == 0:
            GPIO.output(self.input1, GPIO.HIGH)
            GPIO.output(self.input2, GPIO.LOW)
            self.pwm_a.ChangeDutyCycle(50)
        else:
            GPIO.output(self.input1, GPIO.HIGH)
            GPIO.output(self.input2, GPIO.LOW)
            self.pwm_a.ChangeDutyCycle(50)
            sleep(tm)
            GPIO.cleanup((self.input1, self.input2))


    def ReverseMotorB(self, tm=0):
        # self.signals((self.input3,self.input4), (GPIO.LOW, GPIO.HIGH), False, 50)
        if tm == 0:
            GPIO.output(self.input3, GPIO.LOW)
            GPIO.output(self.input4, GPIO.HIGH)
            self.pwm_b.ChangeDutyCycle(50)
        else:
            GPIO.output(self.input3, GPIO.LOW)
            GPIO.output(self.input4, GPIO.HIGH)
            self.pwm_b.ChangeDutyCycle(50)
            sleep(tm)
            GPIO.cleanup((self.input3, self.input4))

    def ForwardBoth(self, tm=0):
        if tm == 0:
            self.ForwardMotorA()
            self.ForwardMotorB()
        else:
            self.ForwardMotorA()
            self.ForwardMotorB()
            sleep(tm)
            GPIO.cleanup()

    def ReverseBoth(self, tm=0):
        if tm == 0:
            self.ReverseMotorA()
            self.ReverseMotorB()
        else:
            self.ReverseMotorA()
            self.ReverseMotorB()
            sleep(tm)
            GPIO.cleanup()

    # Move motor A - Forward - with Speed = speed
    def ForwardMotorAwSpeed(self, speed, tm=0):
        # self.signals((self.input1,self.input2), (GPIO.LOW, GPIO.HIGH), True, speed)
        if tm == 0:
            GPIO.output(self.input1, GPIO.LOW)
            GPIO.output(self.input2, GPIO.HIGH)
            self.pwm_a.ChangeDutyCycle(speed)
        else:
            GPIO.output(self.input1, GPIO.LOW)
            GPIO.output(self.input2, GPIO.HIGH)
            self.pwm_a.ChangeDutyCycle(speed)
            sleep(tm)
            GPIO.cleanup((self.input1, self.input2))

    def ForwardMotorBwSpeed(self, speed, tm=0):
        # self.signals((self.input3,self.input4), (GPIO.HIGH, GPIO.LOW), False, speed)
        if tm == 0:
            GPIO.output(self.input3, GPIO.HIGH)
            GPIO.output(self.input4, GPIO.LOW)
            self.pwm_b.ChangeDutyCycle(speed)
        else:
            GPIO.output(self.input3, GPIO.HIGH)
            GPIO.output(self.input4, GPIO.LOW)
            self.pwm_b.ChangeDutyCycle(speed)
            sleep(tm)
            GPIO.cleanup((self.input3, self.input4))

    def ReverseMotorAwSpeed(self, speed, tm=0):
        # self.signals((self.input1,self.input2), (GPIO.HIGH, GPIO.LOW), True, speed)
        if tm == 0:
            GPIO.output(self.input1, GPIO.HIGH)
            GPIO.output(self.input2, GPIO.LOW)
            self.pwm_a.ChangeDutyCycle(speed)
        else:
            GPIO.output(self.input1, GPIO.HIGH)
            GPIO.output(self.input2, GPIO.LOW)
            self.pwm_a.ChangeDutyCycle(speed)
            sleep(tm)
            GPIO.cleanup((self.input1, self.input2))

    def ReverseMotorBwSpeed(self, speed, tm=0):
        # self.signals((self.input3,self.input4), (GPIO.LOW, GPIO.HIGH), False, speed)
        if tm == 0:
            GPIO.output(self.input3, GPIO.LOW)
            GPIO.output(self.input4, GPIO.HIGH)
            self.pwm_b.ChangeDutyCycle(speed)
        else:
            GPIO.output(self.input3, GPIO.LOW)
            GPIO.output(self.input4, GPIO.HIGH)
            self.pwm_b.ChangeDutyCycle(speed)
            sleep(tm)
            GPIO.cleanup((self.input3, self.input4))

    def ForwardBothwSpeed(self, speed, tm=0):
        if tm == 0:
            self.ForwardMotorAwSpeed(speed)
            self.ForwardMotorBwSpeed(speed)
        else:
            self.ForwardMotorAwSpeed(speed)
            self.ForwardMotorBwSpeed(speed)
            sleep(tm)
            GPIO.cleanup()

    def ReverseBothwSpeed(self, speed, tm=0):
        if tm == 0:
            self.ReverseMotorAwSpeed(speed)
            self.ReverseMotorBwSpeed(speed)
        else:
            self.ReverseMotorAwSpeed(speed)
            self.ReverseMotorBwSpeed(speed)
            sleep(tm)
            GPIO.cleanup()

    def StopAll(self):
        GPIO.cleanup()

    def StopMotorA(self):
        GPIO.cleanup((self.input1, self.input2))

    def StopMotorB(self):
        GPIO.cleanup((self.input3, self.input4))