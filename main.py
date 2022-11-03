import getopt
import sys
import morse_dict


def convert(string):
    res = ''
    for c in string:
        try:
            res += morse_dict.morse_dict[c] + ' '
        except KeyError:
            pass

    return res


def print_manpage():
    with open('manpage') as manpage:
        lines = manpage.readlines()
        for line in lines:
            print(line, end='')


def main(argv):
    _f_inputfile = False
    _f_outputfile = False

    try:
        opts, args = getopt.getopt(argv, 'f:o:', ['file', 'ofile'])
    except getopt.GetoptError:
        print_manpage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print_manpage()
        elif opt in ('-f', '--file'):
            _f_inputfile = True
            input_file = arg
        elif opt in ('-o', '--ofile'):
            _f_outputfile = True
            output_path = arg

    if _f_inputfile:
        output_file = ''
        with open(input_file) as f:
            lines = f.readlines()
            for line in lines:
                output_file += convert(line.lower())
    else:
        output_file = convert(argv[len(argv)-1].lower())

    if _f_outputfile:
        try:
            with open(output_path, 'x') as o:
                o.write(output_file)
        except FileExistsError:
            print('This file already exists! Exiting the program.')
            sys.exit(2)
    else:
        print(output_file)


if __name__ == '__main__':
    main(sys.argv[1:])
