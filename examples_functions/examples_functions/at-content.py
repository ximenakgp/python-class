def get_at_content(dna, num): #Le paso el numero de digitos que quiero que redondeé
    dna = dna.replace('N', '')#Para hacer que ya no cuente las Ns, se pone vacío 
    length = len(dna) 
    a_count = dna.upper().count('A') 
    t_count = dna.upper().count('T') 
    at_content = (a_count + t_count) / length 
    return round (at_content, num)#round permite redondear a x decimales


at_content = get_at_content("ATGACTGGACCA", 2)#Se deben pasar dos argumentos a la función
print("ATGACTGGACCA" + ": " + str(at_content))
print("AT content ATGACTGGACCA  is " + str(get_at_content("ATGACTGGACCA", 3)))
print(get_at_content("ATGCGCGATCGATCGAATCG", 2))
print(get_at_content ("actcccgatgag", 4)) #PASO DE ARGUMENTOS POR POSICIÓN

print(get_at_content(dna="TCAGCACT", num=2))#PASO POR PALABRAS CLAVE O ARGUMENTO:tambien se puede hacer el llamdo ocupando el nombre de los parametros
print(get_at_content(num=2, dna="TCAGCACT"))#si usamos el nombre no importa el orden 
print(get_at_content("GGCATCGATGC", num=1))#PASO POR POSICIÓN Y NOMBRE:ya no se usa el nombre de un parametro
# print(get_at_content(dna="GGCATCGATGC", 2))#Este no funciona porque primero van los argumentos posicionales y luego los de nombre


#Probando funcion get_at_content
assert get_at_content("ATGC", 2) == 0.5 #ok, no imprime nada solo dice corri la funcion y si da lo que pusiste jsjs
# assert get_at_content("ATGC", 2) == 0.4 #es falso y me dice que hay un error al ejecutar el programa: AssertionError
assert get_at_content("ATGCNNNNNNN", 2) == 0.5 #la funcion no regresa un ok porque si esta contando las Ns
#print(get_at_content("ATGCNNNNNNN", 2)) #En realidad es 0.18
