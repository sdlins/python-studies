import re, pyperclip

texto = pyperclip.paste()

regex = re.compile(r'''
    (
    \(?0?\d{3}\)?-\d{3}-\d{4}                                           # telefone
    |
    [a-zA-Z_\-.+]{2,}@[a-zA-Z_\-]{2,}\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?    # email
    )
''', re.VERBOSE)

resultado = regex.findall(texto)
print(resultado[0][0])

