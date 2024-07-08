import tkinter as tk
from lb_1_5 import encryption_and_dencryption as encryption_and_dencryption_lab_5
from lb_1_4 import encryption as encryption_lab_4
from lb_1_4 import dencryption as dencryption_lab_4
from lb_1_3 import encryption as encryption_lab_3
from lb_1_3 import dencryption as dencryption_lab_3
from lb_1_2 import encryption as encryption_lab_2
from lb_1_2 import dencryption as dencryption_lab_2
from lb_1_1 import encryption as encryption_lab_1
from lb_1_1 import dencryption as dencryption_lab_1


def return_int_value(value:str):
        return int(value)

def check_the_number(value:int):
        if 0 <= value <= 31:
            return True
        return False

def inser_word_entry_4(word:str, entry):
        entry.delete(0, tk.END)
        entry.insert(0,word)

def XOR_cipher():
    root_lab_5 = tk.Tk()
    root_lab_5.title("Ukrainian Encryption/Decryption")

    lable_1 = tk.Label(root_lab_5,text='Enter the word to encrypt/decrypt')
    lable_2 = tk.Label(root_lab_5,text='Enter the encryption/decryption key')
    lable_3 = tk.Label(root_lab_5,text='Obtained result')

    entry_1 = tk.Entry(root_lab_5, width=30)
    entry_2 = tk.Entry(root_lab_5, width=30)
    entry_3 = tk.Entry(root_lab_5, width=30)

    def check_for_enty_fill():
        if len(entry_1.get()) != 0 and len(entry_2.get()) != 0:
            return True
        return False
    
    def button_press_for_lab_5():
        if check_for_enty_fill():
            temp = encryption_and_dencryption_lab_5(entry_1.get(),entry_2.get())
            print(type(entry_1.get()))
            entry_3.delete(0, tk.END)
            entry_3.insert(0,temp)

    button_for_start = tk.Button(root_lab_5, text="Encryption/Decryption",command=button_press_for_lab_5)

    lable_1.grid(row=0, column=0, padx=20, pady=10) 
    lable_2.grid(row=1, column=0, padx=20, pady=10) 
    lable_3.grid(row=2, column=0, padx=20, pady=10) 

    entry_1.grid(row=0, column=1, padx=20, pady=10)
    entry_2.grid(row=1, column=1, padx=20, pady=10) 
    entry_3.grid(row=2, column=1, padx=20, pady=10)

    button_for_start.grid(row=3, column=0, padx=20, pady=10)

    root_lab_5.mainloop()

def transposition_cipher():
    root_lab_4 = tk.Tk()
    root_lab_4.title("Transposition Cipher")

    def check_for_enty_fill():
        if len(entry_1.get()) != 0 and len(entry_2.get()) != 0 and len(entry_3.get()) != 0:
            return True
        return False
    
    def return_int_lists():
        if check_for_enty_fill():
            temp_1 = entry_2.get()
            temp_2 = entry_3.get()

            temp_1 = temp_1.split(' ')
            temp_2 = temp_2.split(' ')

            if len(temp_2) == 4 and len(temp_1) == 4:
                return_list_1 = [int(x) for x in temp_1]
                return_list_2 = [int(x) for x in temp_2]

                return return_list_1,return_list_2
            
        return False
    
    def just_16_long():
        if len(entry_1.get()) == 16:
            return True
        return False

    def inser_word_entry_4(word):
        entry_4.delete(0, tk.END)
        entry_4.insert(0,word)


    def button_dencryption():
        if check_for_enty_fill() and just_16_long():
            row_list, column_list = return_int_lists()
            word = entry_1.get()
            temp = dencryption_lab_4(word,row_list,column_list)
            inser_word_entry_4(temp)

    def button_encryption():
        if check_for_enty_fill() and just_16_long():
            row_list, column_list = return_int_lists()
            word = entry_1.get()
            temp = encryption_lab_4(word,row_list,column_list)
            inser_word_entry_4(temp)


    lable_1 = tk.Label(root_lab_4,text='Enter the word to encrypt/decrypt')
    lable_2 = tk.Label(root_lab_4,text='Enter 4 numeric values ​​using a space (line)')
    lable_3 = tk.Label(root_lab_4,text='Enter 4 numeric values ​​using a space (column)')
    lable_4 = tk.Label(root_lab_4,text='Obtained result')

    entry_1 = tk.Entry(root_lab_4, width=30)
    entry_2 = tk.Entry(root_lab_4, width=30)
    entry_3 = tk.Entry(root_lab_4, width=30)
    entry_4 = tk.Entry(root_lab_4, width=30)

    button_for_encryption = tk.Button(root_lab_4, text="Encrypt",command = button_encryption)
    button_for_dencryption = tk.Button(root_lab_4, text="Decipher",command = button_dencryption)

    button_for_encryption.grid(row=4, column=0, padx=20, pady=10)
    button_for_dencryption.grid(row=4, column=1, padx=20, pady=10)

    lable_1.grid(row=0, column=0, padx=20, pady=10) 
    lable_2.grid(row=1, column=0, padx=20, pady=10) 
    lable_3.grid(row=2, column=0, padx=20, pady=10) 
    lable_4.grid(row=3, column=0, padx=20, pady=10)

    entry_1.grid(row=0, column=1, padx=20, pady=10)
    entry_2.grid(row=1, column=1, padx=20, pady=10) 
    entry_3.grid(row=2, column=1, padx=20, pady=10)
    entry_4.grid(row=3, column=1, padx=20, pady=10)

    root_lab_4.mainloop()
  
