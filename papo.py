import io
import sys
import re

def load(f: str or object) -> str:
    if isinstance(f, str):
        file = open(f, 'rt')
    elif _is_file(f):
        file = f
        file.seek(0)
    else:
        raise TypeError('Input must be an existing text readable file or a path to an existing readable file')

    text = file.read()
    papo = re.sub(r'(^|\s)(((Papo|papo|PAPO){1}\w*)|(\w+))', _capitalize_match, text)

    return papo

def _capitalize_match(m: re.Match) -> str:
    if m.group(3):
        return f'{m.group(1)}{m.group(3)}'
    else:
        text = m.group(5)
        if text.istitle():
            papo = f'Papo{text.lower()}'
        elif text.isupper():
            papo = f'PAPO{text}'
        else:
            papo = f'papo{text}'
        return f'{m.group(1)}{papo}'

def _is_file(f: object) -> bool:
    return isinstance(f, io.TextIOWrapper) if sys.version_info[0] == 2 else hasattr(f, 'read') and hasattr(f, 'seek')