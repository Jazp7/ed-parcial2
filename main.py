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

# C) Consulta de productos mediante árbol binario de búsqueda

# 11. Crear un árbol binario de búsqueda a partir de códigos numéricos de productos

# 12. Implementar la inserción respetando la propiedad de orden del árbol

# 13. Buscar un código e informar si existe

# 14. Mostrar los códigos mediante un recorrido inorden

# 15. Permitir la eliminación de un código, conservando las propiedades del árbol

# D) Integración, validaciones y demostración

# 16. Integrar las funcionalidades en un menú de consola

# 17. Validar entradas y opciones incorrectas

# 18. Demostrar que las tres estructuras funcionan de manera independiente y coordinada dentro del programa

# 19. Presentar pruebas que permitan verificar los resultados
