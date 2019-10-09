

class KPC:
    """
    Keypad Controller Agent class
    """

    def __init__(self):
        self.i = 0
        self.password = ""

    def init_passcode_entry(self):
        pass

    def get_next_signal(self):
        pass

    def verify_login(self):
        pass

    def validate_password_change(self):
        pass

    def light_one_led(self):
        pass

    def flash_leds(self):
        pass

    def twinkle_leds(self):
        pass

    def exit_action(self):
        # shutdown method - power down lightning sequence
        pass

    # Rule Methods For FSM
    def do_action(self, rule):
        rule.action(self, rule.symbol)

    def reset_password_accumulator(self):
        self.password = "" #eller skal selve tekstfilen tømmes????

    def append_next_password_digit(self, symbol):
        self.password += symbol

    def reset_agent(self, symbol):
        pass

    def verify_password(self, symbol):
        pass

    def cache_first_new_password(self, symbol):
        try:
            with open('password.txt', 'w') as f:
                f.write(self.password)
        except FileNotFoundError:
            print("Could not open file!")

    def compare_new_passwords(self, symbol):
        try:
            with open('password.txt', 'r') as f:
                pwd = f.read()
                for line in pwd:
                    for char in range(len(line)):
                        if line[char] != symbol[char]:
                            return False
                return True
        except FileNotFoundError:
            print("Could not open file!")
