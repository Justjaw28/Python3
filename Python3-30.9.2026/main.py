import random

cena = random.randrange(100,300)
print("Jídlo vás stojí " + str(cena) + " Kč.")
print("Kolik zaplatíte?")
client1 = int(input())
print("Zaplatily jste " + str(client1) + " Kč.")
if cena - client1 <= 0:
    print("Děkujeme za zaplacení.")
else:
    print("Musíte doplatit " + str(cena-client1) + " Kč.")
    client2 = int(input())
    print("Zaplatily jste " + str(client2) + " Kč.")
    if cena - client2 - client1 <= 0:
        print("Děkujeme za zaplacení.")
    else:
        print("Musíte doplatit " + str(cena-client2-client1) + " Kč.")
        client3 = int(input())
        print("Zaplatily jste " + str(client3) + " Kč.")
        if cena - client3 - client2 - client1 <= 0:
            print("Děkujeme za zaplacení.")
        else:
            print("Bohužel jste nezaplatili dostatek peněz. Jídlo vám nebude vydáno.")
