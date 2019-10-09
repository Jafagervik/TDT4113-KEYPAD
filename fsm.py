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
        """self.states = [
            "S-Init",
            "S-Read",
            "S-Verify",
            "S-Active",
            "S-Read2",
            "S-Read3"
        ]"""
        self.state = 1 # Initialize state of the FSM
        #self.final_state = self.states[len(self.states)-1]
        self.rules = []

        #                       INIT
        self.add_rule(Rule(1, 2, "all_symbols", self.agent.reset_password_accumulator()))

        #                       READ
        self.add_rule(Rule(2, 2, "signal_is_digit", self.agent.append_next_password_digit()))
        self.add_rule(Rule(2, 3, "*", self.agent.verify_password()))
        self.add_rule(Rule(2, 1, "@", self.agent.reset_agent()))

        #                       VERIFY
        self.add_rule(Rule(3, 4, "Y", self.agent.verify_password())) #verify_login()?
        self.add_rule(Rule(3, 1, "@", self.agent.reset_agent()))

        #                       ACTIVE
        self.add_rule(Rule(4, 5, "*", self.agent.reset_password_accumulator()))

        #                       READ-2
        self.add_rule(Rule(5, 5, "is_digit(s)", self.agent.append_new_password_digit()))
        self.add_rule(Rule(5, 6, "*", self.agent.cache_first_new_password()))
        self.add_rule(Rule(5, 4, "@", self.agent.reset_agent()))

        #                       READ-3
        self.add_rule(Rule(6, 6, "is_digit()", self.agent.append_new_password_digit()))
        self.add_rule(Rule(6, 4, "*", self.agent.compare_new_passwords()))
        self.add_rule(Rule(6, 4, "@", self.agent.reset_agent()))

    def add_rule(self, rule):
        self.rules.append(rule)

    def get_next_signal(self):
        self.agent.get_next_signal()

    def run_rules(self):
        # while rule in self.rules is not fired:
        # do someting
        i = 0
        while not self.fire_rule(self.rules[i]):
            self.apply_rule()
            i += 1


    def apply_rule(self):
        # if condition is met THEN apply rule
        pass

    def fire_rule(self, rule):
        rule.action(2)
        self.state = rule.state2


    def main_loop(self):
        keypad = Keypad()
        ledboard = Ledboard()

        while self.state < 7:
            symbol = self.get_next_signal()
            for rule in self.rules:
                if rule.state1 is self.state and rule.symbol is symbol:
                    self.state = rule.state2
                    #agent.do_action(rule.action, symbol)
            #Kanskje noe skal her

        #Shutdowns
        self.agent.exit_action()
        #keypad.shutdown()
        ledboard.shutting_down()

def signal_is_digit(signal):
    return 48 <= ord(signal) <= 57

def all_symbols(signal):
    return 0 <= ord(signal) <= 255


####                      MÅ ENDRE FSM STATE I KPC NÅR EN FUNKSJON KALLES!!!!!!!!