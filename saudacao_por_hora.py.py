entrada = input('Digite que horas são agora: ')

try:
    hora = float(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia!')

    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    
    else:
        print('Boa noite!')

except:
    print('Digite apenas a hora')