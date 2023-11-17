import sys
import runner


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Syntax: python cccbdb.py CALCULATION FORMULA [DEPTH] [DEEP_FILTERS]')
        print('Example: python cccbdb.py dipole CH4 shallow')
        print('Example: python cccbdb.py geom CH4 deep')
        print('Example: python cccbdb.py geom CH4 deep \'[{"method": "LSDA"}, {"method": "BLYP"}]\'')
        print('Example: python cccbdb.py geom CH4 deep \'[{"method": "LSDA", "basis": "6-31G"}]\'')
        exit()

    # command line args
    calculation = sys.argv[1]
    formula = sys.argv[2]
    depth = sys.argv[3] if len(sys.argv) > 3 else 'shallow'
    deep_filters = sys.argv[4] if len(sys.argv) > 4 else '[{}]'

    # run the parser
    runner.run(calculation, formula, depth, deep_filters)
