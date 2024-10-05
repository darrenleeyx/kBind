from pynput.keyboard import Key, Controller, Listener # type: ignore
import time
from typing import List, Union, Optional

class KeyboardManager:
    def __init__(self):
        self.keyboard = Controller()

    def tap_key(self, key) -> None:
        """
        Tap a single key.
        
        Parameters:
        key (str or Key): The key to tap.
        """
        self.keyboard.tap(key)

    def tap_keys(self, keys) -> None: 
        """
        Tap multiple keys in sequence without delay.
        
        Parameters:
        keys (list of str or Key): A list of keys to tap.
        """
        for key in keys:
            self.keyboard.tap(key)
            
    def tap_keys_with_delay(self, keys, delay) -> None:
        """
        Tap multiple keys in sequence with a delay between each tap.
        
        Parameters:
        keys (list of str or Key): A list of keys to tap.
        delay (float): The delay in seconds between each key tap.
        """
        for key in keys:
            self.keyboard.tap(key)
            time.sleep(delay)

    def listen_next_key(self) -> Optional[Union[str, Key]]:
        """
        Start listening for key press events and print the key that was pressed.
        Stop listening after the first key press.
        """
        self.pressed_key = None

        def on_press(key):
            self.pressed_key = key
            return False  # Stop listener

        with Listener(on_press=on_press) as listener:
            listener.join()

        return self.pressed_key
    
if __name__ == "__main__":
    km = KeyboardManager()
    pressed_key = km.listen_next_key()
    print(f'The key pressed was: {pressed_key}')