import random

print("Vítejte v naší restauraci. Co si přejete k jídlu?")
print("1. Pizza - 150 Kč, 2. Řízek - 200 Kč, 3. Salát - 100 Kč, 4. Polévka - 80 Kč, 5. Hamburger - 120 Kč")
jidlo = int(input())
if jidlo == 1:
    cena = 150
elif jidlo == 2:
    cena = 200
elif jidlo == 3:
    cena = 100
elif jidlo == 4:
    cena = 80
elif jidlo == 5:
    cena = 120
else:
    print("Neplatná volba.")
    exit()
print("Budete si pčát ještě něco k jídlu? (ano/ne)")
dalsi_jidlo = input()
if dalsi_jidlo == "ano":
    print("Co si přejete k jídlu?")
    print("1. Pizza - 150 Kč, 2. Řízek - 200 Kč, 3. Salát - 100 Kč, 4. Polévka - 80 Kč, 5. Hamburger - 120 Kč")
    jidlo2 = int(input())
    if jidlo2 == 1:
        cena += 150
    elif jidlo2 == 2:
        cena += 200
    elif jidlo2 == 3:
        cena += 100
    elif jidlo2 == 4:
        cena += 80
    elif jidlo2 == 5:
        cena += 120
    else:
        print("Neplatná volba.")
        exit()
print("Budete si přát nápoj k jídlu? (ano/ne)")
napoj = input()
if napoj == "ano":
    print("Jaký nápoj si přejete?")
    print("1. Káva - 30 Kč, 2. Čaj - 25 Kč, 3. Voda - 20 Kč, 4. Limonáda - 35 Kč, 5. Džus - 40 Kč")
    napoj_volba = int(input())
    if napoj_volba == 1:
        cena += 30
    elif napoj_volba == 2:
        cena += 25
    elif napoj_volba == 3:
        cena += 20
    elif napoj_volba == 4:
        cena += 35
    elif napoj_volba == 5:
        cena += 40
    else:
        print("Neplatná volba.")
        exit()
print(f"Vaše celková cena je {cena} Kč.")
print("Kolik zaplatíte?")
client1 = int(input())
print(f"Zaplatily jste {client1} Kč.")
if cena - client1 <= 0:
    print("Děkujeme za zaplacení.")
    if cena - client1 < 0:
        print(f"Vaše vrácená částka je {client1-cena} Kč.")
else:
    print(f"Musíte doplatit {cena-client1} Kč.")
    client2 = int(input())
    print(f"Zaplatily jste {client2} Kč.")
    if cena - client2 - client1 <= 0:
        print("Děkujeme za zaplacení.")
        if cena - client2 - client1 < 0:
            print(f"Vaše vrácená částka je {client2+client1-cena} Kč.")
    else:
        print(f"Musíte doplatit {cena-client2-client1} Kč.")
        client3 = int(input())
        print(f"Zaplatily jste {client3} Kč.")
        if cena - client3 - client2 - client1 <= 0:
            print("Děkujeme za zaplacení.")
            if cena - client3 - client2 - client1 < 0:
                print(f"Vaše vrácená částka je {client3+client2+client1-cena} Kč.")
        else:
            print("Bohužel jste nezaplatili dostatek peněz. Jídlo vám nebude vydáno.")