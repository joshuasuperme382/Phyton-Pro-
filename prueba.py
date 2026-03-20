import random

caracteres_contrasena = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;':\",./<>?"

longitud = int(input("Ingrese la longitud de la contraseña: "))
contraseña = ""

for i in range(longitud):
    char = random.choice(caracteres_contrasena)
    contraseña += char

print("Contraseña generada:", contraseña)