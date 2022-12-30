
def agregarProducto(idProducto,nombre,color,talla,precio):
    producto=[idProducto,nombre,color,talla,precio]
    return  producto

def buscarProducto(matrizProducto,idProducto):
    datoProducto= "Registro no se encuentra..."
    for i in range(len(matrizProducto)):
        if(matrizProducto[i][0]==idProducto):
            datoProducto= "\nRegistro Encontrado...\n"
            datoProducto+="\nId producto: "+str(matrizProducto[i][0])
            datoProducto+="\nNombre: "+matrizProducto[i][1]
            datoProducto+= "\nColor: " +matrizProducto[i][2]
            datoProducto+= "\nTalla: " +matrizProducto[i][3]
            datoProducto+= "\nPrecio: " +str(matrizProducto[i][4])

            break
    print(datoProducto)
    return 0

def modificarProducto(matrizProducto,idProducto):
    registro= "Registro no se encuentra..."
    opcion=0
    closeCiclo=True
    for i in range(len(matrizProducto)):
        if(matrizProducto[i][0]==idProducto):
            #Preguntar que dato quiere modificar
            registro = "\nRegistro Encontrado\n"
            print(registro)
            while(closeCiclo):
                print("Ingrese El Dato Que Quiere Modificar Del Producto Numero: "+str(idProducto))
                print("1. Nombre: ( "+matrizProducto[i][1]+" ) ")
                print("2. Color: ( "+matrizProducto[i][2]+" ) ")
                print("3. Talla: ( "+matrizProducto[i][3]+" ) ")
                print("4. Precio: ( "+str(matrizProducto[i][4])+" ) ")
                print("5. Salir\n")
                opcion=int(input())
                if (opcion==1):
                    nuevoNombre=input("Ingrese el nuevo nombre del producto: ")
                    matrizProducto[i][1]=nuevoNombre
                    registro = "\nRegistro Modificado...\n"
                elif(opcion==2):
                    nuevoColor=input("Ingrese el nuevo color del producto: ")
                    matrizProducto[i][2]=nuevoColor
                    registro = "\nRegistro Modificado...\n"
                elif(opcion==3):
                    nuevaTalla=input("Ingrese la nueva talla del producto: ")
                    matrizProducto[i][3]=nuevaTalla
                    registro = "\nRegistro Modificado...\n"
                elif(opcion==4):
                    nuevaPrecio=str(input("Ingrese el nuevo precio del producto: "))
                    matrizProducto[i][4]=nuevaPrecio
                    registro = "\nRegistro Modificado...\n"
                else:
                    closeCiclo=False            
            break
    print(registro)
    return 0

def eliminarProducto(matrizProducto,idProducto):
    mensajeEliminado= "\nNo se encuentra...\n"
    for i in range(len(matrizProducto)):
        if(matrizProducto[i][0]==idProducto):
            del matrizProducto[i]
            mensajeEliminado="\nProducto N "+str(idProducto)+" Encontrado Y Eliminado\n"
            break
    print(mensajeEliminado)
    return 0
