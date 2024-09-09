import os
from pyfmodex.system import System
from pyfmodex.flags import MODE


class SoundManager:
    def __init__(self, base_path="assets/sounds"):
        """
        Initializes the FMOD system and sets up the base path for sound assets.
        """
        self.base_path = base_path
        self.fmod_system = System()
        self.fmod_system.init()
        self.sounds = {}  # Cache loaded sounds

    def load_sound(self, sound_name):
        """
        Loads a sound from the base path and stores it in the cache.
        Appends '.mp3' to the sound_name and loads it if not already loaded.
        """
        sound_path = os.path.join(self.base_path, f"{sound_name}.mp3")

        if sound_name not in self.sounds:
            if not os.path.exists(sound_path):
                raise FileNotFoundError(f"Sound file not found: {sound_path}")

            # Load the sound and store it in the cache
            sound = self.fmod_system.create_sound(sound_path, mode=MODE.DEFAULT)
            self.sounds[sound_name] = sound

    def play_sound(self, sound_name):
        """
        Plays a sound. If the sound is not loaded yet, it loads it first.
        """
        # Load the sound if not loaded
        if sound_name not in self.sounds:
            self.load_sound(sound_name)

        # Play the sound
        self.fmod_system.play_sound(self.sounds[sound_name])
        
        # Update FMOD system to keep audio playing smoothly
        self.fmod_system.update()

    def stop_all_sounds(self):
        """
        Stops all currently playing sounds.
        """
        self.fmod_system.mixer_stop_all()

sound = SoundManager()