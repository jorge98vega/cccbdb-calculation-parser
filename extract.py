from table_parser import HTMLTableParser


def simple(list):
    results = []
    p = HTMLTableParser()
    p.feed(str(list))
    for row in p.tables[0]:
        detail = {
            'method': row[0][0],
            'value': row[1][0],
            'url': 'https://cccbdb.nist.gov/' + row[1][1] if len(row[1]) > 1 else ''
        }
        results.append(detail)
    return results


def complex(list):
    results = []
    p = HTMLTableParser()
    p.feed(str(list))
    headers = p.tables[0][0]
    # remove first 2 blank columns from header row
    del headers[0]
    del headers[0]
    for row in p.tables[0]:
        # only lines with a level
        if len(row[0]) > 0:
            method = row[0][0]
            for index, value in enumerate(row):
                # only bond that have content
                if len(value) == 2:
                    detail = {
                        'method': method,
                        'basis': headers[index-1][0],
                        'value': value[0],
                        'url': 'https://cccbdb.nist.gov/' + value[1]
                    }
                    results.append(detail)
    return results


def deep(list):
    results = []
    p = HTMLTableParser()
    p.feed(str(list))
    headers = p.tables[0][0]
    for row in p.tables[0][1:]:
        detail = {
            key[0]: value[0] for (key, value) in zip(headers, row)
        }
        results.append(detail)
    return results
