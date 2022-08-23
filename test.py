from prettytable import PrettyTable
import os
nume = input("Numele de familie: ").capitalize()
os.system('cls')
prenume = input("Prenumele: ").capitalize()
varsta = int(input("Varsta: "))
adresa = input("Adresa: ").capitalize()
tabel = PrettyTable()
tabel.add_column("Nume familie", [nume])
tabel.add_column("Prenume", [prenume])
tabel.add_column("Varsta", [varsta])
tabel.add_column("Adresa", [adresa])

tabel.align = "c"
print(tabel)