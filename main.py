"""
Caso empresarial: Sistema de gestión de pedidos de una distribuidora

Una distribuidora de productos tecnológicos “Las naranjas” necesita un prototipo en Python para gestionar las solicitudes de sus clientes, controlar las últimas operaciones de despacho y consultar productos por su código. Actualmente, las tareas manuales ocasionan errores en el orden de atención, dificultad para revisar operaciones recientes y demoras al localizar productos.

Desarrolle un programa de consola que utilice una cola FIFO, una pila LIFO y un árbol binario de búsqueda.
"""

"""
Datos iniciales obligatorios
Cola FIFO: Solicitudes P001, P002, P003, registradas en ese orden, con sus datos como estudiantes.
Pila LIFO: Despachos D001, D002, D003, registrados en ese orden.
Árbol binario de búsqueda: Códigos: 50, 30, 70, 20, 40, 60, 80, insertados en ese orden.
"""

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

"""
A) Gestión de solicitudes mediante FIFO
"""

solicitudes = []

# 1. Registrar solicitudes con un código y el nombre del cliente (nombre de los estudiantes)

def registrar_solicitud(codigo, nombre_cliente):
    solicitud = {
        "codigo": codigo,
        "nombre_cliente": nombre_cliente
    }
    return solicitud


# 2. Agregar cada solicitud al final de la cola

solicitudes.append(registrar_solicitud("P001", "Evelin Carolina"))
solicitudes.append(registrar_solicitud("P002", "José Arístides"))
solicitudes.append(registrar_solicitud("P003", "Julio Román"))

# 3. Atender la siguiente solicitud respetando el orden de llegada

def atender_solicitud():
    if solicitudes:
        return solicitudes.pop(0)
    return None

# 4. Mostrar las solicitudes pendientes

def mostrar_solicitudes_pendientes():
    for solicitud in solicitudes:
        print(f"{solicitud['codigo']} - {solicitud['nombre_cliente']}")

# 5. Controlar cuando no existan solicitudes para atender

def atender_solicitud_con_control():
    solicitud = atender_solicitud()
    if solicitud is None:
        print("No existen solicitudes para atender.")
    else:
        print(f"Solicitud atendida: {solicitud['codigo']} - {solicitud['nombre_cliente']}")


"""
B) Registro de despachos mediante LIFO
"""

despachos = []

# 6. Registrar un despacho con código de operación y código de producto

def registrar_despacho(codigo_operacion, codigo_producto):
    despacho = {
        "codigo_operacion": codigo_operacion,
        "codigo_producto": codigo_producto
    }
    return despacho

# 7. Agregar cada despacho a la pila

despachos.append(registrar_despacho("D001", "Producto 1"))
despachos.append(registrar_despacho("D002", "Producto 2"))
despachos.append(registrar_despacho("D003", "Producto 3"))

# 8. Consultar los despachos registrados

def consultar_despachos():
    for despacho in reversed(despachos):
        print(f"{despacho['codigo_operacion']} - {despacho['codigo_producto']}")

# 9. Retirar el último despacho registrado mediante desapilado

def retirar_despacho():
    if despachos:
        return despachos.pop()
    return None

# 10. Controlar el intento de retirar elementos cuando la pila esté vacía

def retirar_despacho_con_control():
    despacho = retirar_despacho()
    if despacho is None:
        print("No existen despachos para retirar.")
    else:
        print(
            f"Despacho retirado: {despacho['codigo_operacion']} - "
            f"{despacho['codigo_producto']}"
        )


"""
C) Consulta de productos mediante árbol binario de búsqueda
"""

# 11. Crear un árbol binario de búsqueda a partir de códigos numéricos de productos

class Nodo:
    def __init__(self, codigo):
        self.codigo = codigo
        self.izquierda = None
        self.derecha = None


raiz = None

# 12. Implementar la inserción respetando la propiedad de orden del árbol

def insertar(raiz, codigo):
    if raiz is None:
        return Nodo(codigo)

    if codigo < raiz.codigo:
        raiz.izquierda = insertar(raiz.izquierda, codigo)
    elif codigo > raiz.codigo:
        raiz.derecha = insertar(raiz.derecha, codigo)

    return raiz


for codigo in [50, 30, 70, 20, 40, 60, 80]:
    raiz = insertar(raiz, codigo)

# 13. Buscar un código e informar si existe

def buscar(raiz, codigo):
    if raiz is None:
        return False
    if raiz.codigo == codigo:
        return True
    if codigo < raiz.codigo:
        return buscar(raiz.izquierda, codigo)
    return buscar(raiz.derecha, codigo)

# 14. Mostrar los códigos mediante un recorrido inorden

def recorrido_inorden(raiz):
    codigos = []

    if raiz is not None:
        codigos.extend(recorrido_inorden(raiz.izquierda))
        codigos.append(raiz.codigo)
        codigos.extend(recorrido_inorden(raiz.derecha))

    return codigos


