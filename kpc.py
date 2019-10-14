"""hei"""

import os
import fsm
import keypad
import ledboard


class KPC:
    """
    Keypad Controller Agent class
    """

    def __init__(self, fsm):

        self.fsm = fsm  # pointer to fsm
        self.i = 0
        self.keypad = fsm.keypad  # pointer to keypad
        self.ledboard = fsm.ledboard  # pointer to ledboard
        self.cp = self.load_pass()
        self.cump = ""  # list of strings, password-buffer and entered numbers
        self.pathname_complete = os.getcwd() + r"\password.txt"  # path to password text
        self.override_signal = None  # override-signal
        # slots for holding LED id(lid)& Ldur, both entered via keypad
        self.led_id = None
        self.led_dur = None

    def init_passcode_entry(self):
        """Clear the passcode-buffer and initiate a ”power up” lighting sequence
        on the LED Board. This should be done when the user first presses the keypad."""
        self.cump = ""
        self.ledboard.powering_up()

    """
    def get_next_signal(self):
        Return the override-signal, if it is non-blank; otherwise query the keypad
        for the next pressed key.
        if self.override_signal:
            return self.override_signal
        return self.keypad.get_next_signal()
    """

    def get_next_signal(self):
        """ Return the override-signal, if it is non-blank; otherwise query the keypad
        for the next pressed key."""
        if not self.override_signal:
            self.cump += self.keypad.get_next_signal()

    def verify_login(self):
        """Check that the password just entered via the keypad matches that in the password file.
        Store the result (Y or N) in the override-signal. Also, this should call the LED
        Board to initiate the appropriate lighting pattern for login success or failure"""
        # f = open(k.pathname_complete, "r")
        # corr_pass = f.read()
        if self.compare_new_passwords(self.cump):
            self.override_signal = "Y"
            self.flash_leds()
        else:
            self.override_signal = "N"
            self.twinkle_leds()

    def validate_password_change(self):
        """Check that the new password is legal. If so, write the new password in the password file.
        A legal password should be at least 4 digits long and should
        contain no symbols other than the digits 0-9. As in verify login, this should use the LED
        Board to signal success or failure in changing the password.2"""

        if self.verify_password(self.cump):
            self.cache_first_new_password()
            self.override_signal = "Y"
            self.flash_leds()
        else:
            self.override_signal = "N"
            self.twinkle_leds()

    def light_one_led(self):
        """Using values stored in the Lid and Ldur slots, call the LED Board and request
        that LED # Lid be turned on for Ldur seconds."""
        self.ledboard.light_led(self.led_id, self.led_dur)

    def flash_leds(self):
        """ Call the LED Board and request the flashing of all LEDs."""
        self.ledboard.flash_all_leds()

    def twinkle_leds(self):
        """Call the LED Board and request the twinkling of all LEDs."""
        self.ledboard.twinkle_all_leds()

    def exit_action(self):
        """Call the LED Board to initiate the ”power down” lighting sequence."""
        # shutdown method - power down lightning sequence
        self.ledboard.shutting_down()

    # Rule Methods For FSM
    def do_action(self, rule):
        """hei"""
        rule.action(self, rule.symbol)

    def reset_password_accumulator(self):
        """hei"""
        self.cump = ""  # eller skal selve tekstfilen tømmes????

    def append_next_password_digit(self, symbol):
        """hei"""
        self.cump += symbol

    """
    def reset_agent(self, symbol):

        pass
    """

    def verify_password(self, symbol):
        """hei"""
        if len(symbol) > 3:
            for i in symbol:
                if not str.isdigit(i):
                    return False
            return True
        return False

    def cache_first_new_password(self):
        """hei"""
        try:
            with open(self.pathname_complete, 'w') as f:
                f.write(self.cump)
        except FileNotFoundError:
            print("Could not open file!")

    def load_pass(self):
        """hei"""
        try:
            with open(self.pathname_complete, 'r') as f:
                return f.read()
        except FileNotFoundError:
            print("Could not open file!")

    def compare_new_passwords(self, symbol):
        """hei"""

        for line in self.cp:
            for char in range(len(line)):
                if line[char] != symbol[char]:
                    return False
        return True


#k = KPC()
#f = open(k.pathname_complete, "r")
#print(f.read())
