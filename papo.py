import io
import sys
import re


def _is_file(f: object) -> bool:
    return isinstance(f, io.TextIOWrapper) if sys.version_info[0] == 2 else hasattr(f, 'read') and hasattr(f, 'seek')

def _ignore_loader() -> tuple:
    try:
        ignore = []
        with open('.papoignore') as papoignore:
            for line in papoignore.readlines():
                treated_line = line.split('#', 1)[0].strip('\n').strip()
                if treated_line:
                    ignore.append(treated_line)
        return (ignore)

    except FileNotFoundError:
        return ()

PAPOIGNORE = _ignore_loader()

def _capitalize_match(m: re.Match) -> str:
    if m.group(2).lower() in PAPOIGNORE:
        return f'{m.group(1)}{m.group(2)}'

    elif m.group(3):
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

def load(f: str or object) -> str:
    if isinstance(f, str):
        file = open(f, 'rt')
    elif _is_file(f):
        file = f
        file.seek(0)
    else:
        raise TypeError('Input must be an existing text papo readable file or a path to an existing papo readable file')

    text = file.read()
    papo = re.sub(r'(^|\s)(((Papo|papo|PAPO){1}\w*)|(\w+))', _capitalize_match, text)

    return papo