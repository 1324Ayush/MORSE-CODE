import sys

try:
    import keyboard  # pip install keyboard
except Exception as e:
    print("Failed to import 'keyboard'. Make sure you installed it (pip install keyboard) and run with appropriate privileges.")
    raise

MORSE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.',  '(': '-.--.',  ')': '-.--.-',
    '&': '.-...',  ':': '---...', ';': '-.-.-.',
    '=': '-...-',  '+': '.-.-.',  '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-',
    '@': '.--.-.'
}

def to_morse(ch: str) -> str:
    """Return morse string for a single character, or empty string if unsupported."""
    return MORSE.get(ch.upper(), '')

print("Live Morse Code Typing")
print("-------------------------------------------------")
print("Type on your keyboard and see Morse code instantly.")
print("Spacebar = / (word separator)")
print("Enter    = new line")
print("Esc      = exit")
print("Backspace= shown as <BS>")
print("-------------------------------------------------\n")

try:
    while True:
        event = keyboard.read_event()
        if event.event_type != keyboard.KEY_DOWN:
            continue

        key = event.name

        if key == "esc":
            print("\n[Exiting live Morse typing]")
            sys.exit(0)

        if key == "space":
            print(" / ", end="", flush=True)
            continue

        if key == "enter":
            print()
            continue

        if key == "backspace":
            # visual indicator for backspace (you can change behavior as desired)
            print("<BS>", end="", flush=True)
            continue

        # If it's a single-character key like 'a', '1', '.', etc.
        if len(key) == 1:
            code = to_morse(key)
            if code:
                print(code, end=" ", flush=True)
            else:
                print("<?>", end="", flush=True)

        # ignore other keys (shift, ctrl, alt, etc.)

except KeyboardInterrupt:
    print("\n[Stopped by user]")
