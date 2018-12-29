import os

for pasta, subpastas, arquivos in os.walk('..'):
    print ('Pasta atual:', pasta)

    for subpasta in subpastas:
        print('<dir>', pasta.rstrip('/'), '/', subpasta, sep='')

    for arquivo in arquivos:
        print(pasta.rstrip('/'), '/', arquivo, sep='')

    print('')