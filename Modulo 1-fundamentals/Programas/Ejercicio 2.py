print("Bienvenido, este programa evaluará si aprueba, según sus notas. A continuación le solicitaré algunos datos...")
nombre = input("Escriba su nombre: ")
edad = int(input("Escriba su edad: "))

#declarando el directorio del estudiante
dict_estudiante = {
  "nombre": nombre,
  "edad": edad,
  "notas": [],
  "aprobado": False,
}

#Pide y añade las notas al directorio
dict_estudiante["notas"].append(float(input("Ingrese su nota #1: ")))
dict_estudiante["notas"].append(float(input("Ingrese su nota #2: ")))
dict_estudiante["notas"].append(float(input("Ingrese su nota #3: ")))
dict_estudiante["notas"].append(float(input("Ingrese su nota #4: ")))
dict_estudiante["notas"].append(float(input("Ingrese su nota #5: ")))


nota_media = sum(dict_estudiante["notas"]) / len(dict_estudiante["notas"])

if nota_media > 3.0:
    dict_estudiante["aprobado"] = True
    print(dict_estudiante)

else:
    dict_estudiante["aprobado"] = False
    print(dict_estudiante)

    