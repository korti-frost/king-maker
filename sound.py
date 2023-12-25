import pygame

def add_musics(sound_manager):
    sound_manager.load_music('main_menu', r'data\music\01 The Kingdom Awaits.wav')

def add_sounds(sound_manager):
    sound_manager.load_sound('button_click', r'data\sound\sfx_button_select1.wav')

class SoundManager:
    def __init__(self):
        self.sounds = {}  # Dictionary to store sounds
        self.music = {}  # Dictionary to store music

        # Set the default volume
        self.volume_sounds = 0.5
        self.volume_music = 0.5

        # Load the sounds and music to the dictionaries
        add_sounds(self)
        add_musics(self)

    def load_sound(self, name, path):
        # Load a sound and store it in the dictionary
        self.sounds[name] = pygame.mixer.Sound(path)
        self.sounds[name].set_volume(self.volume_sounds)

    def play_sound(self, name):
        # Play a sound
        if name in self.sounds:
            self.sounds[name].play()

    def load_music(self, name, path):
        # Load a music track and store it in the dictionary
        self.music[name] = path
        pygame.mixer.music.load(self.music[name])
        pygame.mixer.music.set_volume(self.volume_music)

    def play_music(self, name):
        # Play a music track
        if name in self.music:
            pygame.mixer.music.load(self.music[name])
            pygame.mixer.music.play(-1)  # Play the music indefinitely

    def set_sound_volume(self, volume):
        # Set the volume for all sounds
        for sound in self.sounds.values():
            sound.set_volume(volume)

    def set_music_volume(self, volume):
        # Set the volume for the music
        pygame.mixer.music.set_volume(volume)