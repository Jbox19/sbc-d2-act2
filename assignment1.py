from random import randint

humpyang = input("Choose fold or unfold: ")
print("player picks", humpyang)

c1 = randint(1,2)
c2 = randint(1,2)

if c1 == 1:
    print("c1 picks fold")
else:
    print("c1 picks unfold")

if c2 == 1:
    print("c2 picks fold")
else:
    print("c2 picks unfold")

if humpyang == "fold" and c1 == 2 and c2 == 2:
    print("Player win")
elif humpyang == "fold" and c1 == 2 and c2 == 1:
    print("c1 win")
elif humpyang == "fold" and c1 == 1 and c2 == 2:
    print("c2 win")
elif humpyang == "unfold" and c1 == 1 and c2 == 1:
    print("Player win")
elif humpyang == "unfold" and c1 == 1 and c2 == 2:
    print("c1 win")
elif humpyang == "unfold" and c1 == 2 and c2 == 1:
    print("c2 win")
else:
    print("draw")