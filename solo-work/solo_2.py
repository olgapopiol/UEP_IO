#zadanie z zajęć
def trojkat(bok_a,bok_b,bok_c,h_a):
    pole=bok_a*h_a/2
    obwod=bok_a+bok_b+bok_c
    return pole, obwod

print("Pole i obwod wynosi: ", trojkat(2,3,4,4))

