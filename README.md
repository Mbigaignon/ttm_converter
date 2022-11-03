# ttm_converter

A simple Text-to-Morse converter.
Reads a string from the command line or a specified file and converts it to Morse code. By default, the programm outputs
its result to the console, unless another option is selected.

Coding conventions :
    - Uses the International Morse Code
    - Only encodes the 26 basic Latin letters regardless of case, as well as the 10 Arabic numerals
    - All others characters are skipped
    - A short mark is encoded with the character '.'
    - A long mark is encoded with the character '—'
    - A short gap is encoded with a single whitespace
    - A medium gap is encoded with a triple whitespace

Syntax:

    python main.py [OPTIONS] ARG
        Reads the argument as a string and outputs the converted Morse code.

    python main.py [OPTIONS] -f FILE
    python main.py [OPTIONS] --ifile=FILE
        Reads the provided file and outputs its content, converted to Morse code.

Options:

    '{-o|--ofile} FILE'
        The program with create a new file with the provided name and write its result into it. It WILL NOT write into
        an existing file.
