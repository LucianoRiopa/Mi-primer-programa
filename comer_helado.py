queres_helado_input = input("¿Queres un helado? (Si/No)").upper()

if queres_helado_input == "Si":
    queres_helado = True
elif queres_helado_input == "No":
    queres_helado = False
else:
    print("Te he dicho que me digas si o no, no se que has dicho pero cuento como que no")
    queres_helado = False

tiene_dinero_input = input("¿ Tienes dinero para un helado ?").upper()
esta_el_senor_helados_input = input("¿Esta el señor de los helados?").upper()
esta_tu_tia_input = input("¿Estas con tu tia?").upper()


queres_helado = queres_helado_input =="Si"
tiene_dinero = tiene_dinero_input == "Si"
esta_tu_tia = esta_tu_tia_input == "Si"
puede_permitirselo = tiene_dinero or esta_tu_tia
esta_el_senor_helados = esta_el_senor_helados_input == "Si"


if queres_helado == "si" and (tiene_dinero == "Si" or esta_tu_tia == "Si") and esta_el_senor_helados == "Si":
    print("Pues toma tu helado")
else:
    print("Pues nada")



