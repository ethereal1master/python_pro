import random
def gen(aaa):

    waos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    pw = "".join(random.choice(waos) for i in range(aaa))
    print("La clave generada es:", pw)
    return pw
sas = input("quieres crear una contraseña?")
if sas == "si":
    vivalagrasa = int(input("Longitud clave: "))
    test= gen(vivalagrasa)
