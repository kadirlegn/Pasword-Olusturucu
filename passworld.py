import string
from random import *
characters = string.ascii_letters + string.punctuation + string.digits
karakterSayisi = input("Karakter Sayısı Kaç Olsun ? ")

password = ""

for i in range (int(karakterSayisi)):
    password += choice (characters)

    print(password)
