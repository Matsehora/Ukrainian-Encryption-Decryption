ukr_alfabet_lover = [
    'а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ','ь', 'ю', 'я'
]

numbers = list(range(1, 34))


def string_to_int(string_value: str):
    temp_value = ukr_alfabet_lover.index(string_value)
    return temp_value
    

def XOR(firs_value:int,second_value:int):
    return firs_value ^ second_value

def encryption_and_dencryption(word:str,key:str):
 # Розширюємо ключ до довжини слова
    extended_key = key * (len(word) // len(key)) + key[:len(word) % len(key)]

    return_word = ""
    for x in range(len(word)):
        temp = XOR(string_to_int(word.lower()[x]), string_to_int(extended_key.lower()[x]))
        if temp >= 33:
            temp -= 33
        return_word += ukr_alfabet_lover[temp]

    return return_word