def mostrar_inorden():
    print(recorrido_inorden(raiz))

# 15. Permitir la eliminación de un código, conservando las propiedades del árbol

def eliminar(raiz, codigo):
    if raiz is None:
        return None

    if codigo < raiz.codigo:
        raiz.izquierda = eliminar(raiz.izquierda, codigo)
    elif codigo > raiz.codigo:
        raiz.derecha = eliminar(raiz.derecha, codigo)
    else:
        if raiz.izquierda is None:
            return raiz.derecha
        if raiz.derecha is None:
            return raiz.izquierda

        sucesor = raiz.derecha
        while sucesor.izquierda is not None:
            sucesor = sucesor.izquierda

        raiz.codigo = sucesor.codigo
        raiz.derecha = eliminar(raiz.derecha, sucesor.codigo)

    return raiz


"""
D) Integración, validaciones y demostración
"""

# 16. Integrar las funcionalidades en un menú de consola

def mostrar_menu():
    print("\n--- Sistema de pedidos ---")
    print("1. Mostrar solicitudes pendientes")
    print("2. Atender solicitud")
    print("3. Mostrar despachos")
    print("4. Retirar despacho")
    print("5. Buscar producto")
    print("6. Mostrar productos en orden")
    print("7. Eliminar producto")
    print("8. Ejecutar demostración")
    print("9. Ejecutar pruebas")
    print("0. Salir")


def ejecutar_menu():
    global raiz

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            if solicitudes:
                mostrar_solicitudes_pendientes()
            else:
                print("No hay solicitudes pendientes.")
        elif opcion == "2":
            atender_solicitud_con_control()
        elif opcion == "3":
            if despachos:
                consultar_despachos()
            else:
                print("No hay despachos registrados.")
        elif opcion == "4":
            retirar_despacho_con_control()
        elif opcion == "5":
            codigo = leer_entero("Ingrese el código del producto: ")
            if buscar(raiz, codigo):
                print("El producto existe.")
            else:
                print("El producto no existe.")
        elif opcion == "6":
            mostrar_inorden()
        elif opcion == "7":
            codigo = leer_entero("Ingrese el código del producto a eliminar: ")
            if buscar(raiz, codigo):
                raiz = eliminar(raiz, codigo)
                print("Producto eliminado correctamente.")
            else:
                print("El producto no existe.")
        elif opcion == "8":
            ejecutar_demostracion()
        elif opcion == "9":
            ejecutar_pruebas()
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opción incorrecta. Seleccione una opción del 0 al 9.")

# 17. Validar entradas y opciones incorrectas

def leer_entero(mensaje):
    while True:
        valor = input(mensaje)
        try:
            return int(valor)
        except ValueError:
            print("Entrada incorrecta. Debe ingresar un número entero.")

# 18. Demostrar que las tres estructuras funcionan de manera independiente y coordinada dentro del programa

def ejecutar_demostracion():
    print("\n--- Demostración del sistema ---")
    print("Solicitudes pendientes:")
    mostrar_solicitudes_pendientes()

    solicitud = atender_solicitud()
    if solicitud is not None:
        print(f"Solicitud atendida: {solicitud['codigo']} - {solicitud['nombre_cliente']}")

    print("Despachos registrados:")
    consultar_despachos()

    despacho = retirar_despacho()
    if despacho is not None:
        print(f"Último despacho retirado: {despacho['codigo_operacion']}")

    print(f"Productos en orden: {recorrido_inorden(raiz)}")
    print(f"¿Existe el producto 60?: {'Sí' if buscar(raiz, 60) else 'No'}")

# 19. Presentar pruebas que permitan verificar los resultados

def ejecutar_pruebas():
    solicitudes_prueba = []
    solicitudes_prueba.append(registrar_solicitud("P001", "Estudiante 1"))
    solicitudes_prueba.append(registrar_solicitud("P002", "Estudiante 2"))
    assert solicitudes_prueba.pop(0)["codigo"] == "P001"

    despachos_prueba = []
    despachos_prueba.append(registrar_despacho("D001", "Producto 1"))
    despachos_prueba.append(registrar_despacho("D002", "Producto 2"))
    assert despachos_prueba.pop()["codigo_operacion"] == "D002"

    raiz_prueba = None
    for codigo in [50, 30, 70, 20, 40, 60, 80]:
        raiz_prueba = insertar(raiz_prueba, codigo)

    assert recorrido_inorden(raiz_prueba) == [20, 30, 40, 50, 60, 70, 80]
    assert buscar(raiz_prueba, 60) is True
    assert buscar(raiz_prueba, 99) is False

    raiz_prueba = eliminar(raiz_prueba, 20)
    assert recorrido_inorden(raiz_prueba) == [30, 40, 50, 60, 70, 80]
    print("Pruebas del árbol: correctas.")
    print("Las estructuras FIFO, LIFO y el árbol están funcionando.")


if __name__ == "__main__":
    ejecutar_menu()
