import os


def file(file, result, codes):
    # remove blank lines from code
    clean_codes = os.linesep.join([s for s in codes.splitlines() if s.strip()])

    # write code to file
    file.write(result['method'] + '\n')
    if 'basis' in result:
        file.write(result['basis'] + '\n')
    file.write(result['value'] + '\n')
    file.write(clean_codes + '\n')
    file.write('-------------------------------------------\n')
    file.flush()


def file_shallow(file, result):
    # write code to file

    if 'basis' in result:
        file.write("%s / %s : %s \n" % (result['method'], result['basis'], result['value']))
    else:
        file.write("%s : %s \n" % (result['method'], result['value']))
    file.flush()


def console(result, failed=False):
    result.pop('url', None)
    if failed:
        print('failed: ' + str(result))
    else:
        print(str(result))
