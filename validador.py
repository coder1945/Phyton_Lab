import usuario
import password

respuesta=False
while respuesta==False:
        nombre=input("Ingrese usuario: ")
        if usuario.nickname(nombre) == True:
            print("Usuario creado!")
            respuesta=True

while respuesta==True:
    clave=input("Ingrese clave: ")
    if password.clave(clave)==True:
        print("Clave creada!")
        respuesta=False
