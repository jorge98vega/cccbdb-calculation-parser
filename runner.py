import os
import requests
import extract
import writer
import constant
import sys
from bs4 import BeautifulSoup
import pandas as pd
import json


def run(calculation, formula, depth='shallow'):
    data = {
        'formula': formula,
        'submit1': 'Submit'
    }

    url1 = 'https://cccbdb.nist.gov/%s1x.asp' % calculation
    url2 = 'https://cccbdb.nist.gov/%s2x.asp' % calculation

    while True:
        try:
            print('**** Posting formula')

            # request initial url
            session = requests.Session()
            res = session.post(constant.URLS['form'], data=data, headers=constant.headers(url1), allow_redirects=False)

            print('**** Fetching data')

            # follow the redirect
            if res.status_code == 302:
                res2 = session.get(url2)

            print('**** Extracting data')

            # find tables
            soup = BeautifulSoup(res2.content, 'html.parser')
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
            #print(e)
            print('**** Failed, retrying...')
            continue
        break

    # create file
    filename = formula + '.' + calculation

    results = p_results + s_results + e_results
    df = pd.DataFrame(results, columns=['method', 'basis', 'value'])
    df.to_csv(filename + '.shallow.csv', index=False)

    # for each link in data
    if depth == 'deep':
        print('**** Fetching deep data')

        # create file
        file = open(filename + '.deep.json', 'w', encoding='utf-8')

        for result in results:
            while True:
                try:
                    # pull codes
                    res3 = session.get(result['url'])

                    soup = BeautifulSoup(res3.content, 'html.parser')
                    deep = soup.find_all('table', limit=2)[1]

                    d_results = extract.deep(deep)

                    result['deep'] = d_results
                    json.dump(result, file, ensure_ascii=False, indent=4)
                except KeyboardInterrupt:
                    sys.exit()
                except Exception as e:
                    #print(e)
                    print('**** Failed, retrying...')
                    continue
                break
        file.close()

    print('**** Done')
