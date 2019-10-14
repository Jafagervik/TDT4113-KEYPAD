from kpc import KPC
from keypad import Keypad
from ledboard import Ledboard
from rule import Rule
from inspect import isfunction


class FSM:
    """
    The finite state machine will take input given from the agent, and change
    state for each character received. We start in S_0 and the final state S_n
    where n is the amount of characters inputed.
    """

    def __init__(self):
        self.agent = KPC() # Pointer to the KPC object
        self.keypad = Keypad()
        self.ledboard = Ledboard()

        self.state = 1 # Initialize state of the FSM
        self.final_state = 7 #not a state, if we end up here we're outside the state machine
        self.rules = []
        self.curr_rules = []

    def setup(self, signal):
        """
        Sets up all of the rules for the
        :return: void
        """
        #                       INIT
        self.add_rule(Rule(1, 2, all_symbols(signal), self.agent.reset_password_accumulator()))

        #                       READ
        self.add_rule(Rule(2, 2, signal_is_digit(signal), self.agent.append_next_password_digit()))
        self.add_rule(Rule(2, 3, asterisk(signal), self.agent.verify_login()))
        self.add_rule(Rule(2, 1, True, self.agent.reset_agent()))

        #                       VERIFY
        self.add_rule(Rule(3, 4, self.override_signal_y(), self.agent.verify_login()))  # verify_login()?
        self.add_rule(Rule(3, 1, True, self.agent.reset_agent()))

        #                       ACTIVE
        self.add_rule(Rule(4, 5, asterisk(signal), self.agent.reset_password_accumulator()))
        self.add_rule(Rule(4, 4, not asterisk(signal), self.agent.reset_agent()))

        #                       READ-2
        self.add_rule(Rule(5, 5, signal_is_digit(signal), self.agent.append_new_password_digit()))
        self.add_rule(Rule(5, 6, asterisk(signal), self.agent.cache_first_new_password()))
        self.add_rule(Rule(5, 4, True, self.agent.reset_agent()))

        #                       READ-3
        self.add_rule(Rule(6, 6, signal_is_digit(signal), self.agent.append_new_password_digit()))
        self.add_rule(Rule(6, 4, asterisk(signal), self.agent.compare_new_passwords()))
        self.add_rule(Rule(6, 4, True, self.agent.reset_agent()))

    def add_rule(self, rule):
        self.rules.append(rule)

    def override_signal_y(self):
        return True if self.agent.override_signal == "Y" else False

    def get_next_signal(self):
        self.agent.get_next_signal()

    def state_handler(self, state):
        pass

    def run_rules(self):
        # while rule in self.rules is not fired:
        # do someting
        for rule in self.rules:
            if self.apply_rule(rule.state1, rule.symbol):
                self.fire_rule(rule)
                return rule.state2

    def apply_rule(self, curr_state, condition):
        # if condition is met THEN apply rule
        if curr_state is self.state and condition:
            return True
        return False

    def fire_rule(self, rule):
        rule.action()

    def main_loop(self):
        while self.state < self.final_state:
            symbol = self.get_next_signal()
            self.state = self.run_rules()
            #Kanskje noe skal her

        #Shutdowns
        self.ledboard.shutting_down()

# Methods to help us determine which method should be called
def signal_is_digit(signal):
    return 48 <= ord(signal) <= 57


def all_symbols(signal):
    return 0 <= ord(signal) <= 255


def asterisk(signal):
    return 42 == ord(signal)

