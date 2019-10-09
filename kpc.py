

class KPC:
    """
    Keypad Controller Agent class
    """

    def __init__(self):
        self.i = 0

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
    def reset_password_accumulator(self):
        pass

    def append_next_password_digit(self):
        pass

    def reset_agent(self):
        pass

    def verify_password(self):
        pass

    def cache_first_new_password(self):
        pass

    def compare_new_password_digit(self, password):
        with open('password.txt', "r") as f:
            pwd = f.read()
            for line in pwd:
                for char in range(len(line)):
                    if line[char] != password[char]:
                        return False
            return True