def caesars_cipher_1_shift():
    root_lab_3 = tk.Tk()
    root_lab_3.title("CaCaesar cipher 2 shift")


    def check_for_enty_fill():
        if len(entry_1.get()) != 0 and len(entry_2.get()) != 0 and len(entry_3.get()) != 0:
            return True
        return False
    
    def full_cehck():
        if check_for_enty_fill() and check_the_number(return_int_value(entry_2.get())) and check_the_number(return_int_value(entry_3.get())):
            return True
        return False

    def inser_word_entry_4(word):
        entry_4.delete(0, tk.END)
        entry_4.insert(0,word)

    def button_encryption():
        if full_cehck():
            temp = encryption_lab_3(entry_1.get(),return_int_value(entry_2.get()),return_int_value(entry_3.get()))
            inser_word_entry_4(temp)

    def button_dencryption():
        if full_cehck():
            temp = dencryption_lab_3(entry_1.get(),return_int_value(entry_2.get()),return_int_value(entry_3.get()))
            inser_word_entry_4(temp)

    lable_1 = tk.Label(root_lab_3,text='Enter the word to encrypt/decrypt')
    lable_2 = tk.Label(root_lab_3,text='Enter the numeric a')
    lable_3 = tk.Label(root_lab_3,text='Enter the numeric b')
    lable_4 = tk.Label(root_lab_3,text='Obtained result')

    entry_1 = tk.Entry(root_lab_3, width=30)
    entry_2 = tk.Entry(root_lab_3, width=30)
    entry_3 = tk.Entry(root_lab_3, width=30)
    entry_4 = tk.Entry(root_lab_3, width=30)

    button_for_encryption = tk.Button(root_lab_3, text="Encrypt",command = button_encryption)
    button_for_dencryption = tk.Button(root_lab_3, text="Decipher",command = button_dencryption)

    button_for_encryption.grid(row=4, column=0, padx=20, pady=10)
    button_for_dencryption.grid(row=4, column=1, padx=20, pady=10)

    lable_1.grid(row=0, column=0, padx=20, pady=10) 
    lable_2.grid(row=1, column=0, padx=20, pady=10) 
    lable_3.grid(row=2, column=0, padx=20, pady=10) 
    lable_4.grid(row=3, column=0, padx=20, pady=10)

    entry_1.grid(row=0, column=1, padx=20, pady=10)
    entry_2.grid(row=1, column=1, padx=20, pady=10) 
    entry_3.grid(row=2, column=1, padx=20, pady=10)
    entry_4.grid(row=3, column=1, padx=20, pady=10)

    root_lab_3.mainloop()

