def agregarProveedor(NitProveedor,nombre,celular,direccion):
    proveedor=[NitProveedor,nombre,celular,direccion]
    return  proveedor

def buscarProveedor(matrizProveedor,idProveedor):
    datoProveedor= "Registro no se encuentra..."
    for i in range(len(matrizProveedor)):
        if(matrizProveedor[i][0]==idProveedor):
            datoProveedor= "\nRegistro Encontrado...\n"
            datoProveedor+="\nNit: "+str(matrizProveedor[i][0])
            datoProveedor+="\nNombre: "+matrizProveedor[i][1]
            datoProveedor += "\nContacto Telefonico: " +str(matrizProveedor[i][2])
            datoProveedor += "\nDirección: " + str(matrizProveedor[i][3])

            break
    print(datoProveedor)
    return 0

def modificarProveedor(matrizProveedor,idProveedor):
    registro= "Registro no se encuentra..."
    opcion=0
    closeCiclo=True
    for i in range(len(matrizProveedor)):
        if(matrizProveedor[i][0]==idProveedor):
            #Preguntar que dato quiere modificar
            registro = "\nRegistro Encontrado\n"
            print(registro)
            while(closeCiclo):
                print("Ingrese El Dato Que Quiere Modificar Del Proveedor Numero: "+str(idProveedor))
                print("1. Nombre: ( "+matrizProveedor[i][1]+" ) ")
                print("2. Contacto Telefonico: ( "+str(matrizProveedor[i][2])+" ) ")
                print("3. Dirección: ( "+str(matrizProveedor[i][3])+" ) ")
                print("4. Salir\n")
                opcion=int(input())
                if (opcion==1):
                    nuevoNombre=input("Ingrese el nuevo nombre del Proveedor: ")
                    matrizProveedor[i][1]=nuevoNombre
                    registro = "\nRegistro Modificado...\n"
                elif(opcion==2):
                    nuevoContacto=int(input("Ingrese el nuevo contacto del Proveedor: "))
                    matrizProveedor[i][2]=nuevoContacto
                    registro = "\nRegistro Modificado...\n"
                elif(opcion==3):
                    nuevaDire=str(input("Ingrese la nueva dirección del Proveedor: "))
                    matrizProveedor[i][3]=nuevaDire
                    registro = "\nRegistro Modificado...\n"
                else:
                    closeCiclo=False            
            break
    print(registro)
    return 0

def eliminarProveedor(matrizProveedor,idProveedor):
    mensajeEliminado= "\nNo se encuentra...\n"
    for i in range(len(matrizProveedor)):
        if(matrizProveedor[i][0]==idProveedor):
            del matrizProveedor[i]
            mensajeEliminado="\nProveedor Con Nit N "+str(idProveedor)+" Encontrado Y Eliminado\n"
            break
    print(mensajeEliminado)
    return 0
