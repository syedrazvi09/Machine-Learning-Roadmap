import builtins
from IPython.display import display
import ipywidgets as widgets
import time

def patched_input(prompt=""):
    text = widgets.Text(description=prompt)
    display(text)

    user_input = {}

    def handle_submit(sender):
        user_input['value'] = sender.value
        text.close()

    text.on_submit(handle_submit)

    # Wait until user types something and presses Enter
    while 'value' not in user_input:
        time.sleep(0.1)
    return user_input['value']

# Replace built-in input with patched one
builtins.input = patched_input
