class State:
    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass

class StateManager:
    def __init__(self, settings, sound_manager):
        self.state = None
        self.settings = settings
        self.sound_manager = sound_manager

    def set_state(self, state):
        self.state = state(self.settings, self.sound_manager)

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