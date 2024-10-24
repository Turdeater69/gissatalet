import random
#Random tal mellan 1-10
attempt=5
correct=random.randint(1,10)
print("Gissa talet, du har fem försök att gissa det dolda talet mellan 1-10.")
for i in range(attempt):
    guess=int(input("Ange talet:"))
    if guess==correct:
        print("Grattis du har rätt")
        break
    if guess>correct:
        print("För högt")
    if guess<correct:
        print("För lågt")
if guess!=correct:
    print("Du gissade fel för många gånger, talet var ", correct)
