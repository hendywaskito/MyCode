#Assigment Answer for Camp1_Day2_assign2
#Script Author: Hendy Waskito
#Company: Packet Systems Indonesia

import random
pilih = 'y'
while pilih.lower() == 'y' :
    print("\n Please guess the value from 1 to 10 \n")
    angka = random.randint(1,10)
    tebak = input("Guess the number: ")
    if int(tebak) == angka:
        print("Correct !!")
    else:
        print("Wrong !!")
    pilih = input("Do you want to try again (y/n): ")
print("\n Thanks for playing this game")