def realizarVenta(idCliente,idProducto,cantidad):
    #Crear una venta
    venta=[idCliente,idProducto,cantidad,]
    return  venta
    
    #Buscar si un id esta en una matriz
def buscarId(id,matriz):
    dato= False
    for i in range(len(matriz)):
        if(matriz[i][0]==id):
            dato= True
            break
    return dato

def historialVenta(matrisVenta):
    datoVentas= "No se encuentras registros..."
    for i in range(len(matrisVenta)):
        datoVentas += "\n------------ Registro N "+str(i+1)+" --------------"
        datoVentas+="\nId Cliente: "+str(matrisVenta[i][0])
        datoVentas+="\nId Producto: "+str(matrisVenta[i][1])
        datoVentas += "\nCantidad: " +str(matrisVenta[i][2])
    print(datoVentas)
    return 0