import sys
import reader


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Syntax: python cccbdb2.py CALCULATION FORMULA [DIRECTORY]')
        print('Example: python cccbdb2.py dipole CH4 tests')
        exit()

    # command line args
    calculation = sys.argv[1]
    formula = sys.argv[2]
    directory = sys.argv[3] if len(sys.argv) > 3 else '.'

    # run the parser
    reader.read(calculation, formula, directory)
