from flask import Flask, render_template, request
app = Flask(__name__)

CHARS_TO_MORSE_CODE_MAPPING = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '\'': '· − − − − ·',
    '!': '− · − · − −',
    '/': '− · · − ·',
    '(': '− · − − ·',
    ')': '− · − − · −',
    '&': '· − · · ·',
    ':': '− − − · · ·',
    ';': '− · − · − ·',
    '=': '− · · · −',
    '+': '· − · − ·',
    '-': '− · · · · −',
    '_': '· · − − · −',
    '"': '· − · · − ·',
    '$': '· · · − · · −',
    '@': '· − − · − ·',
}


# function to encode plain English text to morse code
def to_morse_code(english_plain_text):
    morse_code = ''
    for char in english_plain_text:
        # checking for space
        # to add single space after every character and double space after every word
        if char == ' ':
            morse_code += '  '
        else:
            # adding encoded morse code to the result
            morse_code += CHARS_TO_MORSE_CODE_MAPPING[char.upper()] + ' '
    return morse_code


def reverse_mapping(mapping):
    reversed = {}
    for key, value in mapping.items():
        reversed[value] = key
    return reversed


MORSE_CODE_TO_CHARS_MAPPING = reverse_mapping(CHARS_TO_MORSE_CODE_MAPPING)

def to_english_plain_text(morse_code):
    english_plain_text = ''

    current_char_morse_code = ''
    i = 0
    while i < len(morse_code):
        # checking for each character
        if morse_code[i] == ' ':
            # checking for word
            if len(current_char_morse_code) == 0 and morse_code[i + 1] == ' ':
                english_plain_text += ' '
                i += 1
            else:
                # adding decoded character to the result
                english_plain_text += MORSE_CODE_TO_CHARS_MAPPING[
                    current_char_morse_code]
                current_char_morse_code = ''
        else:
            # adding morse code char to the current character
            current_char_morse_code += morse_code[i]
        i += 1

    # adding last character to the result
    if len(current_char_morse_code) > 0:
        english_plain_text += MORSE_CODE_TO_CHARS_MAPPING[
            current_char_morse_code]

    return english_plain_text



@app.route("/", methods=['GET','POST'])
def morsecode():
    if request.method == "POST":
        data= request.form
        ff = data["text"]
        morsecode = to_morse_code(ff)
    else:
        ff = "Hi"
        morsecode = to_morse_code(ff)
    return render_template('morsecode.html', text=ff, morsecode=morsecode)


@app.route("/reverse", methods=['GET','POST'])
def reverse():
    if request.method == "POST":
        data= request.form
        ff = data["code"]
        morsecode = to_english_plain_text(ff)
    else:
        ff = ".-"
        morsecode = to_english_plain_text(ff)
    return render_template('morsecode.html', text0=morsecode, morsecode0=ff)


if __name__ == "__main__":
    app.run()
