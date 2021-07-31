# PAPO

A comical parser for a comical language.

You are free to clone this repo and use the parser as much as you want.

### Example

Here you have a small script you can use to try the papo-parser and have a good time.

```python
import papo

with open('sample_text.txt', 'r') as papo_in:
    sample_text = papo_in.read()
    papo_out = papo.load(papo_in)

print(f'----- SAMPLE TEXT -----\n\n{sample_text}\n\n-----------------------')
print(f'------ PAPO TEXT ------\n\n{papo_out}\n\n-----------------------')
```

This code is already included in [`papo_example_script.py`](./papo_example_script.py).