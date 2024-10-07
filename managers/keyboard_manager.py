import time
from pynput.keyboard import Controller
from persistence.bindings.binding import Binding

class KeyboardManager:
    keyboard = Controller()

    @staticmethod
    def tap_key(key) -> None:
        """
        Tap a single key.
        
        Parameters:
        key (str or Key): The key to tap.
        """
        KeyboardManager.keyboard.tap(key)

    @staticmethod
    def tap_keys(keys) -> None: 
        """
        Tap multiple keys in sequence without delay.
        
        Parameters:
        keys (list of str or Key): A list of keys to tap.
        """
        for key in keys:
            KeyboardManager.keyboard.tap(key)

    @staticmethod
    def tap_keys_with_delay(keys, delay) -> None:
        """
        Tap multiple keys in sequence with a delay between each tap.
        
        Parameters:
        keys (list of str or Key): A list of keys to tap.
        delay (float): The delay in seconds between each key tap.
        """
        for key in keys:
            KeyboardManager.keyboard.tap(key)
            time.sleep(delay)