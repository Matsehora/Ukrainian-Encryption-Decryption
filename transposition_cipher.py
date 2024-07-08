#word = input("Введіть слово або черення яке буде містити 16 літер")

def procesing_word(word:str):
    if len(word) == 16:
        return word
    elif ' ' in word and len(word) == 17:
        return word.replace(' ','')
    else:
        return word[:16]

#first_four = input("Введіть 4 числових значення через пробіл")

def str_to_int_for_four(str_of_ints: str):
    return_list = []
    for x in str_of_ints.split(' '):
        return_list.append(int(x))

    return return_list

def dencryption(word:str,int_list_rows: list,int_list_collums: list):
    list_of_val_collums = [
    [0, 4, 8, 12],
    [1, 5, 9, 13],
    [2, 6, 10, 14],
    [3, 7, 11, 15]
    ]
    temp_str_collum = ''

    result = list(word)

    '''for x in int_list_collums:
        for y in list_of_val_collums[x-1]:
            temp_str_collum += word[y]'''
    
    n = len(int_list_collums)
    for i in range(n):
        for j in range(0, n-i-1):
            if int_list_collums[j] > int_list_collums[j+1]:
                int_list_collums[j], int_list_collums[j+1] = int_list_collums[j+1], int_list_collums[j]
                for y in list_of_val_collums[int_list_collums[j]-1]:
                    h = list_of_val_collums[int_list_collums[j+1]-1]
                    result[y], result[h[list_of_val_collums[int_list_collums[j]-1].index(y)]] = result[h[list_of_val_collums[int_list_collums[j]-1].index(y)]], result[y]


    temp_str_collum = ''.join(result)
    print('temp = ',temp_str_collum)
    list_of_val_rows = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15]
    ]

    result_rows = list(temp_str_collum)
    
    

    '''for x in int_list_rows:
        for y in list_of_val_rows[x-1]:
            return_string += temp_str_collum[y]'''
    for i in range(n):
        for j in range(0, n-i-1):
            if int_list_rows[j] > int_list_rows[j+1]:
                int_list_rows[j], int_list_rows[j+1] = int_list_rows[j+1], int_list_rows[j]
                for y in list_of_val_rows[int_list_rows[j]-1]:
                    h = list_of_val_rows[int_list_rows[j+1]-1]
                    result_rows[y], result_rows[h[list_of_val_rows[int_list_rows[j]-1].index(y)]] = result_rows[h[list_of_val_rows[int_list_rows[j]-1].index(y)]], result_rows[y]
    
    return_string = ''.join(result_rows)
    
    return return_string


def encryption(word:str,int_list_rows: list,int_list_collums: list):
    list_of_val_rows = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15]
    ]
    temp_str_rows = ''

    for x in int_list_rows:
        for y in list_of_val_rows[x-1]:
            temp_str_rows += word[y]

    list_of_val_collums = [
    [0, 4, 8, 12],
    [1, 5, 9, 13],
    [2, 6, 10, 14],
    [3, 7, 11, 15]
    ]
    temp_colums = list(temp_str_rows) 

    n = len(int_list_collums)
    for i in range(n):
        for j in range(0, n-i-1):
            if int_list_collums[j] > int_list_collums[j+1]:
                int_list_collums[j], int_list_collums[j+1] = int_list_collums[j+1], int_list_collums[j]
                for y in list_of_val_collums[int_list_collums[j]-1]:
                    h = list_of_val_collums[int_list_collums[j+1]-1]
                    temp_colums[y], temp_colums[h[list_of_val_collums[int_list_collums[j]-1].index(y)]] = temp_colums[h[list_of_val_collums[int_list_collums[j]-1].index(y)]], temp_colums[y]

    return_string = ''.join(temp_colums)
    return return_string

