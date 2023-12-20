class State:
    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass

class StateManager:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def handle_event(self, event):
        if self.state is not None:
            new_state = self.state.handle_event(event)
            return new_state

    def update(self):
        if self.state is not None:
            self.state.update()

    def draw(self):
        if self.state is not None:
            self.state.draw()