from os import system
from interfaz import *
from funcionesCliente import *
from funcionesProducto import *
from funcionesProveedor import *
from funcionesVenta import *
from funcionesCompra import *

closeProgram=True
matrizCliente=[]
matrizProducto=[]
matrizProveedor=[]
matrizVenta=[]
matrizCompra=[]
option = 0

#Manejo funciones de la interfaz
system("cls")
while (closeProgram):
    interfaz("MENU PRINCIPAL",0)
    opcionesPrincipales()
    option=int(input())
    closeProgram2=True
    system("cls")

    if (option == 1):
        while (closeProgram2):
            interfaz("CLIENTE", 0)
            opciones()
            option2 = int(input())
            system("cls")
            if (option2==1):
                interfaz("AGREGAR CLIENTE", 0)
                idCliente=int(input("Por favor ingrese el id del cliente: "))
                nombreCliente=input("Por favor ingrese el nombre del cliente: ")
                celularCliente=int(input("Por favor ingrese el telefono del cliente: "))
                direccionCliente=input("Por favor ingrese la direccion del cliente: ")
                #Agregamos los input recibidos por el usuario mediante una funcion a la matriz cliente
                matrizCliente.append(agregarCliente(idCliente,nombreCliente,celularCliente,direccionCliente))
                print("\nCliente N "+str(idCliente)+" agregado Con Exito...\n")

            elif (option2==2):
                interfaz("MODIFICAR CLIENTE", 0)
                idCliente = int(input("Por favor ingrese el id del cliente: "))
                #Enviamos a la funcion modificarCliente el id digitado por el usuario y la matriz cliente
                modificarCliente(matrizCliente,idCliente) 

            elif (option2==3):
                interfaz("ELIMINAR CLIENTE", 0)
                idCliente = int(input("Por favor ingrese el id del cliente: "))
                #Enviamos a la funcion eliminarCliente el id digitado por el usuario y la matriz cliente
                eliminarCliente(matrizCliente,idCliente)
                
            elif (option2==4):
                interfaz("BUSCAR CLIENTE", 0)
                idCliente = int(input("Por favor ingrese el id del cliente: "))
                #Enviamos a la funcion buscarCliente el id digitado por el usuario y la matriz cliente
                buscarCliente(matrizCliente,idCliente)
            else:
                closeProgram2 = False

    elif (option == 2):
        while (closeProgram2):
            interfaz("PRODUCTO", 0)
            opciones()
            option2 = int(input())
            system("cls")
            if (option2==1):
                interfaz("AGREGAR PRODUCTO", 0)
                idProducto=int(input("Por favor ingrese el id del producto: "))
                nombreProducto=input("Por favor ingrese un nombre al producto: ")
                colorProducto=input("Por favor ingrese el Color del producto: ")
                tallaProducto=input("Por favor ingrese la talla del producto: ")
                precioProducto=int(input("Por favor ingrese el precio del producto: "))
                #Agregamos los input recibidos por el usuario mediante una funcion a la matriz producto
                matrizProducto.append(agregarProducto(idProducto,nombreProducto,colorProducto,tallaProducto,precioProducto))
                print("\nProducto N "+str(idProducto)+" agregado Con Exito...\n")

            elif (option2==2):
                interfaz("MODIFICAR PRODUCTO", 0)
                idProducto = int(input("Por favor ingrese el id del producto: "))
                #Enviamos a la funcion modificarProducto el id digitado por el usuario y la matriz producto
                modificarProducto(matrizProducto,idProducto)

            elif (option2==3):
                interfaz("ELIMINAR PRODUCTO", 0)
                idProducto = int(input("Por favor ingrese el id del producto: "))
                #Enviamos a la funcion eliminarProducto el id digitado por el usuario y la matriz producto
                eliminarProducto(matrizProducto,idProducto)

            elif (option2==4):
                interfaz("BUSCAR PRODUCTO", 0)
                idProducto = int(input("Por favor ingrese el id del producto: "))
                #Enviamos a la funcion buscarProducto el id digitado por el usuario y la matriz producto
                buscarProducto(matrizProducto,idProducto)
            else:
                closeProgram2 = False

    elif (option == 3):
        while (closeProgram2):
            interfaz("VENTAS", 0)
            opciones2()
            option2 = int(input())
            system("cls")
            if (option2==1):
                if (len(matrizCliente)>=1 and len(matrizProducto)>=1):
                    interfaz("REALIZAR VENTA", 0)
                    print("REGISTROS DATOS DEL CLIENTE:")
                    print("ID,NOMBRE,CELULAR,DIRECCION")
                    print(matrizCliente)
                    idCliente=int(input("\nPor favor ingrese el id del cliente: "))
                    
                    print("\nREGISTROS DATOS DEL PRODUCTO:")
                    print("ID,NOMBRE,COLOR,TALLA,PRECIO")
                    print(matrizProducto)
                    idProducto=int(input("\nPor favor ingrese el id del producto: "))
                    #Verificar si esta el cliente y el producto que digito el usuario estan para realizar laa VENTAS
                    if(buscarId(idCliente,matrizCliente) and buscarId(idProducto,matrizProducto)):
                        #Enviamos a la funcion realizarVenta el id digitado por el usuario de cliente y producto mas la matriz cliente, producto y cantidad para registrar venta
                        cantidad=int(input("\nPor favor ingrese la cantidad: "))
                        
                        matrizVenta.append(realizarVenta(idCliente,idProducto,cantidad))
                        print("Venta Agregada Exitosamente...")
                    else:
                        print("El cliente o el producto que ingreso no se encuentran,Intenta de nuevo: ")
                    
                else:
                    print("No Hay Registros De Productos O Clientes Para Crear Una Venta.")
            elif (option2==2):
                historialVenta(matrizVenta)
            else:
                closeProgram2 = False

    elif (option == 4):
        while (closeProgram2):
            interfaz("COMPRAS", 0)
            opciones3()
            option2 = int(input())
            system("cls")
            if (option2==1):
                if (len(matrizProveedor)>=1):
                    interfaz("REALIZAR COMPRA", 0)
                    print("REGISTROS DATOS DEL PROVEEDOR:")
                    print("NIT,NOMBRE,CELULAR,DIRECCION")
                    print(matrizProveedor)
                    nitProveedor=int(input("\nPor favor ingrese el id del proveedor al que desea comprar: "))
                    #Verificar si esta elproveedor que digito el usuario estan para realizar laa compra
                    if(buscarId(nitProveedor,matrizProveedor)):
                        #Enviamos a la funcion realizarVenta el id digitado por el usuario de cliente y producto mas la matriz cliente, producto y cantidad para registrar venta
                        nombreMaterial=input("\nPor favor ingrese el nombre del material: ")
                        cantidad=int(input("\nPor favor ingrese la cantidad: "))
                        #agregamnos los datos a una funcion lo cual retorna una lista de compras y se lo agregamos a la matriz compras
                        matrizCompra.append(realizarCompra(nombreMaterial,cantidad,nitProveedor))
                        print("Compra Agregada Exitosamente...")
                    else:
                        print("El Proveedor que ingreso no se encuentran,Intenta de nuevo: ")
                    
                else:
                    print("No Hay Registros De Proveedores Para Crear Una Compra.")
            elif (option2==2):
                historialCompra(matrizCompra)
            else:
                closeProgram2 = False

    elif (option == 5):
        while (closeProgram2):
            interfaz("PROVEEDORES", 0)
            opciones()
            option2 = int(input())
            system("cls")
            if (option2==1):
                interfaz("AGREGAR PROVEEDOR", 0)
                nitProveedor=int(input("Por favor ingrese el nit del proveedor: "))
                nombreProveedor=input("Por favor ingrese el nombre del proveedor: ")
                celularProveedor=int(input("Por favor ingrese el telefono del proveedor: "))
                direccionProveedor=input("Por favor ingrese la direccion del proveedor: ")
                #Agregamos los input recibidos por el usuario mediante una funcion a la matriz Proveedor
                matrizProveedor.append(agregarProveedor(nitProveedor,nombreProveedor,celularProveedor,direccionProveedor))
                print("\nProveedor N "+str(nitProveedor)+" agregado Con Exito...\n")

            elif (option2==2):
                interfaz("MODIFICAR PROVEEDOR", 0)
                nitProveedor = int(input("Por favor ingrese el nit del proveedor: "))
                #Enviamos a la funcion modificarProveedor el id digitado por el usuario y la matriz proveedor
                modificarProveedor(matrizProveedor,nitProveedor)

            elif (option2==3):
                interfaz("ELIMINAR PROVEEDOR", 0)
                nitProveedor = int(input("Por favor ingrese el nit del proveedor: "))
                #Enviamos a la funcion eliminarProveedor el id digitado por el usuario y la matriz proveedor
                eliminarProveedor(matrizProveedor,nitProveedor)
                
            elif (option2==4):
                interfaz("BUSCAR PROVEEDOR", 0)
                nitProveedor = int(input("Por favor ingrese el nit del proveedor: "))
                #Enviamos a la funcion buscarProveedor el id digitado por el usuario y la matriz proveedor
                buscarProveedor(matrizProveedor,nitProveedor)
            else:
                closeProgram2 = False
    else:
        closeProgram=False
