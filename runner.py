import os
import requests
import extract
import writer
import constant
import sys
from bs4 import BeautifulSoup
import pandas as pd
import json


def run(calculation, formula, depth='shallow', deep_filters='[{}]'):
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
        deep_file = open(filename + '.deep.json', 'w', encoding='utf-8')
        dic_list = []

        deep_filters = json.loads(deep_filters)
        for deep_filter in deep_filters:
            partial_results = [{key: result[key] for key in result if key in deep_filter} for result in results]
            filtered_results = [result for result, partial_result in zip(results, partial_results) if partial_result == deep_filter]
            for result in filtered_results:
                while True:
                    try:
                        # pull codes
                        res3 = session.get(result['url'])
                        
                        if calculation in ['dipole']:
                            # dipole calculation
                            soup = BeautifulSoup(res3.content, 'html.parser')
                            deep_table = soup.find_all('table', limit=2)[1]
                            deep_results = extract.deep(deep_table)
                        else:
                            # calculations with 'carttabdumpx.asp' or 'tabdumpx.asp' actions
                            res4 = session.post(constant.URLS['dump'])
                            # try alternate dump url
                            if res4.status_code == 500:
                                res4 = session.post(constant.URLS['dump2'])

                            soup = BeautifulSoup(res4.content, 'html.parser')
                            codes = soup.find('textarea').text
                            clean_codes = os.linesep.join([s for s in codes.splitlines() if s.strip()])
                            deep_results = clean_codes

                        dic = {key: result[key] for key in result if key != 'url'}
                        dic['deep'] = deep_results
                        dic_list.append(dic)
                    except KeyboardInterrupt:
                        sys.exit()
                    except Exception as e:
                        #print(e)
                        print('**** Failed, retrying...')
                        continue
                    break
        json.dump(dic_list, deep_file, ensure_ascii=False, indent=4)
        deep_file.close()

    print('**** Done')
