#!/usr/bin/python3
"""log parsing"""
import re


def print_stats(total_size, status_codes):
    '''Prints the accumulated statistics of the HTTP request log.
    '''
    print('File size: {:d}'.format(total_size), flush=True)
    for status_code in sorted(status_codes.keys()):
        num = status_codes.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def update_metrics(line, total_size, status_codes):
    '''Updates the total size of file and the status codes.
    Args:
        line (str): The line of input from which to retrieve the metrics.
    Returns:
        int: The new total file size.
    '''
    '''extract line of an HTTP request log.'''
    pt = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    extract_data = {
        'status_code': 0,
        'file_size': 0,
    }
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(pt[0], pt[1], pt[2], pt[3], pt[4])
    resp_match = re.fullmatch(log_fmt, line)
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        extract_data['status_code'] = status_code
        extract_data['file_size'] = file_size

    status_code = extract_data.get('status_code', '0')
    if status_code in status_codes.keys():
        status_codes[status_code] += 1
    return total_size + extract_data['file_size']


def log_parsing():
    '''Log parsing.
    '''
    line_count = 0
    total_size = 0
    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            total_size = update_metrics(
                line,
                total_size,
                status_codes,
            )
            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
    except (KeyboardInterrupt, EOFError):
        print_stats(total_size, status_codes)


if __name__ == '__main__':
    log_parsing()
