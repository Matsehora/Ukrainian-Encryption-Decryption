ukr_alfabet = [
    'А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'Є', 'Ж', 'З','И', 'І', 'Ї', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю', 'Я'
]

ukr_alfabet_lover = [
    'а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я'
]

#k = [int(input('a: ')),int(input('b: '))]
#word = input("word: ")

def index_start(k: list):
    return_list = [k[1]]
    for x in range(31):
        return_list.append(numb(return_list[-1],k[0]))

    return return_list

def numb(num: int,plus: int):
    temp = num + plus
    if temp >= 33:
        return temp-32
    return temp


def encryption(word:str,a:int ,b: int):
    yap = [a,b]
    encryption_list = index_start(yap)
    ouput = ''
    for x in word:
        if x in ukr_alfabet:
            temp = ukr_alfabet.index(x)
            temp = encryption_list[temp]
            ouput += ukr_alfabet[temp]
        else:
            temp = ukr_alfabet_lover.index(x)
            #print(temp) 
            temp = encryption_list[temp]
            #print(temp) 
            ouput += ukr_alfabet_lover[temp]

    return ouput

def dencryption(word:str,a:int ,b: int):
    yap = [a,b]
    encryption_list = index_start(yap)
    ouput = ''
    for x in word:
        if x in ukr_alfabet:
            temp = ukr_alfabet.index(x)
            temp = encryption_list.index(temp)
            ouput += ukr_alfabet[temp]
        else:
            temp = ukr_alfabet_lover.index(x)
            #print(temp )
            temp = encryption_list.index(temp)
            #print(temp) 
            ouput += ukr_alfabet_lover[temp]

    return ouput
        

#crept_decript = input('Введіть \'зашифрувати\' чи \'розшифрувати\'?: ')
'''
print(index_start(k))
print('inpunt_vord')
if crept_decript == "зашифрувати":
    print(encryption(word,index_start(k)))
elif crept_decript == "розшифрувати":
    print(dencryption(word,index_start(k)))
'''