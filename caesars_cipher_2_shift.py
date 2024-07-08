ukr_alfabet = [
    'А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'Є', 'Ж', 'З','И', 'І', 'Ї', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю', 'Я'
]

ukr_alfabet_lover = [
    'а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я'
]


def encryption(word: str,a: int,b: int):
    output = ''
    for x in word:
        lower = False
        if x in ukr_alfabet_lover:
            lower = True
            temp = ukr_alfabet_lover.index(x)
        else:
            temp = ukr_alfabet.index(x)
        temp += a + b

        if temp >= 33:
            temp -= 33

        if lower:
            output += ukr_alfabet_lover[temp]
        else:
            output += ukr_alfabet[temp]

    return output

def dencryption(word: str,a: int,b: int):
    output = ''
    for x in word:
        lower = False
        if x in ukr_alfabet_lover:
            lower = True
            temp = ukr_alfabet_lover.index(x)
        else:
            temp = ukr_alfabet.index(x)
        temp = (temp - a) - b

        if temp < 0:
            temp += 33

        if lower:
            output += ukr_alfabet_lover[temp]
        else:
            output += ukr_alfabet[temp]

    return output
