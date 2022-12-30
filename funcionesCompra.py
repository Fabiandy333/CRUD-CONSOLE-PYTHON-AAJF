def realizarCompra(nombreMaterial,cantidad,nitProveedor):
    #Crear una venta
    compra=[nombreMaterial,cantidad,nitProveedor]
    return  compra

def historialCompra(matrizCompra):
    datoCompra= "No se encuentras registros..."
    for i in range(len(matrizCompra)):
        datoCompra += "\n------------ Registro N "+str(i+1)+" --------------"
        datoCompra+="\nMaterial: "+str(matrizCompra[i][0])
        datoCompra+="\nCantidad: "+str(matrizCompra[i][1])
        datoCompra += "\nNitProveedor: "+str(matrizCompra[i][2])
    print(datoCompra)
    return 0