import RPi.GPIO as GPIO
import time


class Ledboard:
    """
    GPIO magic
    """

    def __init__(self):
        self.pins = [18, 23, 24]

        self.pin_led_states = [
            [1, 0, -1],  # A
            [0, 1, -1],  # B
            [-1, 1, 0],  # C
            [-1, 0, 1],  # D
            [1, -1, 0],  # E
            [0, -1, 1]   # F
        ]

        self.setup()

    @staticmethod
    def setup():
        GPIO.setmode(GPIO.BCM)

    def set_pin(self, pin_index, pin_state):
        if pin_state == -1:
            GPIO.setup(self.pins[pin_index], GPIO.IN)
        else:
            GPIO.setup(self.pins[pin_index], GPIO.OUT)
            GPIO.output(self.pins[pin_index], pin_state)

    def light_led(self, led_number):
        for pin_index, pin_state in enumerate(self.pin_led_states[led_number]):
            self.set_pin(pin_index, pin_state)

    def turn_off_led(self, led_number):
        # do we need this method even?
        pass

    def flash_all_leds(self, k):
        """

        :param k: int, seconds to flash on and off for
        :return:
        """
        start = time.time()
        now = start + k**2         # sets now high enough to let the loop start
        while now - start >= k:
            for i in range(6):
                self.light_led(i)
            time.sleep(0.2)

            for i in range(5, -1):
                self.light_led(i)  # should possibly use turn_off_light
            time.sleep(0.2)
            now = time.time()

    def twinkle_all_leds(self, k):
        """

        :param k:
        :return:
        """
        while True:
            for i in range(6):
                self.light_led(i)
            time.sleep(k)

            for i in range(5, -1):
                self.light_led(i)  # should possibly use turn_off_light
            time.sleep(k)

    # Additional methods for setting up and shutting down the system
    def powering_up(self):
        for i in range(6):
            self.light_led(i)
            time.sleep(0.5)

    def shutting_down(self):
        for i in range(6):
            self.light_led(i)

        for i in range(5, -1):
            self.light_led(i) #should possibly use turn_off_light
            time.sleep(0.5)