def vigenère_cipher():
    root_lab_2 = tk.Tk()
    root_lab_2.title("Vigenère cipher")

    def check_for_enty_fill():
        if len(entry_1.get()) != 0 and len(entry_2.get()) != 0 and len(entry_3.get()) != 0:
            return True
        return False
    
    def full_cehck():
        if check_for_enty_fill() and check_the_number(return_int_value(entry_2.get())) and check_the_number(return_int_value(entry_3.get())):
            return True
        return False

    def button_encryption():
        if full_cehck():
            temp = encryption_lab_2(entry_1.get(),return_int_value(entry_2.get()),return_int_value(entry_3.get()))
            inser_word_entry_4(temp,entry_4)

    def button_dencryption():
        if full_cehck():
            temp = dencryption_lab_2(entry_1.get(),return_int_value(entry_2.get()),return_int_value(entry_3.get()))
            inser_word_entry_4(temp,entry_4)


    lable_1 = tk.Label(root_lab_2,text='Enter the word to encrypt/decrypt')
    lable_2 = tk.Label(root_lab_2,text='Enter the numeric a')
    lable_3 = tk.Label(root_lab_2,text='Enter the numeric b')
    lable_4 = tk.Label(root_lab_2,text='Отриманий результат')

    entry_1 = tk.Entry(root_lab_2, width=30)
    entry_2 = tk.Entry(root_lab_2, width=30)
    entry_3 = tk.Entry(root_lab_2, width=30)
    entry_4 = tk.Entry(root_lab_2, width=30)

    button_for_encryption = tk.Button(root_lab_2, text="Зашифрувати",command = button_encryption)
    button_for_dencryption = tk.Button(root_lab_2, text="Розшифрувати",command = button_dencryption)

    button_for_encryption.grid(row=4, column=0, padx=20, pady=10)
    button_for_dencryption.grid(row=4, column=1, padx=20, pady=10)

    lable_1.grid(row=0, column=0, padx=20, pady=10) 
    lable_2.grid(row=1, column=0, padx=20, pady=10) 
    lable_3.grid(row=2, column=0, padx=20, pady=10) 
    lable_4.grid(row=3, column=0, padx=20, pady=10)

    entry_1.grid(row=0, column=1, padx=20, pady=10)
    entry_2.grid(row=1, column=1, padx=20, pady=10) 
    entry_3.grid(row=2, column=1, padx=20, pady=10)
    entry_4.grid(row=3, column=1, padx=20, pady=10)

def caesars_cipher_1_shift():
    root_lab_1 = tk.Tk()
    root_lab_1.title("Caesar's cipher 1 shift")

    def check_for_enty_fill():
            if len(entry_1.get()) != 0 and len(entry_2.get()) != 0:
                return True
            return False

    def button_encryption():
        if check_for_enty_fill():
            temp = encryption_lab_1(entry_1.get(),int(entry_2.get()))
            inser_word_entry_4(temp,entry_3)

    def button_dencryption():
        if check_for_enty_fill():
            temp = dencryption_lab_1(entry_1.get(),int(entry_2.get()))
            inser_word_entry_4(temp,entry_3)


    lable_1 = tk.Label(root_lab_1,text='Введіть слово для шифрування/розшифрування')
    lable_2 = tk.Label(root_lab_1,text='Введіть ключ k')
    lable_3 = tk.Label(root_lab_1,text='Obtained result')

    entry_1 = tk.Entry(root_lab_1, width=30)
    entry_2 = tk.Entry(root_lab_1, width=30)
    entry_3 = tk.Entry(root_lab_1, width=30)

    lable_1.grid(row=0, column=0, padx=20, pady=10) 
    lable_2.grid(row=1, column=0, padx=20, pady=10) 
    lable_3.grid(row=2, column=0, padx=20, pady=10) 

    entry_1.grid(row=0, column=1, padx=20, pady=10)
    entry_2.grid(row=1, column=1, padx=20, pady=10) 
    entry_3.grid(row=2, column=1, padx=20, pady=10)

    button_for_encryption = tk.Button(root_lab_1, text="Encrypt",command = button_encryption)
    button_for_dencryption = tk.Button(root_lab_1, text="Decipher",command = button_dencryption)

    button_for_encryption.grid(row=4, column=0, padx=20, pady=10)
    button_for_dencryption.grid(row=4, column=1, padx=20, pady=10)

    root_lab_1.mainloop()


# Create the main window
root = tk.Tk()
root.title("Text Window Example")

# Create an entry field and a button
button_1 = tk.Button(root, text="Caesar's cipher 1 shift",command = caesars_cipher_1_shift)
button_2 = tk.Button(root, text="Vigenère cipher",command = vigenère_cipher)
button_3 = tk.Button(root, text="Caesar's cipher 2 shift",command = caesars_cipher_1_shift)
button_4 = tk.Button(root, text="Transposition Cipher",command = transposition_cipher)
button_5 = tk.Button(root, text="XOR cipher",command = XOR_cipher)

# Create a Text widget


# Pack the entry, button, and text widget into the window
button_1.pack(pady=5)
button_2.pack(pady=5)
button_3.pack(pady=5)
button_4.pack(pady=5)
button_5.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()