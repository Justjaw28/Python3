import random

cena = random.randrange(100,300)
print("Jídlo vás stojí " + str(cena) + " Kč.")
print("Kolik zaplatíte?")
client1 = int(input())
if cena >= client1:
    print("Děkujeme za zaplacení.")
else:
    print("Musíte doplatit " + str(cena) + " Kč.")
    client2 = int(input())
    if cena >= client2:
        print("Děkujeme za zaplacení.")
    else:
        print("Musíte doplatit " + str(cena) + " Kč.")
        client3 = int(input())
        if cena >= client3:
            print("Děkujeme za zaplacení.")
        else:
            print("Bohužel jste nezaplatili dostatek peněz. Jídlo vám nebude vydáno.")
