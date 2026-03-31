# MORSE-CODE
PYTHON PROJECT

This repository contains a small Python script that lets you type on your keyboard and see the corresponding Morse code live in the terminal.​

Overview The script listens for key presses using the keyboard library and immediately prints the Morse code for each supported character. Special keys such as Space, Enter, Escape, and Backspace are handled with custom behavior to make interactive typing more convenient.​

Features Live translation of letters, digits, and common punctuation into Morse code as you type.​

Spacebar prints / as a word separator, Enter starts a new line, Escape cleanly exits, and Backspace shows a indicator.​

Unsupported characters are shown as <?> so you can see when something has no mapping in the Morse dictionary.​

Requirements Python 3.7+ installed on your system.​

The third‑party keyboard package, which requires administrator/root privileges on some systems (especially Linux and macOS) to capture global key events.​

Install dependencies with:

bash pip install keyboard If pip is not in your PATH or you get a permissions error, use:​

bash python -m pip install keyboard

or on some systems
python3 -m pip install keyboard Usage Clone or download this repository and change into its directory.​

Run the script from a terminal:

bash python live_morse_typing.py Read the on‑screen help:

Type any supported character (A–Z, 0–9, and listed punctuation) to see its Morse code.​

Press Space to output / as a word separator.

Press Enter to start a new line.

Press Backspace to print as a visual indicator.

Press Esc to exit the program cleanly.

Morse Dictionary The script uses a dictionary MORSE that maps:​

Uppercase letters A–Z to standard Morse sequences (dots and dashes).

Digits 0–9 to their Morse equivalents.

Common punctuation such as . , ? ' ! / ( ) & : ; = + - _ " $ @ to standard Morse where defined.

Any character not present in this mapping results in <?> being printed so that the program does not crash on unexpected input.​

How It Works A helper function to_morse(ch: str) -> str looks up each character in the MORSE dictionary and returns an empty string if it is not supported.​

The main loop waits for key events, filters for key‑down events, and then:

Handles special keys (esc, space, enter, backspace) with custom behavior.

For single-character keys, calls to_morse and prints the resulting code or <?>.​

The loop runs until you press Esc or interrupt the program (Ctrl+C).​

Notes and Limitations On some platforms the keyboard library may require running the script with elevated privileges for global key capture to work.​

The program currently supports one‑way conversion (typed character → Morse) only; it does not decode Morse back to text.​

Layout is tuned for a terminal; IDE consoles that handle input differently may not behave as expected.​

Possible Improvements Add configuration for timing (e.g., beeps or tones for dots and dashes).​

Implement decoding from Morse to plaintext using a reverse dictionary.​

Add command‑line options for choosing input source or toggling features.
