import re

foneregex = re.compile(r'(\d\d) (\d\d\d\d\d-\d\d\d\d)')
mo = foneregex.search('Meu numero e 61 98149-4148.')
area, fone = mo.groups()

print('Telefone encontrado: ' + area + ' ' + fone)
print(area.rjust(20) + fone.rjust(40))