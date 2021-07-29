import io
import sys
import re

def load(f: str or object):
    if isinstance(f, str):
        file = open(f, 'r')
    elif _is_file(f):
        file = io.TextIOWrapper(f)
    else:
        raise TypeError('Input must be an existing text readable file or a path to an existing readable file')

    text = file.read()
    papo = re.sub(r'(^|\s)([Pp]apo){0,1}(\w)', _capitalize_match, text)
    
    return papo

def _capitalize_match(m: re.Match):
    if m.group(3).istitle():
        papo = f'Papo{m.group(3).lower()}'
    elif m.group(3).isupper():
        papo = f'PAPO{m.group(3)}'
    else:
        papo = f'papo{m.group(3)}'
    return f'{m.group(1)} {papo}'

def _is_file(f):
    return isinstance(f, io.TextIOWrapper) if sys.version_info[0] == 2 else hasattr(f, 'read')