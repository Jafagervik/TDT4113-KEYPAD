

class FSM:
    """
    The finite state machine will take input given from the agent, and change
    state for each character received. We start in S_0 and the final state S_n
    where n is the amount of characters inputed.
    """

    def init(self, state, signal):
        self.state = 0
        self.signal = signal
        self.n = 0

    def signal_to_state(self, signal):
        if self.state == 0 and self.signal == 8:
            self.state = 1
        elif self.state == 0:
            self.state = 0
        elif self.state == 1 and self.signal == 3:
            self.state = 2

    def add_state(self):
        self.n += 1