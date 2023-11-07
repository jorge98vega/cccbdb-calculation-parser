import os
import requests
import extract
import writer
import constant
import sys
from bs4 import BeautifulSoup
import pandas as pd


def read(calculation, formula, directory='.'):
    filename = directory + '/' + formula + '.' + calculation
    if not os.path.exists(filename + '.html'):
        sys.exit('File ' + filename + '.html does not exist.')

    try:
        print('**** Extracting data')

        # find tables
        with open(filename + '.html') as fp:
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
    except Exception as e:
        print(e)
        print('**** Failed')
        sys.exit()

    # create file
    results = p_results + s_results + e_results
    df = pd.DataFrame(results, columns=['method', 'basis', 'value'])
    df.to_csv(filename + '.csv', index=False)
    print('**** Done')
