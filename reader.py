import os
import requests
import extract
import writer
import constant
import sys
from bs4 import BeautifulSoup


def read(calculation, formula, directory='.'):
    filename = directory + '/' + formula + '.' + calculation + '.html'
    if not os.path.exists(filename):
        sys.exit('File ' + filename + ' does not exist.')

    try:
        print('**** Extracting data')

        # find tables
        with open(filename) as fp:
            soup = BeautifulSoup(fp, 'html.parser')
        predefined = soup.find('table', attrs={'id': 'table1'})
        standard = soup.find('table', attrs={'id': 'table2'})
        effective = soup.find('table', attrs={'id': 'table3'})

        # extract data (including links to codes)
        p_results = extract.simple(predefined)
        s_results = extract.complex(standard)
        e_results = extract.complex(effective)
    except KeyboardInterrupt:
        sys.exit()
    except:
        print('**** Failed')
        sys.exit()

    # create file
    file = open(os.path.join(os.getcwd(), directory + '/' + formula + '.' + calculation + '.txt'), 'w')

    for result in (p_results + s_results + e_results):
        writer.file_shallow(file, result)
        writer.console(result)
    file.close()
