
def agregarCliente(idCliente,nombre,celular,direccion):
    cliente=[idCliente,nombre,celular,direccion]
    return  cliente

def buscarCliente(matrisCliente,idCliente):
    datoCliente= "Registro no se encuentra..."
    for i in range(len(matrisCliente)):
        if(matrisCliente[i][0]==idCliente):
            datoCliente= "\nRegistro Encontrado...\n"
            datoCliente+="\nId Cliente: "+str(matrisCliente[i][0])
            datoCliente+="\nNombre: "+matrisCliente[i][1]
            datoCliente += "\nContacto Telefonico: " +str(matrisCliente[i][2])
            datoCliente += "\nDirección: " + str(matrisCliente[i][3])
            break
    print(datoCliente)
    return 0

def modificarCliente(matrisCliente,idCliente):
    registro= "Registro no se encuentra..."
    opcion=0
    closeCiclo=True
    for i in range(len(matrisCliente)):
        if(matrisCliente[i][0]==idCliente):
            #Preguntar que dato quiere modificar
            registro = "\nRegistro Encontrado\n"
            print(registro)
            while(closeCiclo):
                print("Ingrese El Dato Que Quiere Modificar Del Cliente Numero: "+str(idCliente))
                print("1. Nombre: ( "+matrisCliente[i][1]+" ) ")
                print("2. Contacto Telefonico: ( "+str(matrisCliente[i][2])+" ) ")
                print("3. Dirección: ( "+str(matrisCliente[i][3])+" ) ")
                print("4. Salir\n")
                opcion=int(input())
                if (opcion==1):
                    nuevoNombre=input("Ingrese el nuevo nombre del Cliente: ")
                    matrisCliente[i][1]=nuevoNombre
                    registro = "\nRegistro Modificado...\n"
                elif(opcion==2):
                    nuevoContacto=int(input("Ingrese el nuevo contacto del Cliente: "))
                    matrisCliente[i][2]=nuevoContacto
                    registro = "\nRegistro Modificado...\n"
                elif(opcion==3):
                    nuevaDire=str(input("Ingrese la nueva dirección del Cliente: "))
                    matrisCliente[i][3]=nuevaDire
                    registro = "\nRegistro Modificado...\n"
                else:
                    closeCiclo=False            
            break
    print(registro)
    return 0

def eliminarCliente(matrisCliente,idCliente):
    mensajeEliminado= "\nNo se encuentra...\n"
    for i in range(len(matrisCliente)):
        if(matrisCliente[i][0]==idCliente):
            del matrisCliente[i]
            mensajeEliminado="\nCliente N "+str(idCliente)+" Encontrado Y Eliminado\n"
            break
    print(mensajeEliminado)
    return 0
