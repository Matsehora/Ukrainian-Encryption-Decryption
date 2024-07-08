ukr_alfabet = [
    'А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'Є', 'Ж', 'З','И', 'І', 'Ї', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю', 'Я', ' ',',','.'
]

ukr_alfabet_lover = [
    'а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з',
    'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
    'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ',
    'ь', 'ю', 'я', ' ',',','.'
]


def encryption(word,k):
    out_put = ''
    
    for x in word:
        lover_case = False
        if x in ukr_alfabet:
            temp = ukr_alfabet.index(x) + k
        else:
            lover_case = True
            temp = ukr_alfabet_lover.index(x) + k
        if temp >= 36:
            temp -= 36
        
        if lover_case:
            out_put += ukr_alfabet_lover[temp]
        else:
            out_put += ukr_alfabet[temp]

    return out_put

def dencryption(word,k):
    out_put = ''
    
    for x in word:
        lover_case = False
        if x in ukr_alfabet:
            temp = ukr_alfabet.index(x) - k
        else:
            lover_case = True
            temp = ukr_alfabet_lover.index(x) - k
        if temp < 0:
            temp += 36
        
        if lover_case:
            out_put += ukr_alfabet_lover[temp]
        else:
            out_put += ukr_alfabet[temp]

    return out_put

