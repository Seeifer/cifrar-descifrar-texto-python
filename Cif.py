opcion = input("¿Cifrar o Descifrar?: ").lower()   # Se solicita al usuario que elija si desea cifrar o descifrar un texto
j = 0
if opcion in ["cifrar", "cif ", "1"]:   # Si el usuario desea cifrar el texto
    clave = input("Introduzca la clave: ")
    clave_numeros = [int(x) for x in clave]
    org = input("introduzca texto a cifrar: ")
    # Se inicializan dos listas vacías para almacenar el texto cifrado
    lista = []
    listaV2 = []

    for i in org:  # Se recorre cada letra del texto a cifrar
        i = ord(i) + clave_numeros[j]  # Se convierte la letra en su valor numérico en la tabla ASCII y se le suma el valor correspondiente de la clave
        lista.append(i)
        j += 1
        if j == len(clave_numeros):
            j = 0

    for j in lista:
        j = chr(j)  # Se convierte el valor numérico cifrado en su letra correspondiente en la tabla ASCII y se agrega a la segunda lista
        listaV2.append(j)

    print("".join(listaV2))  # Se imprime el texto cifrado

elif opcion in ["descifrar", "descif ", "2", "des"]:  # Si el usuario desea descifrar el texto
    decif = input("Introduzca el texto a decifrar: ")
    clave = input("Introduzca la clave: ")
    clave_numeros = [int(x) for x in clave]
    decif_valor = []
    new_decif = []

    for i in decif:  # Se recorre cada valor numérico cifrado en el texto a descifrar
        i = ord(i) - clave_numeros[j]  # Se le resta al valor numérico cifrado el valor correspondiente de la clave y se convierte en su letra correspondiente en la tabla ASCII
        decif_valor.append(i)
        j += 1
        if j == len(clave_numeros):
            j = 0

    for j in decif_valor:
        j = chr(j)  # Se convierte el valor numérico descifrado
        new_decif.append(j)

    print("".join(new_decif))   # Se imprime el texto descifrado

else:
    print("Opcion No Valida (Escritura Erronea)")  # si el usuario introduce una opcion no valida
