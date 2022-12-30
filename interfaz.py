espacio="********************************************************************************************"
encabezado="************************************** SOWTWARE AAJF ***************************************"

#FUNCIONES INTERFAZ

#Esta funciòn retorna un string para la parte del subtitulos del software
def subinterfaz(stringOption,option):
    if(option==1):
        subMenu="**--------- AGREGAR "+stringOption+" -------------------------------------------------------**"
    elif(option==2):
        subMenu="**--------- MODIFICAR "+stringOption+" -----------------------------------------------------**"
    elif (option==3):
        subMenu="**--------- ELIMINAR "+stringOption+" ------------------------------------------------------**"
    elif (option==4):
        subMenu="**--------- BUSCAR "+stringOption+" --------------------------------------------------------**"
    else:
        subMenu="************************************** "+stringOption+" ***************************************"
    return subMenu

#Esta funciòn imprime el encabezado completo del software
def interfaz(stringOption,option):
    print("\n",espacio,"\n",encabezado,"\n",espacio,"\n")
    a=subinterfaz(stringOption,option)
    print(a)
    return 0
    
    
def opcionesPrincipales():
    print("** Selecciona una opciòn: ")
    print("** 1.CLIENTE ")
    print("** 2.PRODUCTO ")
    print("** 3.VENTAS ")
    print("** 4.COMPRAS ")
    print("** 5.PROVEEDORES ")
    print("** 6.SALIR DEL PROGRAMA <--")
    print("*********************************************************************************************")
    return 0

def opciones():
    print("** Selecciona una opciòn: ")
    print("** 1.Agregar ")
    print("** 2.Modificar ")
    print("** 3.Eliminar ")
    print("** 4.Buscar ")
    print("** 5.Salir <--")
    print("*********************************************************************************************")
    return 0
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def opciones2():
    print("** Selecciona una opciòn: ")
    print("** 1.Realizar Venta ")
    print("** 2.Historial De Venta ")
    print("** 3.Salir <--")
    print("*********************************************************************************************")
    return 0
    
    
    
    
    
    
def opciones3():
    print("** Selecciona una opciòn: ")
    print("** 1.Realizar Compra ")
    print("** 2.Historial De Compra ")
    print("** 3.Salir <--")
    print("*********************************************************************************************")
    return 0
