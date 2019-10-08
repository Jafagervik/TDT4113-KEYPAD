

class Rule:
    """
    Rule for the fsm
    """

    def __init__(self, state1, state2, signal, action):
        self.state1 = state1
        self.state2 = state2
        self.signal = signal
        self.action = action
