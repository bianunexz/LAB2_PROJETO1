import random 
def cumprimento(texto):
    print(f"olá,  {texto}") 

cumprimento(" bianca nunes de mendonça ")

def aleatorio():
    numero_1=random.randint(0,100)
    numero_2=random.randint(0,100)
    numero_3=random.randint(0,100)
    numero_4=random.randint(0,100)
    numero_5=random.randint(0,100)
    numero_6=random.randint(0,100)
    numero_7=random.randint(0,100)
    media=(numero_1+numero_2+numero_3+numero_4+numero_5+numero_6+numero_7)/7
    return media

m = aleatorio()
print(m)