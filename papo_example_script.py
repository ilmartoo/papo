import papo

with open('sample_text.txt', 'r') as papo_in:
    sample_text = papo_in.read()
    papo_out = papo.load(papo_in)

print(f'----- SAMPLE TEXT -----\n\n{sample_text}\n\n-----------------------')
print(f'------ PAPO TEXT ------\n\n{papo_out}\n\n-----------------------')